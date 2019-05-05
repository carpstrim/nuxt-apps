<template>
  <v-content>
    <div id="core-view">
      <v-fade-transition mode="out-in">
        <nuxt/>
      </v-fade-transition>
      <v-footer dark inset fixed app style="justify-content: flex-end">
        <span style="padding:1vw">
          <strong>
            &copy; 2019 -
            Hands-on-Campus.com
          </strong>
        </span>
      </v-footer>
    </div>
  </v-content>
</template>

<script>
export default {
  metaInfo() {
    return {
      title: "Vuetify Material Dashboard by CreativeTim"
    };
  }
};
</script>

<style>
#core-view {
  padding-bottom: 100px;
}
</style>
