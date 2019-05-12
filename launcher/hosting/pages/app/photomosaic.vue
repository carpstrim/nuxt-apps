
<template>
  <div id="app">
    <div style="text-align:center">
      <h3>Photo Mosaic</h3>
    </div>
    <v-container>
      <v-layout wrap>
        <v-flex
          xs12
          sm6
          class="img-box"
        >
          <div class="img-box-inside">
            <div
              class="box-text"
              v-if="!baseImg.url"
            >
              <upload-btn
                :fileChangedCallback="uploadFile('baseImg',true)"
                color="primary"
                title="1.Upload Base-Image"
              ></upload-btn>
            </div>
            <v-img
              :src="baseImg.url"
              v-else
              @dblclick="baseImg={}"
              class="base-img"
              aspect-ratio="1"
            ></v-img>
          </div>
        </v-flex>
        <v-flex
          xs12
          sm6
          class="img-box"
        >
          <div class="img-box-inside">
            <div
              class="box-text"
              v-if="!pmUrl"
            >
              <v-btn
                color="info"
                :disabled="!subImgs.length>0 || !baseImg.url"
                @click="genPhotomosaic"
                :loading="loading.pm"
              >3.Generate Photomosaic</v-btn>
            </div>
            <v-img
              :src="pmUrl"
              v-else
              @dblclick="pmUrl=``"
              class="base-img"
              aspect-ratio="1"
            ></v-img>

          </div>
        </v-flex>
        <v-flex
          xs12
          class="img-box"
        >
          <upload-btn
            :fileChangedCallback="uploadFile('subImgs')"
            color="info"
            title="2.Upload Sub-Image"
            multiple
          ></upload-btn>
        </v-flex>
        <v-flex
          xs12
          class="img-box"
        >{{subImgs.length}}枚/{{totalSubImgSize}} (最大 {{limitSubImg}}枚まで可能)</v-flex>
      </v-layout>
      <v-layout wrap>
        <v-flex
          xs2
          v-for="(subImg,i) in subImgs"
          :key="i"
        >
          <v-card class="sub-img">
            <v-img
              :src="subImg.url"
              aspect-ratio="1"
              @dblclick="subImgs.splice(i,1)"
            />
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>

    <v-dialog
      :v-model="loading.base||loading.sub||loading.pm"
      width="80vw"
    >
      hoge!{{loading}}
    </v-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      subImgs: [],
      baseImg: {},
      pmUrl: "",
      loading: {
        pm: false,
        base: false,
        sub: false
      },
      limitPhotos: 0,
      subPixel: 50,
      basePixelMax: 2000
    };
  },
  computed: {
    limitSubImg() {
      const rate = Math.max(
        2400 / Math.min(this.baseImg.width, this.baseImg.height),
        1
      );
      const fixH = this.baseImg.height * rate;
      const fixW = this.baseImg.width * rate;
      return Math.ceil((fixH / 50) * (fixW / 50) * 1.1) || 0;
    },
    totalSubImgSize() {
      const size = this.subImgs.reduce((p, c) => p + c.size, 0);
      const units = ["B", "KB", "MB", "GB", "TB"];
      const unitIdx = Math.floor((String(size).length - 1) / 3);
      const unit = units[unitIdx];
      const sizeUnited =
        Math.round((size / Math.pow(1000, unitIdx)) * 100) / 100;
      return sizeUnited + unit;
    }
  },
  watch: {
    loading(val) {
      console.log({ val });
    }
  },
  methods: {
    addBaseImg() {
      window.alert("hoge");
    },
    async genPhotomosaic() {
      this.loading.pm = true;
      const url =
        "https://us-central1-hands-on-campus-apps.cloudfunctions.net/photomosaic";
      const data = {
        url_photos: this.subImgs.map(subImg => subImg.url),
        url_base: this.baseImg.url,
        pixel: this.subPixel
      };

      this.pmUrl = await this.$axios
        .$post(url, data, {
          headers: {
            Authorization: "hogehoge"
          }
        })
        .catch(window.alert);
      this.loading.pm = false;
    },
    uploadFile(key, isBase) {
      return async files => {
        const keyLoading = isBase ? "base" : "sub";
        this.loading[key] = true;
        console.log({ files, len: files.length, loading: this.loading });
        if (!files) return;
        let isSingle = false;
        if (!files.length) {
          files = { length: 1, "0": files };
          isSingle = true;
        }
        for (let i = 0; i < files.length; i++) {
          if (files[i].type.indexOf("image") === -1) continue;
          const reader = new FileReader();
          const image = new Image();
          reader.onload = ({ target: { result } }) => {
            image.src = result;
            image.onload = () => {
              // resize
              const { naturalWidth, naturalHeight } = image;
              console.log({ naturalWidth, naturalHeight });
              let targetW, targetH;
              if (!isBase) {
                targetW = this.subPixel;
                targetH = this.subPixel;
              } else {
                const rate =
                  this.basePixelMax / Math.max(naturalWidth, naturalHeight);
                targetW = naturalWidth * rate;
                targetH = naturalHeight * rate;
              }
              const canvas = document.createElement("canvas");
              const ctx = canvas.getContext("2d");
              canvas.width = targetW;
              canvas.height = targetH;
              ctx.drawImage(image, 0, 0, targetW, targetH);
              result = canvas.toDataURL();
              const img = {
                url: result,
                size: result.length * 2,
                width: targetW,
                height: targetH
              };
              if (!isSingle) this[key].push(img);
              if (isSingle) this[key] = img;
              console.log({ uploaded: img });
            };
          };
          reader.readAsDataURL(files[i]);
        }
        this.loading[keyLoading] = false;
        console.log({ files, len: files.length, loading: this.loading });
      };
    }
  }
};
</script>

<style>
.img-box {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 2vh 0;
}
.img-box-inside {
  display: block;
  height: 0;
  width: 100%;
  padding-bottom: 100%;
  border: 1px dashed;
  background-color: whitesmoke;
  position: relative;
}

.box-text {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

.sub-img {
  margin: 1vmin;
}
.base-img {
  width: 100%;
}
</style>
