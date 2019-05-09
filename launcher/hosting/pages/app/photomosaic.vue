
<template>
  <div id="app">
    <div style="text-align:center">
      <h3>Photo Mosaic</h3>
    </div>
    <v-container>
      <v-layout wrap>
        <v-flex xs12 sm6 class="img-box">
          <div class="img-box-inside">
            <div class="box-text" v-if="!baseUrl">
              <upload-btn
                :fileChangedCallback="uploadFile('baseUrl','single')"
                color="primary"
                title="1.Upload Base-Image"
              ></upload-btn>
            </div>
            <v-img
              :src="baseUrl"
              v-else
              @click.right="baseUrl=``"
              class="base-img"
              aspect-ratio="1"
            ></v-img>
          </div>
        </v-flex>
        <v-flex xs12 sm6 class="img-box">
          <div class="img-box-inside">
            <div class="box-text">
              <v-btn
                color="info"
                :disabled="!subUrls.length>0 || !baseUrl"
                @click="genPhotomosaic"
              >3.Generate Photomosaic</v-btn>
            </div>
          </div>
        </v-flex>
        <v-flex xs12 class="img-box">
          <upload-btn
            :fileChangedCallback="uploadFile('subUrls','multi')"
            color="info"
            title="2.Upload Sub-Image"
            multiple
          ></upload-btn>
        </v-flex>
        <v-flex xs12 class="img-box">{{subUrls.length}}枚 (最大 {{limitSubImg}}枚まで可能)</v-flex>
      </v-layout>
      <v-layout wrap>
        <v-flex xs2 v-for="(subUrl,i) in subUrls" :key="i">
          <v-card class="sub-img">
            <v-img :src="subUrl" aspect-ratio="1" @click.right="subUrls.splice(i,1)"/>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      subUrls: [],
      baseUrl: "",
      pmUrl: ""
    };
  },
  computed: {
    limitSubImg() {
      return this.subUrls.length + 10;
    }
  },
  methods: {
    addBaseImg() {
      window.alert("hoge");
    },
    async genPhotomosaic() {
      const url =
        "https://us-central1-hands-on-campus-apps.cloudfunctions.net/photomosaic";
      const data = {
        url_photos: this.subUrls,
        url_base: this.baseUrl
      };

      this.pmUrl = await this.$axios.post(url, data, {
        headers: {
          Authorization: "hogehoge"
        }
      });
      console.log(this.pmUrl)
    },
    uploadFile(key) {
      return async files => {
        console.log({ files, len: files.length });
        if (!files) return;
        let isSingle = false;
        if (!files.length) {
          files = { length: 1, "0": files };
          isSingle = true;
        }
        for (let i = 0; i < files.length; i++) {
          if (files[i].type.indexOf("image") === -1) continue;
          const reader = new FileReader();
          reader.onload = e => {
            if (!isSingle) this[key].push(e.target.result);
            if (isSingle) this[key] = e.target.result;
          };
          reader.readAsDataURL(files[i]);
        }
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
