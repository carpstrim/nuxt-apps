
<template>
  <div id="app">
    <div style="text-align:center">
      <h3>画像コレクター</h3>
    </div>
    <v-container>
      <v-layout wrap row justify-center>
        <v-flex xs12>
          <v-subheader>Search</v-subheader>
        </v-flex>
        <v-flex xs10 sm11>
          <v-text-field
            label="type keyword"
            placeholder="ex. nature, flower"
            outline
            color="primary"
            v-model.lazy="keyword"
            @keydown.enter="search"
          ></v-text-field>
        </v-flex>
        <v-flex
          xs2
          sm1
          style="display:flex;align-items:start;justify-content:center;padding-left:1vw;"
        >
          <v-btn color="info" icon round :loading="loading" @click="search">
            <v-icon>search</v-icon>
          </v-btn>
        </v-flex>
        <v-flex xs12>
          <v-progress-linear v-show="loading" indeterminate />
        </v-flex>

        <v-layout wrap row justify-center>
          <v-flex
            xs4
            sm3
            md2
            v-for="(url,i) in urlList"
            :key="url+i"
            style="display:flex;align-items:start;justify-content:center;  padding: 3px;"
          >
            <div class="thumbs">
              <v-card class="card">
                <img :id="url" :src="url" @click="getDataUrl(url)" />
              </v-card>
            </div>
          </v-flex>
        </v-layout>
      </v-layout>
    </v-container>

    <v-snackbar v-model="snackbar" multi-line :timeout="3000" top>
      画像アドレスをコピーしました
      <v-btn color="warning" flat @click="snackbar = false">Close</v-btn>
    </v-snackbar>
  </div>
</template>

<script>
export default {
  data: () => ({
    keyword: "",
    query: null,
    timeoutId: null,
    loading: false,
    clipboard: null,
    snackbar: false,
    urls: []
  }),
  mounted() {
    if (this.clipboard) return;
    window.addEventListener("copy", e => {
      this.clipboard = e.clipboardData;
    });
  },
  computed: {
    urlList: {
      get() {
        return this.urls.filter((url, i, U) => U.indexOf(url) === i);
      },
      set(val) {
        if (val.length === 0) this.urls = [];
      }
    }
  },
  methods: {
    search() {
      this.query = this.keyword;
    },
    getDataUrl(url) {
      let clipboard = document.createElement(`textarea`);
      clipboard.value = url;
      document.body.appendChild(clipboard);
      clipboard.select();
      document.execCommand("copy");
      clipboard.parentElement.removeChild(clipboard);
      this.snackbar = true;
    }
  },
  watch: {
    keyword(val) {
      clearTimeout(this.timeoutId);
      if (this.query === val) return;
      this.loading = true;
      if (!val) {
        this.query = "";
        this.loading = false;
      } else {
        this.timeoutId = setTimeout(() => {
          this.query = val;
          this.loading = false;
        }, 1000);
      }
    },
    async query(val) {
      this.urlList = [];
      this.urls = [];
      if (val) {
        const endpoint = "https://source.unsplash.com/featured?";
        [...Array(30)].map(async (_, i) => {
          const postUrl = `${endpoint}${this.query},${Math.random()}${i}`;
          const response = await this.$axios.get(postUrl);
          this.urls.push(response.request.responseURL);
        });
      }
    }
  }
};
</script>

<style>
.thumbs {
  width: 100%;
  height: 100%;
  position: relative;
}
.thumbs::before {
  content: "";
  display: block;
  padding-top: 100%;
}
.thumbs .card {
  display: block;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
}
.thumbs img {
  width: 100%;
  height: 100%;
  line-height: 0;
  position: absolute;
  bottom: 0;
  object-fit: cover;
}
</style>
