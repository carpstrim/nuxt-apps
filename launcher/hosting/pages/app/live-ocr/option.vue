<template>
  <v-layout
    fill-height
    align-center
    justify-center
    style="padding-bottom:10rem"
  >
    <data-table
      title="code table"
      v-model="items"
      :headers="headers"
      width="80%"
    />
  </v-layout>
</template>

<script>
export default {
  layout: "live-ocr",
  data() {
    return {
      items: [{ code: "11", label: "hoge" }],
      headers: [
        { value: "code", text: "code", sortable: true },
        { value: "label", text: "品名1", sortable: true }
      ]
    };
  }
};
</script>
