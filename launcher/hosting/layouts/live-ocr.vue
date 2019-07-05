<template>
  <v-app>
    <nuxt />
    <div absolute class="inset">
      <v-fab-transition>
        <v-btn
          :color="camera?'red':'info'"
          class="center-btn"
          large
          absolute
          fab
          @click="switchCamera"
        >
          <v-icon dark>{{camera?'mdi-stop':'mdi-camera'}}</v-icon>
        </v-btn>
      </v-fab-transition>
      <v-layout>
        <v-flex xs4 class="layout justify-end">
          <nuxt-link to="/app/live-ocr/record" class="v-btn">
            <div style="display:flex; flex-direction:column;">
              Record
              <v-icon large dark :disabled="pathEnd!=='record'">mdi-clipboard-text</v-icon>
            </div>
          </nuxt-link>
        </v-flex>
        <v-flex xs4 offset-xs4 class="layout justify-start">
          <nuxt-link to="/app/live-ocr/option" class="v-btn">
            <div style="display:flex; flex-direction:column;">
              Option
              <v-icon large dark :disabled="pathEnd!=='option'">mdi-settings</v-icon>
            </div>
          </nuxt-link>
        </v-flex>
      </v-layout>
    </div>
  </v-app>
</template>
<script>
export default {
  data() {
    return {
      btnLarge: true,
      interval: null
    };
  },
  computed: {
    pathEnd() {
      return this.$route.path.split("/").slice(-1)[0];
    },
    camera() {
      return this.$store.state.camera;
    }
  },
  watch: {
    pathEnd(val) {
      if (val !== "camera") this.$store.commit("stopCamera");
    }
  },
  methods: {
    switchCamera() {
      console.log({ camera: this.camera });
      this.$store.commit("switchCamera");
      this.$router.push("/app/live-ocr/camera");
    }
  }
};
</script>


<style>
.inset {
  width: 100%;
  height: 100px;
  text-align: center;
  position: fixed;
  bottom: 0;
  border-radius: 30% 30% 0 0;
  filter: drop-shadow(2px 2px 2px rgba(0, 0, 0, 0.6));

  background-image: -webkit-radial-gradient(
    50% 0%,
    circle closest-corner,
    transparent 0,
    transparent 50px,
    #21252b 51px
  );
}
.center-btn {
  left: 50%;
  top: -5%;
  transform: translateY(-50%) translateX(-50%);
  -webkit-transform: translateY(-50%) translateX(-50%);
  border-radius: 50% !important;
}

.active {
  color: white;
}
</style>
