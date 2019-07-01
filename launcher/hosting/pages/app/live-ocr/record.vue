<template>
  <v-layout
    justify-center
    class="pt-5"
  >
    <data-table
      title="records"
      v-model="items"
      :creatable="false"
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
      items: [{ code: "11", label: "hoge", createdAt: 0 }],
      headers: [
        { value: "createdAt", text: "記録日時", sortable: true },
        { value: "code", text: "code", sortable: true },
        { value: "label", text: "品名1", sortable: true }
      ]
    };
  }
};
</script>
