<template>
  <v-toolbar
    flat
    app
    style="background: #eee;"
  >
    <v-btn
      flat
      icon
      color="secondary"
      @click="drawerFnc"
    >
      <v-icon>menu</v-icon>
    </v-btn>
    <v-spacer />
  </v-toolbar>
</template>

<script>
export default {
  props: {
    drawerFnc: {
      type: Function,
      default: () => {}
    }
  }
};
</script>
