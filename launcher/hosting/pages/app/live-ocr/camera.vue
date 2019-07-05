<template>
  <v-layout justify-center>
    <v-flex xs12 v-if="false">
      <v-progress-circular
        v-for="progress in progressAry"
        :key="progress.status"
        :rotate="-90"
        :size="100"
        :width="15"
        :value="progress.progress"
        color="teal"
      >{{ progress.status }}</v-progress-circular>
    </v-flex>
    <div style="width:100vw" class="layout justify-center">
      <camera-reader
        :open="isCameraOpen"
        :facingMode="facingMode"
        :processor="processor"
        :processInterval="500"
        :pause="pause"
        frameRate="10"
      />
    </div>
    <v-fab-transition>
      <v-btn color="secondary" dark fab round fixed top right @click="switchCamera">
        <v-icon>mdi-camera-retake</v-icon>
      </v-btn>
    </v-fab-transition>
    <v-snackbar v-model="snack" top>{{readedText}}</v-snackbar>
  </v-layout>
</template>

<script>
import Tesseract from "tesseract.js";

export default {
  layout: "live-ocr",
  data() {
    return {
      srcObject: "",
      bottomNav: "",
      readed: [],
      readedText: "",
      snack: false,
      pause: false,
      facingMode: "environment",
      progresses: {
        "initializing api": 0,
        "recognizing text": 0
      }
    };
  },
  computed: {
    progressAry() {
      return Object.keys(this.progresses).map(status => ({
        status,
        progress: this.progresses[status]
      }));
    },
    isCameraOpen() {
      return this.$store.state.camera;
    }
  },
  mounted() {
    /*
    navigator.mediaDevices.enumerateDevices().then(devices => {
      console.log({ devices });
    });
    */
  },
  methods: {
    processor(im) {
      const code = null;
      this.pause = true;
      Tesseract.recognize(im)
        .progress(({ status, progress }) => {
          this.progresses[status] = progress * 100;
        })
        .then(result => {
          for (let status in this.progresses) {
            this.progresses[status] = 0;
          }
          console.log("result", result);
          result.text = result.text.replace(/\W|[a-z]|O/g, "");
          result.text = result.text
            .split(" ")
            .filter(str => str.length === 12)
            .reduce((p, c) => p + c, "");
          if (result.text.length === 12) {
            this.readedText = result.text;
            this.snack = true;
          }
          result.text = ` [ ${result.text} ] ${result.text.length} words`;
          this.readed.unshift(`${Date.now()}:${result.text}`);
          this.pause = false;
        });
    },
    switchCamera() {
      this.facingMode = this.facingMode === "user" ? "environment" : "user";
    }
  }
};
</script>
