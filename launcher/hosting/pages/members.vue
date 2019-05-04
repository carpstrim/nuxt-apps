<template>
  <v-container>
    <v-layout
      justify-center
      align-center
    >
      <v-flex
        xs12
        justify-center
        align-center
      >
        全ユーザー数 {{num.total}}名 | プロフィール登録ユーザ数 {{num.avaiable}}名 | 男性 {{num.male}}名 | 女性 {{num.female}}名
        <v-card>
          <v-list three-line>
            <template v-for="(item,index) in membersDisplay">
              <v-list-tile
                :key="item._id"
                avatar
              >
                <v-list-tile-avatar>
                  <v-img :src="item.pictureUrl"></v-img>
                </v-list-tile-avatar>

                <v-list-tile-content>
                  <v-list-tile-title>{{item.name}} ({{item.birthday|birthday2age}}) | 登録日:{{item._createdAt | formatDate}}</v-list-tile-title>
                  <v-list-tile-sub-title>{{item.gender|gender2jp}} | 職業:{{item.job}} | TEL:{{item.tel}}</v-list-tile-sub-title>
                  <v-list-tile-sub-title>希望年齢帯:{{item.regulations.guest.age|regAge}} </v-list-tile-sub-title>

                </v-list-tile-content>
              </v-list-tile>
              <v-divider :key="index" />
            </template>
          </v-list>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Vue from "vue";
Vue.filter("gender2jp", gender =>
  gender === "male" ? "🚹男性" : gender === "female" ? "🚺女性" : " 不明"
);
Vue.filter("birthday2age", birthday =>
  birthday
    ? Math.floor(
        (new Date().getTime() - birthday) / (1000 * 60 * 60 * 24 * 365)
      )
    : "-"
);
Vue.filter("regAge", age => {
  let first, last;
  for (let i in age) {
    if (!first && age[i]) first = i;
    if (first && age[i]) last = i;
  }
  return `${first}~${last}`;
});
Vue.filter("formatDate", timestamp => {
  const date = new Date(timestamp);
  return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
});
const db = firebase.firestore();
const _ = require("lodash");
export default {
  async asyncData({ store }) {
    const { docs } = await db
      .collection("users")
      .where("_createdAt", ">", 0)
      .get();
    const members = docs
      .map(doc => ({ _id: doc.id, ...doc.data() }))
      .map(doc => ({ ...doc, _idx: JSON.stringify(doc) }))
      .filter(({ _id }) => _id.indexOf("_host") === -1)
      .sort((a, b) => b._createdAt - a._createdAt);
    const idx = ["gender", "name", "job"].map(key =>
      members
        .map(member => member[key])
        .filter((e, i, A) => e && A.indexOf(e) === i)
    );
    store.commit("setSearchIdx", _.flatten(idx));
    return { members };
  },
  computed: {
    num() {
      return {
        total: this.members.length,
        avaiable: this.members.filter(member => member.gender).length,
        male: this.members.filter(member => member.gender === "male").length,
        female: this.members.filter(member => member.gender === "female").length
      };
    },
    membersDisplay() {
      const { searchWord } = this.$store.state;
      return this.members.filter(
        member => !searchWord || member._idx.indexOf(searchWord) !== -1
      );
    }
  }
};
</script>
