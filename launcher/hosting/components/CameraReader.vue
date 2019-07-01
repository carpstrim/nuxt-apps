<template>
  <div
    class="parent"
    :style="`height:`+height+'px'"
  >
    <video
      style="background-color:grey"
      class="pos-ab"
      :width="width"
      :height="height"
      autoplay
    />
    <canvas
      id="canvas"
      class="pos-ab"
      :width="width"
      :height="height"
    ></canvas>
  </div>
</template>

<script>
export default {
  props: {
    value: {
      type: Boolean,
      default: false
    },
    open: {
      type: Boolean,
      default: false
    },
    facingMode: {
      type: String,
      default: "user"
    },
    processor: {
      type: Function,
      default: im => {
        console.log("running...", { im });
      }
    },
    pause: {
      type: Boolean,
      default: false
    },
    width: {
      default: window.innerWidth
    },
    height: {
      default: window.innerHeight
    },
    processInterval: {
      default: 500
    },
    frameRate: {
      default: 10
    }
  }, //width,height,framerate interval imagefunction
  data() {
    return {
      mediaStream: false,
      timer: null,
      context: null,
      video: null,
      rectLocation: []
    };
  },
  computed: {},
  mounted() {
    const rectSize = { w: this.width * 0.8, h: this.height * 0.1 };
    this.rectLocation = [
      (this.width - rectSize.w) / 2,
      (this.height - rectSize.h) / 2,
      rectSize.w,
      rectSize.h
    ];

    /* canvas setup (distination of video snapshot) */
    const canv = document.createElement("canvas");
    canv.height = this.height;
    canv.width = this.width;
    this.context = canv.getContext("2d");
    this.video = document.querySelector("video");

    const ctx = document.getElementById("canvas").getContext("2d");
    ctx.lineWidth = 5;
    ctx.strokeStyle = "rgb(0,0,255)";
    ctx.strokeRect(...this.rectLocation);
  },
  beforeDestroy() {
    this.cameraStop();
  },
  methods: {
    cameraStart() {
      navigator.mediaDevices
        .getUserMedia({
          audio: false,
          video: {
            width: this.width,
            height: this.height,
            frameRate: { ideal: this.frameRate, max: this.frameRate },
            facingMode: this.facingMode
          }
        })
        .then(mediaStream => {
          this.mediaStream = mediaStream;
          this.video.srcObject = this.mediaStream;
          this.readerStart();
        });
    },
    cameraStop() {
      this.readerStop();
      if (!this.mediaStream) return;
      this.mediaStream.getVideoTracks().forEach(track => {
        track.stop();
      });
      console.log("camera stopped");
    },
    readerStart() {
      this.readerStop();
      this.timer = setInterval(() => {
        if (!this.open) return;
        this.context.drawImage(this.video, 0, 0, this.width, this.height);
        const im = this.context.getImageData(...this.rectLocation);

        if (!this.pause) {
          console.log("start!!!");
          this.processor(im);
        } else {
          console.log("paused");
        }
      }, this.processInterval);
    },
    readerStop() {
      if (this.timer) clearInterval(this.timer);
    }
  },
  watch: {
    open(val) {
      if (val) this.cameraStart();
      if (!val) this.cameraStop();
    },
    facingMode(val) {
      this.cameraStop();
      this.cameraStart();
    }
  }
};
</script>

<style>
.parent {
  position: relative;
}
.pos-ab {
  position: absolute;
}
</style>
