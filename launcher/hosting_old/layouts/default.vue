<template>
  <v-app>
    <v-toolbar
      :clipped-left="clipped"
      fixed
      app
    >
      <v-toolbar-side-icon
        @click="drawer = !drawer"
        v-show="notLoginPage"
      />
      <v-spacer />
      <v-autocomplete
        prepend-icon="search"
        :items="searchIdx"
        :search-input.sync="search"
        clearable
        v-model="val"
      ></v-autocomplete>
    </v-toolbar>
    <v-content>
      <nuxt />
    </v-content>
    <v-footer
      :fixed="fixed"
      app
      style="justify-content: flex-end"
    >
      <span style="padding:1vw">&copy; 2019 hands-on-campus.com</span>
    </v-footer>
    <top-drawer
      :open="drawer"
      :links="links"
    />

  </v-app>
</template>

<script>
export default {
  computed: {
    notLoginPage() {
      return this.$route.name !== "login";
    }
  },
  data() {
    return {
      search: null,
      val: null,
      clipped: false,
      drawer: false,
      fixed: false,
      searchIdx: [],
      items: [
        {
          icon: "apps",
          title: "top",
          to: "/"
        },
        {
          icon: "supervisor_account",
          title: "Members",
          to: "/members"
        },
        {
          icon: "class",
          title: "Events",
          to: "/events"
        }
      ],
      links: [
        { header: "Main" },
        {
          to: "/brains",
          icon: "mdi-cube-outline",
          text: "Brain"
        },
        {
          to: "/detections",
          icon: "mdi-eye-check",
          text: "Detection"
        },
        { divider: true },
        { header: "Advanced" },
        {
          to: "/automations",
          icon: "mdi-robot",
          text: "Automation"
        },
        { divider: true },
        { header: "Settings" },
        {
          to: "/profile",
          icon: "mdi-account",
          text: "Profile"
        },
        {
          to: "/settings",
          icon: "mdi-settings",
          text: "More Settings"
        }
      ],
      miniVariant: false
    };
  },
  watch: {
    search(val) {
      console.log(val);
    }
  }
};
</script>

<style lang="scss">
</style>
