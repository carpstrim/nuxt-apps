<template>
  <v-layout fill-height align-center justify-center style="padding-bottom:10rem">
    <data-table title="code table" v-model="items" :headers="headers" width="80%" />

    width:{{window.innerWidth}}
    height:{{window.innerHeight}}
    width:{{document.documentElement.clientWidth}}
    height:{{document.documentElement.clientHeight}}
  </v-layout>
</template>

<script>
export default {
  layout: "live-ocr",
  asyncData() {
    const items = localStorage.getItem("live-ocr/option/items") || "[]";
    return { items: JSON.parse(items) };
  },
  data() {
    return {
      headers: [
        { value: "code", text: "code", sortable: true },
        { value: "label", text: "品名1", sortable: true }
      ],
      window: window,
      document: document
    };
  },
  watch: {
    items(val) {
      localStorage.setItem("live-ocr/option/items", JSON.stringify(this.items));
    }
  }
};
</script>
