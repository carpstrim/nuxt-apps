<template>
  <date-picker
    v-model="value"
    label="date"
  />
</template>

<script>
export default {
  data() {
    return {
      datetime: "",
      value: null
    };
  },
  watch: {
    value(val) {
      console.log("parent", { val });
    }
  }
};
</script>
