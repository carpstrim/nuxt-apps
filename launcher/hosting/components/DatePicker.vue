<template>
  <v-menu
    ref="menu"
    v-model="menu"
    :close-on-content-click="false"
    :nudge-right="40"
    lazy
    transition="scale-transition"
    offset-y
    full-width
    min-width="290px"
  >
    <template v-slot:activator="{ on }">
      <v-text-field
        v-model="date"
        :label="label"
        readonly
        v-on="on"
        :outline="outline"
      ></v-text-field>
    </template>
    <v-date-picker
      ref="picker"
      v-model="date"
      min="1950-01-01"
      @change="save"
      dark
      locale="ja"
      :day-format="date => new Date(date).getDate()"
    ></v-date-picker>
  </v-menu>
</template>

<script>
export default {
  props: {
    value: {
      type: String,
      default: null
    },
    label: {
      type: String,
      default: null
    },
    outline: {
      type: Boolean,
      default: false
    },
    birthday: {
      type: Boolean,
      default: false
    }
  },
  data: () => ({
    menu: false
  }),
  computed: {
    date: {
      get() {
        return this.value;
      },
      set(val) {
        this.$emit("input", val);
      }
    }
  },
  watch: {
    menu(val) {
      if (!this.birthday) return;
      val && setTimeout(() => (this.$refs.picker.activePicker = "YEAR"));
    }
  },
  methods: {
    save(date) {
      this.$refs.menu.save(date);
    }
  }
};
</script>
