<template>
  <v-app>
    <top-drawer v-model="drawer" :links="links" />
    <top-bar :drawerFnc="()=>{drawer=!drawer}" />
    <top-view />
  </v-app>
</template>

<script>
import TopDrawer from "@/components/TopDrawer";
import TopBar from "@/components/TopBar";
import TopView from "@/components/TopView";

export default {
  components: {
    TopDrawer,
    TopBar,
    TopView
  },
  computed: {
    notLoginPage() {
      return this.$route.name !== "login";
    }
  },
  data() {
    return {
      search: null,
      val: null,
      drawer: false,
      fixed: false,
      searchIdx: [],
      links: [
        { header: "Main" },
        {
          to: "/apps",
          icon: "apps",
          text: "Apps"
        },
        {
          href: "https://app-senbonknock.com/",
          icon: "book",
          text: "Blog"
        },
        {
          to: "/dev",
          icon: "mdi-wrench",
          text: "Under Development"
        },
        { divider: true },
        { header: "Credits" },
        {
          to: "/aboutus",
          icon: "supervisor_account",
          text: "About us"
        },
        {
          to: "/thanks",
          icon: "favorite",
          text: "Thanks"
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
@import "@/assets/style/index.scss";
</style>
