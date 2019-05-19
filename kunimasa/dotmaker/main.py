from sklearn.cluster import KMeans
from PIL import Image
import numpy as np
from io import BytesIO
import requests

def url2im(url):
    try:
        if("data:" in url):
            dec_data = base64.b64decode( url.split(',')[1])
            im  = Image.open(BytesIO(dec_data))
        else:
            im = Image.open(BytesIO(requests.get(url).content))

        return im
    except Exception as e:
        print(e)
        return None

def resize(im, zoom_ratio_y, zoom_ratio_x):
    return im.resize((int(zoom_ratio_x), int(zoom_ratio_y)))

def get_roi(im, sy, ey, sx, ex):
    roi = im.crop((sx, sy, ex, ey))
    return roi

def create_dot_im(rgb,height,width):
    return Image.fromarray(np.uint8(np.tile(rgb,(height,width,1))))


base_path = "https://welove.expedia.co.jp/wp-content/uploads/2016/12/shutterstock_346551977_2-810x606.jpg"

def make_dot_im(img_url,unique_colors=8):
  im = url2im(img_url)  # Image.open(basePath)
  im = im.convert('RGB')

  width, height = im.size

  # div_size pixel
  h = 5 #int(height / div_num_h)
  w = 5 #int(width / div_num_w)

  re_im = resize(im,300,300);
  base_rgb_array = np.array(re_im);
  re_w,re_h,_ = base_rgb_array.shape;
  base_rgb_array = base_rgb_array.reshape([re_h*re_w,3])

  clusters = KMeans(n_clusters=unique_colors,n_jobs=-1).fit_predict(base_rgb_array);
  colors = np.array([base_rgb_array[clusters==i].mean(0) for i in range(unique_colors)])

  sub_ims = [create_dot_im(color,h,w) for color in colors];

  # replace base image with near-color dots
  for sy in range(0, height-1, h):
      for sx in range(0, width-1, w):
          roi = get_roi(im, sy, sy + h, sx, sx + w)
          base_rgb = np.array(roi).mean(0).mean(0)
          idx = np.argmin(np.sum(abs(colors - base_rgb), axis=1))
          im.paste(sub_ims[idx], (sx, sy))

  # image return
  return im


# --- api & debug

def im2buf(im, format='JPEG'):
    buf = BytesIO()
    im.save(buf, format=format)
    return buf

import base64
def im2dataurl(im, content_type='image/jpeg'):
    buf = im2buf(im,"JPEG")
    buf = buf.getvalue();
    base64str = base64.b64encode(buf).decode()
    return "data:{};base64,{}".format(content_type,base64str)

import flask
import json
def dotmaker(request):
    token = request.headers.get('Authorization')
    data = request.get_json()
    print('response data',request.method,data,request.json,request.data,[request.headers])
    def res(data):
        headers={
            "Access-Control-Allow-Origin" : "*",
            "Cache-Control" : "public,max-age=300",
            "Content-Type":"application/json",
            "Access-Control-Allow-Headers":"Content-Type,Authorization,Access-Control-Allow-Origin"
        }
        print(data,headers)
        return (json.dumps(data),headers)

    if(token!='hogehoge'): return res(["invalid authorization",token])
    if(not data): return res('post data is none')
    if(not("url_img" in data)): return res(["url_img is required in payload"])
    url_img = data["url_img"]
    unique_colors = data.get('unique_colors')
    print(url_img)
    im = make_dot_im(url_img,unique_colors)
    dataurl= im2dataurl(im)
    print('dotized',dataurl)
    return res(dataurl)

if __name__ == "__main__":
    unsplash = "https://source.unsplash.com/500x500/?nature"
    print("generating dot image")
    im = make_dot_im(unsplash)
    print("successfully generated")
    im.show()
