<template>
  <datetime-picker v-model="datetime" range/>
</template>

<script>
export default {
  data() {
    return {
      datetime: ""
    };
  }
};
</script>
