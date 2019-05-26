
<template>
  <div>
    <div style="text-align:center">
      <h3 class="title_">Apps</h3>
    </div>

    <v-container class="pa-2">
      <v-layout
        row
        wrap
      >
        <v-flex
          xs4
          sm3
          :key="project._createdAt"
          v-for="project in projects.slice(0,limitProjects)"
          class="pa-2"
        >
          <v-card>
            <v-img
              :src="
              project.urlThumbnail"
              :lazy-src="project.urlThumbnail"
              @click="openOriginal(project)"
              aspect-ratio="1"
            />
          </v-card>
        </v-flex>
        <infinite-loading
          class="infinite-scroll"
          ref="infiniteLoading"
          spinner="spiral"
          @infinite="infiniteHandler"
        >
          <span slot="no-more"></span>
          <span slot="no-results"></span>
        </infinite-loading>
      </v-layout>
    </v-container>
    <v-dialog
      v-model="dialog"
      scrollable
    >
      <div class="dialog--inside">
        <div class="app--name">{{targetProject.name}}</div>
        <br>
        <div class="app--description">{{targetProject.description}}</div>
        <v-img
          :src="targetProject.urlThumbnail"
          aspect-ratio="1"
          width="30vmax"
          class="mt-5 mb-2"
        />
        <v-btn
          color="info"
          v-if="!isHttp(targetProject.toApp)"
          :to="targetProject.toApp"
          round
        >アプリページ</v-btn>
        <v-btn
          color="success"
          v-if="isHttp(targetProject.toApp)"
          :href="targetProject.toApp"
          target="_blank"
          round
        >LINEアプリ</v-btn>
        <v-btn
          color="white"
          v-if="targetProject.toBlog"
          :href="targetProject.toBlog"
          target="_blank"
          outline
        >説明ブログ<v-icon
            small
            right
          >mdi-launch</v-icon>
        </v-btn>
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
      projects: [
        //アプリ作ったらここにデータ追加
        {
          name: "フォトモザイクジェネレーター",
          description:
            "ベースとなる画像ファイルと、フォトモザイクのピースとなるサブ画像複数をアップロードして、フォトモザイクを簡単に作れるアプリです",
          urlThumbnail: require("@/static/thumb/photomosaic.jpg"),
          _createdAt: "2019-05-12",
          toApp: "/app/photomosaic",
          toBlog: "https://app-senbonknock.com/phomosaic/"
        },
        {
          name: "ドット画像メーカー",
          description: "画像ファイルをドット絵っぽく低画質に落とすアプリです",
          urlThumbnail: require("@/static/thumb/dotmaker.jpg"),
          _createdAt: "2019-05-21",
          toApp: "/app/dotmaker",
          toBlog: "https://app-senbonknock.com/dotmaker/"
        },
        {
          name: "100分の1じゃんけん",
          description:
            "100回に１回しか勝てないじゃんけんに挑戦できるネタアプリです。",
          urlThumbnail: require("@/static/thumb/1percentjanken.jpg"),
          _createdAt: "2019-05-20",
          toApp: "https://line.me/R/ti/p/%40ueb6734r",
          toBlog: "https://app-senbonknock.com/1percentjanken/"
        },

        {
          name: "おしゃれ画像コレクター",
          description:
            "unsplash.comからおしゃれな画像を手軽に検索＆画像URLのコピーができるアプリです",
          urlThumbnail: require("@/static/thumb/imagecollector.jpg"),
          _createdAt: "2019-05-25",
          toApp: "/app/imagecollector",
          toBlog: "https://app-senbonknock.com/imagecollector/"
        },
        {
          name: "匿名型画像投稿アプリ memorus",
          description:
            "LINE+Googleフォトを組み合わせたようなサービス。結婚式やイベントなどで参加者みんなとSNSで繋がったりする必要なく、手軽に写真を共有しあるLINEアプリ",
          urlThumbnail: require("@/static/thumb/memorus-thumb.jpg"),
          _createdAt: "2019-05-26",
          toApp: "https://line.me/R/ti/p/%40lhl7924a",
          toBlog: "https://app-senbonknock.com/memorus/"
        }
      ],
      limitProjects: 20,
      targetProject: {}
    };
  },
  computed: {},
  methods: {
    openOriginal(project) {
      this.targetProject = project;
      this.dialog = true;
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
    },
    isHttp(text) {
      if (!text) return;
      return text.indexOf("http") !== -1;
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

.infinite-scroll {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100vw;
}

.dialog--inside {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: white;
  background-color: rgba(0, 0, 0, 0.6);
  width: 100%;
  height: 100%;
  padding: 5vh 5vh;
}
.app--name {
  font-size: 3vh;
}
.app--description {
  font-size: 2vh;
  text-align: center;
  width: 60vw;
}
</style>
