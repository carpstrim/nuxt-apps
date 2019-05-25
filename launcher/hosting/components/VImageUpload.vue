<template>
  <div :style="`width:${width}`">
    <v-layout
      style="width:100%"
      wrap
    >
      <v-flex xs12>
        <div
          class="thumbs mesh"
          :style="`width:calc(${width});height:calc(${width});`"
        >
          <v-img
            v-show="thumbUrl"
            :src=thumbUrl
            aspect-ratio="1"
            style="border:1px solid;"
          />
          <v-icon
            v-show="!thumbUrl"
            large
          >image</v-icon>
        </div>
      </v-flex>
      <v-flex xs12>
        <div class="thumbs">
          <upload-btn
            :fileChangedCallback="fileChanged"
            color="primary"
          > Upload Image</upload-btn>
        </div>
      </v-flex>
    </v-layout>
  </div>

</template>

<script>
export default {
  props: {
    width: {
      type: String,
      default: "200px"
    },
    fileChangedCallback: {
      default: undefined,
      type: Function
    }
  },
  data: () => ({
    thumbUrl: ""
  }),
  methods: {
    async fileChanged(file) {
      if (!file) return;
      const reader = new FileReader();
      const image = new Image();
      reader.onload = ({ target: { result } }) => {
        image.src = result;
        image.onload = () => {
          // resize
          const { naturalWidth, naturalHeight } = image;
          let targetW, targetH;
          const rate = 300 / Math.max(naturalWidth, naturalHeight);
          targetW = naturalWidth * rate;
          targetH = naturalHeight * rate;
          const canvas = document.createElement("canvas");
          const ctx = canvas.getContext("2d");
          canvas.width = targetW;
          canvas.height = targetH;
          ctx.drawImage(image, 0, 0, targetW, targetH);
          result = canvas.toDataURL();
          this.thumbUrl = result;
          this.fileChangedCallback(result);
        };
      };
      reader.readAsDataURL(file);
    }
  }
};
</script>

<style>
.thumbs {
  display: flex;
  justify-content: center;
  align-items: center;
}
.mesh {
  background-color: ghostwhite;
}
.thumbs img {
  width: 100%;
  height: 100%;
  line-height: 0;
  position: absolute;
  bottom: 0;
  object-fit: cover;
}
.upload-btn {
}
.upload-btn input[type="file"] {
  position: absolute;
  height: 0.1px;
  width: 0.1px;
  overflow: hidden;
  opacity: 0;
  z-index: -1;
}
.upload-btn-hover {
  cursor: pointer;
}
</style>
