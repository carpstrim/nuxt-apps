<template>
  <v-app>
    <nuxt />
    <div
      absolute
      class="inset"
    >
      <nuxt-link to="/app/live-ocr/camera">
        <v-fab-transition>
          <v-btn
            :color="cameraColor"
            class="center-btn"
            large
            absolute
            fab
          >
            <v-icon dark>{{pathEnd==='camera'?'mdi-stop':'mdi-camera'}}</v-icon>
          </v-btn>
        </v-fab-transition>
      </nuxt-link>
      <v-layout>
        <v-flex
          xs4
          class="layout justify-end"
        >
          <nuxt-link
            to="/app/live-ocr/record"
            class="v-btn"
          >
            <div style="display:flex; flex-direction:column;">
              Record
              <v-icon
                large
                dark
                :disabled="pathEnd!=='record'"
              >mdi-clipboard-text</v-icon>
            </div>
          </nuxt-link>

        </v-flex>
        <v-flex
          xs4
          offset-xs4
          class="layout justify-start"
        >
          <nuxt-link
            to="/app/live-ocr/option"
            class="v-btn"
          >
            <div style="display:flex; flex-direction:column;">
              Option
              <v-icon
                large
                dark
                :disabled="pathEnd!=='option'"
              >mdi-settings</v-icon>
            </div>
          </nuxt-link>
        </v-flex>
      </v-layout>
    </div>
  </v-app>
</template>
<script>
const reds = {
  "$red-100": "#ffcdd2",
  "$red-200": "#ef9a9a",
  "$red-300": "#e57373",
  "$red-400": "#ef5350",
  "$red-500": "#f44336",
  "$red-600": "#e53935",
  "$red-700": "#d32f2f",
  "$red-800": "#c62828",
  "$red-900": "#b71c1c"
};
export default {
  data() {
    return {
      btnLarge: true,
      interval: null,
      cameraColor: this.pathEnd === "camera" ? "red" : "info",
      red: 100
    };
  },
  computed: {
    pathEnd() {
      return this.$route.path.split("/").slice(-1)[0];
    }
  },
  watch: {
    pathEnd(val) {
      if (val === "camera") {
        this.interval = setInterval(() => {
          this.red += 100;
          if (this.red >= 500) this.red = 300;
          this.cameraColor = reds[`$red-${this.red}`];
          console.log("camera running...");
        }, 300);
      } else {
        this.cameraColor = "info";
        clearInterval(this.interval);
      }
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
