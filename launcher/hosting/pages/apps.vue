
<template>
  <div id="app">
    <div class="title-container">
      <div style="text-align:center">
        <h3 class="title_">Apps</h3>
      </div>

      <div>
        <transition-group
          class="projects"
          name="projects"
        >
          <div
            class="project img-size"
            :key="project._createdAt"
            v-for="project in projects.slice(0,limitProjects)"
          >
            <v-img
              class="project-image"
              :src="project.urlThumbnail"
              :lazy-src="project.urlThumbnail"
              @click="openOriginal(project)"
            />
          </div>
        </transition-group>
        <infinite-loading
          class="infinite-scroll"
          ref="infiniteLoading"
          spinner="spiral"
          @infinite="infiniteHandler"
        >
          <span slot="no-more"></span>
          <span slot="no-results"></span>
        </infinite-loading>
      </div>
    </div>
    <v-dialog
      v-model="dialog"
      fullscreen
    >
      <div style="background-color:rgba(0,0,0,0.8)">
        <v-img
          :src="targetThumbnailUrl"
          :lazy-src="targetThumbnailUrl"
          @click="closeDialog"
          @load="loaded"
          height="100vh"
          contain
        >
          <template>
            <v-layout
              fill-height
              align-center
              justify-center
              ma-0
            >
              <v-progress-circular
                indeterminate
                color="grey lighten-5"
                v-show="loading"
                size="100"
              ></v-progress-circular>
            </v-layout>
          </template>
        </v-img>
      </div>
    </v-dialog>
  </div>
</template>

<script>
import InfiniteLoading from "vue-infinite-loading";
export default {
  components: {
    InfiniteLoading
  },
  async asyncData({ params: { id }, app: { $firestore }, query: { type } }) {},
  mounted() {},
  data() {
    return {
      dialog: false,
      targetImageUrl: "",
      targetThumbnailUrl: "",
      loading: true,
      projects: [  //アプリ作ったらここにデータ追加
        {
          name: "フォトモザイク生成ツールだよ",
          description:
            "ベースとなる画像ファイルと、フォトモザイクのピースとなるサブ画像複数をアップロードして、フォトモザイクを簡単に作れるアプリです",
          urlThumbnail: require("@/static/icon_origin.png"),
          _createdAt: "2019-05-12",
          toApp: "/app/photomosaic",
          toBlog: "https://app-senbonknock.com/hello-world/"
        }
      ],
      limitProjects: 20
    };
  },
  computed: {},
  methods: {
    openOriginal({ urlThumbnail }) {
      this.targetImageUrl = urlThumbnail;
      this.targetThumbnailUrl = urlThumbnail;
      this.dialog = true;
      this.loading = true;
    },
    loaded() {
      this.loading = false;
    },
    closeDialog() {
      this.dialog = false;
    },
    infiniteHandler() {
      setTimeout(() => {
        this.limitProjects += 15;
        if (this.projects.length > this.limitProjects) {
          this.$refs.infiniteLoading.stateChanger.loaded();
        } else {
          this.$refs.infiniteLoading.stateChanger.complete();
        }
      }, 1000);
    }
  }
};
</script>
<style>
html,
body {
  margin: 0;
  font-family: "Dawning of a New Day", cursive !important;
}

.top-bar {
  display: flex;
  flex-direction: row;
  justify-content: left;
  align-items: left;
  margin: 2vh;
}
.top-bar-icon {
  text-align: left;
  margin: 0 0 0 auto;
}

.title-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title_ {
  font-family: "Dawning of a New Day", cursive;
  font-size: 30pt;
  font-weight: normal;
}

.projects {
  margin-top: 25px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.projects-enter {
  transform: scale(0.5) translatey(-80px);
  opacity: 0;
}

.projects-leave-to {
  transform: translatey(30px);
  opacity: 0;
}

.projects-leave-active {
  position: absolute;
  z-index: -1;
}

.infinite-scroll {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100vw;
}

.project {
  transition: all 0.35s ease-in-out;
  box-shadow: 0px 2px 8px lightgrey;
  border-radius: 3px;
  display: flex;
  margin: 1vw;
  flex-direction: column;
  align-items: center;
}

@media screen and (max-width: 499px) {
  .img-size {
    width: 30vw;
    height: 30vw;
  }
}

@media screen and (min-width: 500px) and (max-width: 999px) {
  .img-size {
    width: 30vw;
    height: 30vw;
  }
}

@media screen and (min-width: 1000px) {
  .img-size {
    width: 18vw;
    height: 18vw;
    margin: 0.5vw;
  }
}
.rotating {
  animation: spin 1.5s linear infinite;
}
@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

.project-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-top-left-radius: 3px;
  border-top-right-radius: 3px;
  border-bottom-left-radius: 3px;
  border-bottom-right-radius: 3px;
}
</style>
