<template>
  <div>
    <v-text-field
      v-model="innerValue.zipcode"
      label="郵便番号"
      :outline="outline"
      :error-messages="errorMsg"
    />
    <v-text-field
      v-model="innerValue.address"
      label="住所"
      :outline="outline"
      :error-messages="errorMsg"
    />
    <v-text-field
      v-model="innerValue.no"
      label="番地"
      :outline="outline"
    />

  </div>
</template>

<script>
export default {
  props: {
    value: {
      type: Object,
      default: () => ({
        zipcode: null,
        address: null
      })
    },
    outline: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      errorMsg: null
    };
  },
  computed: {
    innerValue: {
      get() {
        return this.value;
      },
      set(val) {
        this.$emit("input", val);
      }
    }
  },
  watch: {
    "innerValue.zipcode": async function(zipcode) {
      if (!zipcode) return;
      zipcode = zipcode.replace(/-/g, "");
      if (zipcode.length !== 7) {
        this.innerValue = { ...this.innerValue, address: null };
        return;
      }
      zipcode = zipcode.slice(0, 3) + "-" + zipcode.slice(3, 7);
      const { code, data } = await this.$axios.$get(
        `https://api.zipaddress.net/?zipcode=${zipcode}`
      );
      this.errorMsg = code === 200 ? null : "正しい郵便番号を入力してください";
      if (this.errorMsg) return;
      const { fullAddress: address } = data;
      this.innerValue = { ...this.innerValue, address, zipcode };
    }
  }
};
</script>
