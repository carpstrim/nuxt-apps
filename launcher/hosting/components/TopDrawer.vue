<template>
  <v-navigation-drawer
    id="app-drawer"
    v-model="drawer"
    app
    dark
    floating
    persistent
    :mobile-break-point="breakPoint"
    width="260"
  >
    <v-img :src="image" height="100%">
      <v-layout class="fill-height" column tag="v-list">
        <v-list-tile avatar to="/">
          <v-list-tile-avatar>
            <v-img :src="logo"/>
          </v-list-tile-avatar>
          <v-list-tile-title class="title">Thous&Apps</v-list-tile-title>
        </v-list-tile>

        <template v-for="(link, i) in links">
          <v-list-tile
            v-if="link.to || link.href"
            :key="link.text"
            :to="link.to"
            :href="link.href"
            :target="(link.href)? '_blank':''"
            active-class="info"
            avatar
            class="v-list-item"
          >
            <v-list-tile-action>
              <v-icon>{{ link.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-title v-text="link.text"/>
          </v-list-tile>
          <v-divider v-else-if="link.divider" :key="i"/>
          <v-subheader
            v-else-if="link.header"
            :key="link.header"
            class="grey--text text--lighten-4"
          >{{ link.header }}</v-subheader>
        </template>
      </v-layout>
    </v-img>
  </v-navigation-drawer>
</template>

<script>
import Logo from "@/static/icon_origin.png";
import sidebarImage from "@/static/sidebar1.jpg";

export default {
  data: () => ({
    dialog: false,
    image: sidebarImage,
    logo: Logo,
    drawer: false
  }),
  props: {
    breakPoint: {
      type: String,
      default: "900"
    },
    links: {
      type: Array,
      default: []
    },
    sync: {
      type: Function,
      default: () => {
        console.log("oops");
      }
    }
  },
  mounted() {
    this.drawer = screen.width > this.breakPoint ? true : false;
  },
  computed: {},
  methods: {
    switch() {
      this.drawer = !this.drawer;
    }
  }
};
</script>

<style lang="scss">
//@import "@/assets/style/index.scss";

#app-drawer {
  .v-list__tile {
    border-radius: 4px;

    &--buy {
      margin-top: auto;
      margin-bottom: 17px;
    }
  }

  .v-image__image--contain {
    top: 9px;
    height: 60%;
  }

  .search-input {
    margin-bottom: 30px !important;
    padding-left: 15px;
    padding-right: 15px;
  }
}
</style>
