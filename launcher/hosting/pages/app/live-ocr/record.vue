<template>
  <v-layout justify-center class="pt-5">
    <data-table title="records" v-model="items" :creatable="false" :headers="headers" width="80%" />
  </v-layout>
</template>

<script>
export default {
  layout: "live-ocr",
  asyncData() {
    const items = localStorage.getItem("live-ocr/option/record") || "[]";
    return { items: JSON.parse(items) };
  },
  data() {
    return {
      headers: [
        { value: "createdAt", text: "記録日時", sortable: true },
        { value: "code", text: "code", sortable: true },
        { value: "label", text: "品名1", sortable: true }
      ]
    };
  }
};
</script>
