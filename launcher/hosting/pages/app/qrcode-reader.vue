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
          <h1 class="title">QRCode Reader</h1>
        </v-flex>
      </div>
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
        <p></p>

        <p
          v-show="doneQR&&isCameraOpen"
          class="suc"
        >QRコードの読み取りに成功しました。しばらくお待ち下さい。</p>
        <v-progress-circular
          indeterminate
          color="primary"
          v-show="doneQR&&isCameraOpen"
        ></v-progress-circular>
      </v-flex>
      <v-flex xs12>
        <camera-reader
          :open="isCameraOpen"
          width=300
          height=500
          :processor="processor"
          frameRate="10"
        ></camera-reader>
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
      doneQR: false,
      isCameraOpen: false,
      readed: null
    };
  },
  methods: {
    processor(im) {
      const code = jsQR(im.data, im.width, im.height);
      if (code) {
        console.log("Found QR code", code, code.data);
        this.readed = code.data;
        this.doneQR = true;
      }
    }
  }
};
</script>

<style>
</style>
