<template>
  <div>
    <v-dialog v-model="dialog" max-width="500px">
      <template v-slot:activator="{ on }">
        <div
          class="justify-space-between align-end layout"
          :style="`width:${width}`"
          style="margin: 0 auto"
        >
          <h4>{{title}}</h4>
          <v-btn
            color="primary"
            dark
            class="mb-2"
            v-on="on"
            round
            flat
            outline
            small
            v-if="creatable"
          >New Item</v-btn>
        </div>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">{{ formTitle }}</span>
        </v-card-title>

        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>
              <v-flex xs12 sm6 md4 v-for="header in headers" :key="header.value">
                <v-text-field v-model="editedItem[header.value]" :label="header.text"></v-text-field>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="secondary" flat @click="close">Cancel</v-btn>
          <v-btn color="primary" @click="save">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <div :style="`width:${width}`" style="margin:0 auto;">
      <v-data-table
        :headers="headers"
        :items="items"
        class="elevation-1"
        :rows-per-page-items="[10,25,50,{'text':'$vuetify.dataIterator.rowsPerPageAll','value':-1}]"
      >
        <template v-slot:items="props">
          <td
            class="text-xs-center"
            v-for="header in headers"
            :key="header.value"
          >{{ props.item[header.value] }}</td>
          <td class="justify-center layout px-0">
            <v-icon small class="mr-2" @click="editItem(props.item)">edit</v-icon>
            <v-icon small @click="deleteItem(props.item)">delete</v-icon>
          </td>
        </template>
      </v-data-table>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      default: "title"
    },
    creatable: {
      tyle: Boolean,
      default: true
    },
    headers: {
      type: Array,
      default: () => [
        {
          text: "test",
          value: "key",
          sortable: true,
          align: "left"
        }
      ]
    },
    value: {
      type: Array,
      default: () => [
        {
          key: "hoge"
        }
      ]
    },
    width: {
      type: String,
      default: "100%"
    }
  },
  data: () => ({
    dialog: false,
    editedIndex: -1,
    editedItem: {}
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    },
    items: {
      get() {
        return this.value;
      },
      set(val) {
        this.$emit("input", val);
      }
    }
  },
  mounted() {
    const keys = this.headers.map(header => header.value);
    const items = {};
    for (let key of keys) {
      items[key] = "";
    }
    this.editedItem = items;
  },
  watch: {
    dialog(val) {
      val || this.close();
    }
  },

  methods: {
    editItem(item) {
      this.editedIndex = this.items.indexOf(item);
      this.editedItem = { ...item };
      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.items.indexOf(item);
      confirm("Are you sure you want to delete this item?") &&
        this.items.splice(index, 1);
    },

    close() {
      this.dialog = false;
      this.editedItem = {};
      this.editedIndex = -1;
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.items[this.editedIndex], this.editedItem);
      } else {
        this.items.push(this.editedItem);
      }
      this.items = this.items.filter(v => Object.keys(v).some(k => v[k]));
      this.close();
    }
  }
};
</script>

<style>
.v-table__overflow {
  overflow-x: unset !important;
  overflow-y: unset !important;
}
</style>
