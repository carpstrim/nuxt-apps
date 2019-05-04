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
        全イベント数 {{num.total}} | リクエスト中 {{num.avaiable}} | ゲスト募集中 {{num.toGuest}} | お店予約中 {{num.toHost}}
        <v-card>
          <v-list three-line>
            <template v-for="(item,index) in eventsDisplay">
              <v-list-tile
                :key="item._id"
                avatar
              >
                <v-list-tile-content>
                  <v-list-tile-title>{{item.type}} | 登録日:{{item._createdAt | formatDate}} | ステータス:{{item.status.state}}</v-list-tile-title>
                  <v-list-tile-sub-title>開催時間:{{item.startAt|formatDateTime}} - {{item.endAt|formatTime}} </v-list-tile-sub-title>
                  <v-list-tile-sub-title>{{item.memberStr}} </v-list-tile-sub-title>
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
Vue.filter("formatDate", timestamp => {
  const date = new Date(timestamp);
  return `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
});
Vue.filter("formatDateTime", timestamp => {
  const date = new Date(timestamp);
  return `${date.getFullYear()}-${date.getMonth() +
    1}-${date.getDate()} ${date.getHours()}:${("0" + date.getMinutes()).slice(
    -2
  )}`;
});
Vue.filter("formatTime", timestamp => {
  const date = new Date(timestamp);
  return `${date.getHours()}:${("0" + date.getMinutes()).slice(-2)}`;
});

const db = firebase.firestore();
const _ = require("lodash");
export default {
  async asyncData({ store }) {
    const { docs } = await db
      .collection("events")
      .where("_createdAt", ">", 0)
      .get();
    const events = docs
      .map(doc => ({ _id: doc.id, ...doc.data() }))
      .map(doc => ({ ...doc, _idx: JSON.stringify(doc) }))
      .map(doc => {
        const memberStr = _.toArray(doc.guests)
          .map(guest => ({
            name: guest.profile.LINE.displayName,
            member: guest.member
          }))
          .reduce(
            (p, c) =>
              p +
              ` ${c.name} 男性:${c.member.male}名 女性:${c.member.female}名`,
            ""
          );
        return { ...doc, memberStr };
      })
      .sort((a, b) => b._createdAt - a._createdAt);
    const idx = ["type"].map(key =>
      events
        .map(event => event[key])
        .filter((e, i, A) => e && A.indexOf(e) === i)
    );
    store.commit("setSearchIdx", _.flatten(idx));
    return { events };
  },
  computed: {
    num() {
      return {
        total: this.events.length,
        avaiable: this.events.filter(
          ({
            status: {
              isRequestable: { guest, host }
            }
          }) => guest || host
        ).length,
        toGuest: this.events.filter(
          ({
            status: {
              isRequestable: { guest }
            }
          }) => guest
        ).length,
        toHost: this.events.filter(
          ({
            status: {
              isRequestable: { host }
            }
          }) => host
        ).length
      };
    },
    eventsDisplay() {
      const { searchWord } = this.$store.state;
      return this.events.filter(
        event => !searchWord || event._idx.indexOf(searchWord) !== -1
      );
    }
  }
};
</script>
