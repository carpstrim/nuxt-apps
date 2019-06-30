<template>
  <div id="app">
    <v-app id="inspire">
      <div>
        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ on }">
            <div class="justify-space-between align-center layout ma-0" style="width:100%">
              <h3>title</h3>
              <v-btn color="primary" dark class="mb-2" v-on="on" round flat outline>New Item</v-btn>
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
        <v-data-table :headers="headers" :items="items" class="elevation-1">
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
    </v-app>
  </div>
</template>

<script>
export default {
  props: {
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
    }
  },
  data: () => ({
    dialog: false,
    editedIndex: -1,
    editedItem: {},
    defaultItem: {}
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
    const [item] = JSON.parse(JSON.stringify(this.value));
    for (let key in item) {
      item[key] = "";
    }
    this.editedItem = item;
    this.defaultItem = item;
    console.log(this.editedItem);
  },

  watch: {
    dialog(val) {
      val || this.close();
    }
  },

  methods: {
    editItem(item) {
      this.editedIndex = this.items.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.items.indexOf(item);
      confirm("Are you sure you want to delete this item?") &&
        this.items.splice(index, 1);
    },

    close() {
      this.dialog = false;
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300);
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.items[this.editedIndex], this.editedItem);
      } else {
        this.items.push(this.editedItem);
      }
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
