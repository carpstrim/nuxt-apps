<template>
  <v-container>
    <h3>Devpage</h3>
    <v-flex xs6>
      <v-text-field
        v-model="text"
        append-outer-icon="mdi-arrow-right-circle-outline"
        @click:append-outer="go"
        @keyup.enter="go"
      />
    </v-flex>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      text: ""
    };
  },
  methods: {
    go() {
      if (!this.text) return;
      this.$router.push(this.text);
    }
  }
};
</script>
