<template>
  <div class="ma-4">
    <v-layout justify-end>
      <v-btn flat color="info" @click="text=transform(text)">
        <v-icon left>mdi-auto-fix</v-icon>auto fix
      </v-btn>

      <!-- Download Menu-->
      <v-menu offset-y>
        <template v-slot:activator="{ on }">
          <v-btn flat color="info" v-on="on">
            <v-icon left>mdi-download</v-icon>download
          </v-btn>
        </template>
        <v-list>
          <v-list-tile v-for="(item, index) in items" :key="index" @click="item.onclick">
            <v-list-tile-title>
              <v-layout align-center>
                <v-icon class="mr-2">{{item.icon}}</v-icon>
                {{ item.title }}
              </v-layout>
            </v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-menu>
    </v-layout>

    <!-- viz area -->
    <v-layout row wrap>
      <v-flex xs12 sm3 class="textarea">
        <v-textarea v-model="text" height="100%" background-color outline label="input area"/>
      </v-flex>
      <v-flex xs12 sm9 class="vizarea">
        <div id="viz"/>
      </v-flex>
    </v-layout>

    <!--snackbar-->
    <v-snackbar v-model="snackbar" multi-line :timeout="3000" top right>
      Share URL Copied!
      <v-btn color="warning" flat @click="snackbar = false">Close</v-btn>
    </v-snackbar>
  </div>
</template>

<script>
</script>

<script>
import Viz from "viz.js";
import { Module, render } from "viz.js/full.render.js";
let viz = new Viz({ Module, render });

export default {
  asyncData({ query, redirect, from }) {
    if (query.viztext) {
      redirect(from.path);
      return;
    }
    const {
      query: { viztext }
    } = from;
    const vizText =
      viztext || localStorage.getItem("vizText") || "digraph{\na->b\n}";
    return { text: vizText };
  },
  data() {
    return {
      snackbar: false,
      compile: null,
      items: [
        { title: "image (.png)", icon: "mdi-image", onclick: this.download },
        { title: "share link", icon: "mdi-link", onclick: this.getShareURL }
      ]
    };
  },
  methods: {
    transform(text) {
      return text
        .split("\n")
        .map(row => {
          const [option] = row.match(/(\[.*\])/) || [""];
          const rowFixed = row.replace(option, "");
          const elements = rowFixed.split(/[<-][->]/);
          const elementsR = rowFixed.split("->");
          if (elementsR.length === elements.length && elementsR.length <= 2)
            return row;
          const [, ...reverses] = elements
            .map(e => row.slice(row.indexOf(e) - 2, row.indexOf(e)))
            .map(arrow => arrow === "<-");
          const relations = reverses.map(
            (reverse, i) =>
              (reverse
                ? `${elements[i + 1]}->${elements[i]}`
                : `${elements[i]}->${elements[i + 1]}`) + option
          );

          return relations.reduce((p, c) => `${p}\n${c}`);
        })
        .reduce((p, c) => `${p}\n${c}`);
    },
    download() {
      const svg = document.querySelector("svg");
      const svgData = new XMLSerializer().serializeToString(svg);
      const canvas = document.createElement("canvas");
      canvas.width = svg.width.baseVal.value;
      canvas.height = svg.height.baseVal.value;

      const ctx = canvas.getContext("2d");
      const image = new Image();
      image.onload = function() {
        ctx.drawImage(image, 0, 0);
        const a = document.createElement("a");
        a.href = canvas.toDataURL("image/png");
        a.setAttribute("download", "vizgraph.png");
        a.click();
      };
      image.src =
        "data:image/svg+xml;charset=utf-8;base64," +
        btoa(unescape(encodeURIComponent(svgData)));
    },
    getShareURL() {
      const url = `${window.location.href}?viztext=${encodeURIComponent(
        this.text
      )}`;
      let clipboard = document.createElement(`textarea`);
      clipboard.value = url;
      document.body.appendChild(clipboard);
      clipboard.select();
      document.execCommand("copy");
      clipboard.parentElement.removeChild(clipboard);
      this.snackbar = true;
    },
    renderViz(vizText) {
      viz
        .renderSVGElement(vizText)
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
  },
  mounted() {
    this.renderViz(this.text);
  },
  watch: {
    text(val) {
      if (this.compile) clearInterval(this.compile);
      // text transfroming
      this.compile = setTimeout(() => {
        val = this.transform(val); // auto-fix
        this.renderViz(val); // viz2svg
        localStorage.setItem("vizText", val);
      }, 500);
    }
  }
};
</script>

<style>
.textarea {
  height: 85vmin;
}
.v-textarea {
  height: calc(100%);
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
