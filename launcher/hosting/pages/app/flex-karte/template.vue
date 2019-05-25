
<template>
  <div id="app">
    <div style="text-align:center">
      <h3>カルテ テンプレート作成</h3>
      <v-btn
        outline
        color="secondary"
        @click="gotoKarte"
      >カルテ一覧
      </v-btn>
      <v-btn
        @click="fixKarte();fixedKarte=true;"
        color="primary"
      >更新</v-btn>
    </div>
    <v-snackbar
      :timeout="2000"
      v-model="fixedKarte"
      top
      right
    >
      カルテテンプレートを更新しました。
    </v-snackbar>

    <v-container>
      <v-layout
        wrap
        row
        justify-center
      >
        <draggable
          v-model="items"
          animation=200
          handle=".handle"
          style="width:100%"
          @remove="removeItem"
        >
          <v-flex
            xs12
            v-for="(item,i) in items"
            :key="i"
          >
            <v-context-menu :items="contextMenus(i)">
              <v-card class="card">
                <v-container>
                  <v-layout wrap>
                    <v-flex
                      xs12
                      class="handle"
                    >
                      <div style="width:60%">
                        <v-select
                          :prepend-icon="templateItems[item.type].icon"
                          :items="Object.keys(templateItems)"
                          label="type"
                          v-model="item.type"
                        />
                      </div>
                      <v-icon>mdi-cursor-move</v-icon>
                    </v-flex>
                    <v-flex xs12>
                      <v-text-field
                        v-model="item.label"
                        label="ラベル名を入れてください"
                      />
                    </v-flex>
                    <v-flex xs12>
                      <div v-if="templateItems[item.type].hasOptions">
                        <v-combobox
                          v-model="item.items"
                          label="選択肢を記入してください"
                          chips
                          multiple
                        >
                          <template v-slot:selection="data">
                            <v-chip
                              :selected="data.selected"
                              close
                              @input="removeOption(item.items,data.item)"
                            >
                              <strong>{{ data.item }}</strong>
                            </v-chip>
                          </template>
                        </v-combobox>
                      </div>
                    </v-flex>
                    <v-expansion-panel :key="i">
                      <v-expansion-panel-content>
                        <template v-slot:header>
                          <v-subheader>プレビューを見る</v-subheader>
                        </template>
                        <v-container fluid>
                          <v-layout
                            wrap
                            width="80%"
                          >
                            <v-flex
                              xs12
                              class="preview-center"
                            >
                              <v-subheader>{{item.label||"{ラベル名}"}}</v-subheader>
                            </v-flex>
                            <v-flex
                              xs12
                              class="preview-center"
                              style="width:80px"
                            >
                              <component
                                :is="templateItems[item.type].tag"
                                :label="templateItems[item.type].label"
                                :items="item.items"
                                :fileChangedCallback="item.fileChanged"
                                outline
                                color="primary"
                              />
                            </v-flex>
                          </v-layout>
                        </v-container>
                      </v-expansion-panel-content>
                    </v-expansion-panel>

                  </v-layout>
                </v-container>
              </v-card>
            </v-context-menu>
          </v-flex>
        </draggable>

        <v-flex xs12>
          <div
            class="create-item"
            @click="createItem"
          >
            <v-icon left>mdi-plus-circle</v-icon>
            Add New Item
          </div>
        </v-flex>

      </v-layout>

    </v-container>

    <v-dialog
      v-model="dialog"
      class="card"
      width="20vw"
    >
      <v-card>
        <v-card-title>
          消去しますか？
        </v-card-title>
        <div style="display:flex;justify-content:flex-end;">
          <v-btn
            color="info"
            @click="removeItem();dialog=false;"
          >
            消去
          </v-btn>
          <v-btn
            @click="dialog=false"
            flat
            color="secondary"
          >キャンセル</v-btn>
        </div>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import draggable from "vuedraggable";
export default {
  components: { draggable },
  asyncData() {
    return {
      items: JSON.parse(localStorage.getItem("karte-template")) || [
        { type: "text", label: "hogehoge" },
        { type: "select", label: "fugafuga", items: ["1"] },
        {
          type: "image",
          label: "image",
          fileChanged: async e => {}
        }
      ]
    };
  },
  data: () => ({
    fixedKarte: false,
    dialog: false,
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
    },
    deletingItemIdx: null
  }),
  mounted() {},
  computed: {
    contextMenus() {
      return i => {
        return [
          {
            title: "delete",
            onClick: () => {
              this.dialog = true;
              this.deletingItemIdx = i;
              //
            }
          }
        ];
      };
    }
  },
  methods: {
    removeItem() {
      this.items.splice(this.deletingItemIdx, 1);
      this.deletingItemIdx = null;
    },
    removeOption(options, item) {
      options.splice(options.indexOf(item), 1);
      options = [...options];
    },
    createItem() {
      this.items.push({
        type: "text",
        label: ""
      });
    },
    fixKarte() {
      console.log({ karte: this.items });
      localStorage.setItem("karte-template", JSON.stringify(this.items));
    },
    gotoKarte() {
      if (
        JSON.stringify(this.items) !== localStorage.getItem("karte-template") &&
        !window.confirm(
          "テンプレートは更新されていないので破棄されます。移動してもよいですか？"
        )
      ) {
        return;
      }
      this.$router.push("karte");
    }
  },
  watch: {}
};
</script>

<style>
.card {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 1vh;
}
.handle {
  display: flex;
  justify-content: space-between;
}
.create-item {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 1vh auto;
  width: 75%;
  border: 1px dashed;
  height: 10vh;
}
.preview {
  width: 80%;
  margin: 0 auto;
}
</style>
