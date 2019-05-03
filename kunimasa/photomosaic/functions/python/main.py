# -*- coding: utf-8 -*-
#import os
#import sys
#sys.path.insert(0, os.getcwd() + '/libs')
import math
import random
import numpy as np
import requests
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageFile, ImageMath

import base64

# enable to load too large photo
ImageFile.LOAD_TRUNCATED_IMAGES = True

def _blend_f(bands1, bands2, func):
    blend = "convert(func(float(a), float(b)), 'L')"
    bands = [
        ImageMath.eval(
            blend,
            a=a,
            b=b,
            func=func
        )
        for a, b in zip(bands1, bands2)
    ]
    return Image.merge("RGB", bands)

def _over_lay(a, b):
    _cl = 2 * a * b / 255
    _ch = 2 * (a + b - a * b / 255) - 255
    return _cl * (a < 128) + _ch * (a >= 128)


def url2im(url):
    try:
        if("data:" in url):
            dec_data = base64.b64decode( url.split(',')[1] ) # 環境依存の様(","で区切って本体をdecode)
            im  = Image.open(BytesIO(dec_data))
        else:
            im = Image.open(BytesIO(requests.get(url).content))

        return im
    except:
        return None

def im2buf(im, format='JPEG'):
    buf = BytesIO()
    im.save(buf, format=format)
    return buf

def im2dataurl(im, content_type='image/jpeg'):
    buf = im2buf(im,"JPEG")
    buf = buf.getvalue();
    base64str = base64.b64encode(buf).decode()
    return "data:{};base64,{}".format(content_type,base64str)



def resize(im, zoom_ratio_y, zoom_ratio_x):

    # 画像のリサイズ
    #    resize = cv2.resize(im, (int(zoom_ratio_x), int(zoom_ratio_y)))
    resize = im.resize((int(zoom_ratio_x), int(zoom_ratio_y)))

    return resize


def get_roi(im, sy, ey, sx, ex):
    roi = im.crop((sx, sy, ex, ey))
    return roi


def get_photo_mozaic_im(basePath, subPaths,pixel=50):
    if(pixel is None): pixel=50
    im = url2im(basePath)  # Image.open(basePath)
    if(not im):
        print('faild to load')
        quit()

    width, height = im.size
    target_min_size = 2400
    min_size = min(width,height)
    resize_rate = max(target_min_size/min_size,1)
    width =math.ceil(width*resize_rate);
    height =math.ceil(height*resize_rate);
    im = resize(im,height,width)

    # div_size pixel
    div_size_h = pixel #int(height / div_num_h)
    div_size_w = pixel #int(width / div_num_w)

    resized_file_list = []

    # サブ画像を縮小し、そのRGB値を算出する
    # 縮小率 サブ画像のサイズ
    resized_file_list = []
    resized_file_rgb = []

    print(" --- downloading photos ")
    with ThreadPoolExecutor(max_workers=30) as executor:
        sub_ims = executor.map(url2im, subPaths)
    sub_ims = list(sub_ims)
    sub_ims = [sub_im for sub_im in sub_ims if sub_im is not None]

    print(" --- processing photo mozaic")
    for sub_im in sub_ims:

        # サブ画像を縮小したときのサイズを算出...
        zoom_y_ratio = div_size_h #height / float(div_num_h)
        zoom_x_ratio = div_size_w #width / float(div_num_w)

        # 縮小実施する
        resized = resize(sub_im, zoom_y_ratio, zoom_x_ratio)
        resized_file_list.append(resized)
        # サブ画像の平均RGB値
        resize_averages = np.asarray(resized.convert('RGB')).mean(0).mean(0)
        resized_file_rgb.append(resize_averages)

    resized_file_rgb = np.array(resized_file_rgb)
    # ROIそれぞれの平均RGBを求める
    # ひとまず逐一処理を実施...。
    im_effect = Image.new('RGB',(width,height),(0,0,0))

    sys = range(0, height, div_size_h)
    sxs = range(0, width, div_size_w)
    base_div_len = len(sys)*len(sxs)
    sub_len = len(resized_file_list)
    sub_set = base_div_len // sub_len
    sub_mod = base_div_len % sub_len

    idx = []
    sub_idx = range(sub_len)
    for s in range(0,sub_set):
        idx.extend(random.sample(sub_idx,sub_len))
    idx.extend(random.sample(sub_idx,sub_mod))

    cnt = 0
    for sy in sys:
        for sx in sxs:
            try:
                # ROIにサブ画像をはめ込み
                im_effect.paste(resized_file_list[idx[cnt]], (sx, sy))
                cnt+=1
            except:
                print("error")

    # image overlay
    im = _blend_f(im.split(), im_effect.split(), _over_lay)

    return im


def photomosaic(request):
    token = request.headers.get('Authorization')
    data = request.get_json()
    if(token!='hogehoge'): return "invalid authorization"
    if(not("url_base" in data and "url_photos" in data)): return "url_base and url_photos are required in payload"
    url_base = data["url_base"]
    url_photos = data["url_photos"]
    pixel = data.get('pixel')
    print(url_base)
    im = get_photo_mozaic_im(url_base,url_photos,pixel)
    return im2dataurl(im)

if __name__ == "__main__":
    print("getting photo urls from google photos")
    unsplash = "https://source.unsplash.com/500x500/?nature,"
    photoUrls = [unsplash+str(i) for i in range(100)];
    photoUrls.append("/2Q==")
    baseUrls = "https://welove.expedia.co.jp/wp-content/uploads/2016/12/shutterstock_346551977_2-810x606.jpg"
    print("generating photo mozaic")
    im = get_photo_mozaic_im(baseUrls, photoUrls,100)
    print("successfully generated")
    res = im2dataurl(im)
#    print(res)
    im.show()
#    uploadPhoto(im)
