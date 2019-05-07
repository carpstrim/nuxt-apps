
<template>
  <div id="app">
    <div style="text-align:center">
      <h3>Photo Mosaic</h3>
    </div>
    <v-container>
      <v-layout wrap>
        <v-flex xs12 sm6 class="img-box">
          <div class="img-box-inside">
            <div class="box-text" @click="addBaseImg">
              <v-icon>add</v-icon>1.Click to add base image
            </div>
          </div>
        </v-flex>
        <v-flex xs12 sm6 class="img-box">
          <div class="img-box-inside">
            <div class="box-text" @click="addBaseImg">
              <v-btn color="info">3.Generate Photomosaic</v-btn>
            </div>
          </div>
        </v-flex>
        <v-flex xs12 class="img-box">
          <upload-btn
            :fileChangedCallback="uploadFile"
            color="info"
            title="2.Upload Sub-Image"
            multiple
          ></upload-btn>
        </v-flex>
        <v-flex xs12 class="img-box">{{dataUrls.length}}枚 (最大 {{limitSubImg}}枚まで可能)</v-flex>
      </v-layout>
      <v-layout wrap>
        <v-flex xs2 v-for="(dataUrl,i) in dataUrls" :key="i">
          <v-card class="sub-img">
            <v-img :src="dataUrl" aspect-ratio="1"/>
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
      dataUrls: []
    };
  },
  computed: {
    limitSubImg() {
      return this.dataUrls.length + 10;
    }
  },
  methods: {
    addBaseImg() {
      window.alert("hoge");
    },
    async uploadFile(files) {
      console.log({ files });
      for (let i = 0; i < files.length; i++) {
        console.log({ file: files[i] });
        const reader = new FileReader();
        reader.onload = e => {
          this.dataUrls.push(e.target.result);
        };
        reader.readAsDataURL(files[i]);
      }
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
</style>
