<template>
  <div>
    <div @contextmenu="show">
      <slot></slot>
    </div>

    <v-menu
      v-model="showMenu"
      :position-x="x"
      :position-y="y"
      absolute
      offset-y
    >
      <v-list>
        <v-list-tile
          v-for="(item, index) in items"
          :key="index"
          @click="item.onClick"
        >
          <v-list-tile-title>{{ item.title }}</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-menu>
  </div>
</template>

<script>
export default {
  data: () => ({
    showMenu: false,
    x: 0,
    y: 0
  }),
  props: {
    items: {
      type: Array,
      default: () => []
    }
  },
  methods: {
    show(e) {
      e.preventDefault();
      this.showMenu = false;
      this.x = e.clientX;
      this.y = e.clientY;
      this.$nextTick(() => {
        this.showMenu = true;
      });
    }
  }
};
</script>
