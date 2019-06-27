<template>
  <v-container
    fluid
    grid-list-lg
    class="container"
  >
    <v-layout
      row
      wrap
      justify-center
    >
      <div
        id="e1"
        style="max-width: 500px; margin: auto;"
      >
        <v-flex xs12>
          <h1 class="title">Live OCR</h1>
        </v-flex>
      </div>
      <v-flex xs12>
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
      <v-flex
        xs12
        justify-center
      >
        <v-btn
          fab
          dark
          middle
          color="primary"
          @click="isCameraOpen=!isCameraOpen"
        >
          <v-icon>camera_enhance</v-icon>
        </v-btn>
        <v-btn
          fab
          dark
          middle
          color="secondary"
          v-show="isCameraOpen"
          @click="switchCamera"
        >
          <v-icon>mdi-camera-party-mode</v-icon>
        </v-btn>
      </v-flex>
      <v-flex xs12>
        <camera-reader
          :open="isCameraOpen"
          :facingMode="facingMode"
          width="300"
          height="500"
          :processor="processor"
          :processInterval="500"
          :pause="pause"
          frameRate="10"
        ></camera-reader>
      </v-flex>
      <v-flex xs12>
        readed
        <p
          v-for="text in readed"
          :key="text"
        >{{text}}</p>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Tesseract from "tesseract.js";

export default {
  data() {
    return {
      srcObject: "",
      isCameraOpen: false,
      readed: [],
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

<style>
</style>
