<template>
  <v-container fluid grid-list-lg class="container">
    <v-layout row wrap justify-center>
      <div id="e1" style="max-width: 500px; margin: auto;">
        <v-flex xs12>
          <h1 class="title">QRCode Reader</h1>
        </v-flex>
      </div>
      <v-flex xs12 justify-center>
        <v-btn fab dark middle color="primary" @click="isCameraOpen=!isCameraOpen">
          <v-icon>camera_enhance</v-icon>
        </v-btn>
        <p></p>

        <p v-show="doneQR&&isCameraOpen" class="suc">QRコードの読み取りに成功しました。しばらくお待ち下さい。</p>
        <v-progress-circular indeterminate color="primary" v-show="doneQR&&isCameraOpen"></v-progress-circular>
      </v-flex>
      <v-flex xs12>
        <video :width="width" :height="height" autoplay/>
      </v-flex>
      <v-flex xs12>{{readed}}</v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import jsQR from "jsQR";

export default {
  data() {
    return {
      srcObject: "",
      width: 300,
      height: 600,
      onLine: true,
      userId: "",
      token: "",
      doneQR: false,
      mediaStream: false,
      isCameraOpen: false,
      timer: null,
      context: null,
      video: null,
      readed: null
    };
  },
  mounted() {
    /* canvas setup (distination of video snapshot) */
    const canv = document.createElement("canvas");
    canv.height = this.height;
    canv.width = this.width;
    this.context = canv.getContext("2d");
    this.video = document.querySelector("video");
  },
  beforeDestroy() {
    this.cameraStop();
  },
  computed: {},
  methods: {
    cameraStart() {
      this.doneQR = false;
      this.isCameraOpen = true;
      navigator.mediaDevices
        .getUserMedia({
          audio: false,
          video: {
            width: this.width,
            height: this.height,
            frameRate: { ideal: 10, max: 10 }
          }
        })
        .then(mediaStream => {
          this.mediaStream = mediaStream;
          this.video.srcObject = this.mediaStream;
          this.readerStart();
        });
    },
    cameraStop() {
      this.isCameraOpen = false;
      this.readerStop();
      this.mediaStream.getVideoTracks().forEach(track => {
        track.stop();
      });
      console.log("camera stopped");
    },
    readerStart() {
      this.readerStop();
      this.timer = setInterval(() => {
        console.log("running .....");
        if (!this.isCameraOpen) return;
        this.context.drawImage(this.video, 0, 0, this.width, this.height);
        const im = this.context.getImageData(0, 0, this.width, this.height);
        const code = jsQR(im.data, im.width, im.height);
        if (code) {
          console.log("Found QR code", code, code.data);
          this.readed = code.data;
          this.doneQR = true;
        }
      }, 500);
    },
    readerStop() {
      if (this.timer) clearInterval(this.timer);
    }
  },
  watch: {
    isCameraOpen(val) {
      if (val) this.cameraStart();

      if (!val) this.cameraStop();
    }
  }
};
</script>

<style>
</style>
