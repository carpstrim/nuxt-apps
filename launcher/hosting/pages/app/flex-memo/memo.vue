
<template>
  <div
    id="app"
    style="text-align:center"
  >
    <h3>マイドキュメント</h3>
    <v-btn
      outline
      color="secondary"
      to="template"
    >テンプレート作成
    </v-btn>
    <v-btn
      color="info"
      @click="createKarte();dialog=true"
    >
      新規ドキュメント
    </v-btn>

    <!--/* Karte List  */ -->
    <v-container>
      <v-layout
        row
        wrap
      >
        <v-flex
          xs6
          sm4
          md3
          v-for="(k,i) in karte"
          :key="i"
          class="pa-1"
        >
          <v-context-menu :items="contextMenus(i)">
            <v-card @click="targetIdx=i;dialog=true">
              <v-list
                v-for="(item,j) in items.slice(0,5)"
                :key="item.label"
                class="pa-0"
              >
                <v-img
                  v-if="item.type==='image'"
                  :src="k[item.label]"
                  aspect-ratio="1"
                />
                <v-list-tile
                  v-else
                  style="height:40px"
                >
                  <v-list-tile-content>
                    <component :is="j===0?'v-list-tile-title':'v-list-tile-sub-title'">
                      <span
                        v-if="typeof(k[item.label])==='object'"
                        class="text-xs-left"
                      >
                        {{Object.keys(k[item.label]).map(textKey=>k[item.label][textKey]).reduce((p,c)=>p+" "+c) }}
                      </span>
                      <span v-else> {{filter(k,item)}}</span>
                    </component>
                  </v-list-tile-content>
                </v-list-tile>
              </v-list>
            </v-card>
          </v-context-menu>
        </v-flex>
      </v-layout>
    </v-container>
    <!--/* DIALOG  */ -->
    <v-dialog
      v-model="dialog"
      max-width="700px"
    >
      <v-card v-if="dialog">
        <v-container>
          <v-layout
            wrap
            row
          >
            <v-flex
              xs12
              v-for="(item,i) in items"
              :key="i"
            >
              <v-divider></v-divider>
              <v-subheader>{{item.label}}</v-subheader>
              <component
                style="margin:0 auto;"
                :is="item.tag"
                :label="item.label"
                v-model="karte[targetIdx][item.label]"
                :items="item.items"
                :fileChangedCallback="item.fileChanged"
                outline
                color="primary"
                :birthday="item.birthday"
              />
            </v-flex>
          </v-layout>
          <v-divider></v-divider>
          <v-layout justify-end>
            <v-btn
              color="info"
              outline
              @click="dialog=false"
            >保存</v-btn>
          </v-layout>
        </v-container>
      </v-card>
    </v-dialog>

    <!-- delete snackbar -->
    <v-snackbar
      :timeout="0"
      v-model="snackbar"
      bottom
      multi-line
    >
      消去しました。
      <v-layout justify-end>
        <div>
          <v-btn
            color="warning"
            @click="restoreKarte();snackbar=false"
          >
            元に戻す
          </v-btn>
          <v-btn
            color="white"
            @click="snackbar=false"
            flat
          >
            閉じる
          </v-btn>
        </div>
      </v-layout>
    </v-snackbar>

  </div>
</template>

<script>
const _ = require("lodash");

export default {
  asyncData({ redirect }) {
    const items = JSON.parse(localStorage.getItem("karte-template"));
    if (!items) {
      redirect("/app/flex-karte/template");
      return;
    }
    let karte = JSON.parse(localStorage.getItem("karte")) || [{}];
    const labels = items.map(item => item.label);
    karte = karte.map(k => _.pick(k, labels));
    return { items, karte };
  },
  layout: "plain",
  data: () => ({
    dialog: false,
    targetIdx: 0,
    karteDeleted: {},
    karteDeletedIdx: null,
    snackbar: false
  }),
  mounted() {
    this.items = this.items.map(item => {
      if (item.type !== "image") return item;
      return {
        ...item,
        fileChanged: async e => {
          this.karte[this.targetIdx][item.label] = e;
        }
      };
    });
    console.table(this.items);
    console.table(this.karte);
  },
  computed: {
    templateTypes() {
      let result = {};
      for (let { label, type } of this.items) {
        result[label] = type;
      }
      return result;
    }
  },
  methods: {
    createKarte() {
      this.karte.unshift({});
      this.targetIdx = 0;
    },
    filter(karte, item) {
      const data = karte[item.label];
      if (item.type === "birthday") {
        const age = Math.floor(
          (Date.now() - new Date(data).getTime()) / 1000 / 60 / 60 / 24 / 365
        );
        if (!data) return "- (-)歳";
        return `${data} (${age})歳`;
      }
      return data || "-";
    },
    contextMenus(i) {
      return [
        {
          title: "消去",
          onClick: () => {
            this.karteDeleted = this.karte.splice(i, 1);
            this.karteDeletedIdx = i;
            this.snackbar = true;
          }
        }
      ];
    },
    restoreKarte() {
      const foot = this.karte.splice(this.karteDeletedIdx);
      this.karte = [...this.karte, ...this.karteDeleted, ...foot];
    }
  },
  watch: {
    karte(val) {
      saveKarte(val);
    },
    dialog(val) {
      if (!val) {
        this.karte = this.karte.filter(karte => {
          return Object.keys(karte).some(label => karte[label]);
        });
        saveKarte(this.karte);
      }
    }
  }
};
function saveKarte(karte) {
  localStorage.setItem("karte", JSON.stringify(karte));
  console.log("karte saved");
  console.table(karte);
}
</script>

<style>
</style>
