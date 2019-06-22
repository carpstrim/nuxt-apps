<template>
  <div>
    <v-btn
      fab
      dark
      middle
      color="primary"
      @click="open=!open"
    >
      <v-icon>camera_enhance</v-icon>
    </v-btn>
    {{readed}}
    <camera-reader
      :open="open"
      :processor="processor"
      frameRate="5"
    ></camera-reader>
  </div>
</template>

<script>
import jsQR from "jsQR";

export default {
  data() {
    return {
      open: false,
      readed: null
    };
  },
  methods: {
    processor(im) {
      const code = jsQR(im.data, im.width, im.height);
      if (code) {
        console.log("Found QR code", code, code.data);
        this.readed = code.data;
      }
    }
  }
};
</script>
