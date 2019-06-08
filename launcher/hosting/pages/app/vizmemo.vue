<template>

  <div class="ma-4">
    <v-layout
      row
      wrap
    >
      <v-flex
        xs12
        sm3
        class="textarea"
      >
        <v-textarea
          v-model="text"
          height="100%"
          background-color
          outline
          label="input area"
        />
      </v-flex>
      <v-flex
        xs12
        sm9
        class="vizarea"
      >
        <div id="viz" />
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
</script>

<script>
import Viz from "viz.js";
import { Module, render } from "viz.js/full.render.js";
let viz = new Viz({ Module, render });
export default {
  data: () => ({
    text: ""
  }),
  mounted() {
    this.text = "digraph{\na->b\n}";
  },
  watch: {
    text(val) {
      // text transfroming

      const p = val.match(/(.*)<-(.*)\n/g);
      console.log({ p });
      // viz2svg
      viz
        .renderSVGElement(val)
        .then(element => {
          const vizElement = document.getElementById("viz");
          const child = vizElement.firstChild;
          if (child) vizElement.removeChild(child);
          vizElement.appendChild(element);
        })
        .catch(error => {
          viz = new Viz({ Module, render });
          console.log(error);
        });
    }
  }
};
</script>

<style>
.textarea {
  height: 85vmin;
}
.v-textarea {
  height: 100%;
}
.v-input__control {
  height: 100%;
}
.v-input__slot {
  margin-bottom: 0;
}
.vizarea {
  background-color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 85vmin;
}
svg {
  width: 100%;
}
#viz {
  overflow: scroll;
}
</style>
