
<template>
  <div
    id="app"
    style="text-align:center"
  >
    <h3>カルテ</h3>
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
      新規カルテ
    </v-btn>

    <!--/* Karte List  */ -->
    <v-container>
      <v-layout
        row
        wrap
      >
        <v-flex
          xs12
          sm6
          v-for="(k,i) in karte"
          :key="i"
          class="pa-1"
        >
          <v-card
            @click="targetIdx=i;dialog=true"
            raised
          >
            <v-layout
              justify-space-between
              row
              align-center
              style="height:10vmax"
              class="pa-4"
            >
              <v-avatar
                size="8vmax"
                class="elevation-6"
              >
                <img :src="k[summaryLabel.img]" />
              </v-avatar>
              <h4>{{k[summaryLabel.text]}}</h4>
              <h4>{{k[summaryLabel.select]}}</h4>
            </v-layout>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
    <!--/* DIALOG  */ -->
    <v-dialog
      v-model="dialog"
      max-width="700px"
    >
      <v-card>
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
              <component
                style="margin:0 auto;"
                :is="templateItems[item.type].tag"
                :label="item.label"
                v-model="karte[targetIdx][item.label]"
                :items="item.items"
                :fileChangedCallback="item.fileChanged"
                outline
                color="primary"
              />
            </v-flex>
          </v-layout>
          <v-divider></v-divider>
          <v-layout justify-end>
            <v-btn
              color="info"
              outline
              @click="dialog=false"
            >閉じる</v-btn>
          </v-layout>
        </v-container>
      </v-card>
    </v-dialog>

  </div>
</template>

<script>
export default {
  asyncData({ redirect }) {
    const items = JSON.parse(localStorage.getItem("karte-template"));
    if (!items) {
      redirect("/app/flex-karte/template");
      return;
    }
    let karte = JSON.parse(localStorage.getItem("karte")) || [{}];
    const idx = items.map((item, i) => ({ ...item, idx: i }));
    const getKarteSummary = type => {
      return idx.filter(i => i.type === type).map(item => item.label);
    };
    return {
      items,
      karte,
      summaryLabel: {
        img: getKarteSummary("image")[0],
        select: getKarteSummary("select")[0],
        text: getKarteSummary("text")[0]
      }
    };
  },
  data: () => ({
    dialog: false,
    targetIdx: 0,
    templateItems: {
      text: {
        tag: "v-text-field",
        label: "text field",
        hasOptions: false,
        icon: "mdi-format-text"
      },
      select: {
        tag: "v-select",
        label: "select",
        hasOptions: true,
        icon: "mdi-checkbox-multiple-marked-outline"
      },
      textArea: {
        tag: "v-textarea",
        label: "text area",
        hasOptions: false,
        icon: "mdi-format-align-justify"
      },
      image: {
        tag: "v-image-upload",
        label: "image upload",
        hasOptions: false,
        icon: "mdi-image"
      }
    }
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
  computed: {},
  methods: {
    createKarte() {
      this.karte.unshift({});
      this.targetIdx = 0;
    }
  },
  watch: {
    dialog(val) {
      if (!val) {
        localStorage.setItem("karte", JSON.stringify(this.karte));
        console.log("karte saved");
        console.table(this.karte);
      }
    }
  }
};
</script>

<style>
</style>
