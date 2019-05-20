
<template>
  <div id="app">
    <div style="text-align:center">
      <h3>ドット画像メーカー</h3>
    </div>
    <v-container>
      <v-layout wrap>
        <v-subheader>
          <h4>色数</h4>
        </v-subheader>
        <v-flex xs12>
          <div class="pannel">
            <v-slider
              v-model="ucolorIdx"
              :tick-labels="ucolorLabels"
              ticks="always"
              :max="ucolorLabels.length-1"
              thumb-label="always"
              always-dirty
              tick-size="3"
            >
              <template v-slot:thumb-label="props">
                <span>{{ ucolorLabels[props.value] }}</span>
              </template>
            </v-slider>
          </div>
        </v-flex>
        <v-flex xs12 sm6 class="img-box">
          <div class="img-box-inside">
            <div class="box-text" v-if="!baseImg">
              <upload-btn :fileChangedCallback="uploadFile()" color="info" title="1.ベース画像"></upload-btn>
            </div>
            <v-img :src="baseImg" v-else @dblclick="baseImg=''" class="base-img" aspect-ratio="1"></v-img>
          </div>
        </v-flex>
        <v-flex xs12 sm6 class="img-box">
          <div class="img-box-inside">
            <div class="box-text" v-if="!dotUrl">
              <v-btn
                color="primary"
                :disabled="!baseImg"
                @click="genDotImg"
                :loading="loading"
              >2.ドット画像生成</v-btn>
            </div>
            <v-img :src="dotUrl" v-else @dblclick="dotUrl=``" class="base-img" aspect-ratio="1"></v-img>
          </div>
        </v-flex>
      </v-layout>
    </v-container>

    <div class="text-xs-center">
      <v-dialog v-model="loading" persistent width="80vw">
        <v-card color="primary" dark>
          <v-card-text>
            <p>処理中...</p>
            <p>{{loadingText}}</p>
            <v-progress-linear indeterminate color="white" class="mb-0"></v-progress-linear>
          </v-card-text>
        </v-card>
      </v-dialog>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      baseImg: "",
      dotUrl: "",
      loading: false,
      ucolorIdx: 2,
      ucolorLabels: ["2", "4", "8", "16", "32", "64"],
      basePixelMax: 500,
      loadingText: "画像アップロード中..."
    };
  },
  computed: {
    ucolors() {
      return this.ucolorLabels[this.ucolorIdx] | 0;
    }
  },
  watch: {
    loading(val) {
      this.loadingText = "画像アップロード中...";
      if (val) {
        const vm = this;
        setTimeout(() => {
          vm.loadingText = "画像計算中.処理には40秒ほどかかります...";
        }, 5000);
      }
    }
  },
  methods: {
    addBaseImg() {
      window.alert("hoge");
    },
    async genDotImg() {
      this.loading = true;
      const url =
        "https://us-central1-hands-on-campus-apps.cloudfunctions.net/dotmaker";
      const data = {
        url_img: this.baseImg,
        unique_colors: this.ucolors
      };

      this.dotUrl = await this.$axios
        .$post(url, data, {
          headers: {
            Authorization: "hogehoge"
          }
        })
        .catch(window.alert);
      this.loading = false;
    },
    uploadFile() {
      return async file => {
        this.loading = true;
        if (!file) {
          this.loading = false;
          return;
        }

        const reader = new FileReader();
        reader.onload = ({ target: { result } }) => {
          const image = new Image();
          image.src = result;
          image.onload = () => {
            // resize
            const { naturalWidth, naturalHeight } = image;
            console.log({ naturalWidth, naturalHeight });
            let targetW, targetH;
            const rate =
              this.basePixelMax / Math.max(naturalWidth, naturalHeight);
            targetW = naturalWidth * rate;
            targetH = naturalHeight * rate;
            const canvas = document.createElement("canvas");
            const ctx = canvas.getContext("2d");
            canvas.width = targetW;
            canvas.height = targetH;
            ctx.drawImage(image, 0, 0, targetW, targetH);
            result = canvas.toDataURL();
            this.baseImg = result;
            console.log({ uploaded: result });
            this.loading = false;
          };
        };
        reader.readAsDataURL(file);
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
}
.hmargin {
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

.base-img {
  width: 100%;
}

.pannel {
  width: 85vw;
  margin: 5vw auto;
}
</style>
