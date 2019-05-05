<template>
  <v-app>
    <top-drawer :open="drawer" :links="links"/>
    <top-bar :drawerFnc="()=>drawer=!drawer"/>
    <top-view/>
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
      drawer: true,
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
          to: "/contact",
          icon: "chat",
          text: "Contact"
        },
        { divider: true },
        { header: "Advanced" },
        {
          to: "/specials",
          icon: "star",
          text: "Specials"
        },
        { divider: true },
        { header: "Credits" },
        {
          to: "/profile",
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
