<template>
  <v-container
    fill-height
    fluid
    grid-list-xl
  >
    <v-layout
      justify-center
      wrap
    >
      <v-flex
        xs12
        md8
      >
        <material-card color="info">
          <div slot="header">
            <div class="title font-weight-light mb-2">{{ title }}</div>
            <div class="category">{{ subtitle }}</div>
          </div>
          <v-img :src="hocLogo"></v-img>
          <v-card-text>
            <h4>未経験からでもWeb/アプリが作れる世界へ</h4>
            <p>「手を動かしながら学ぶ」をモットーに、Webサイト・Webアプリ等の開発を学ぶ社会人チーム。</p>
            <br>
            <h4>学びを最大化する3つの活動</h4>
            <p>「手を動かしながら学ぶ」ことを大事にしながら勉強していきます。</p>
            <br>
            <h5>1. 費用を抑えながらみんなで勉強</h5>
            <p>部活のように部費を集め、その予算内で書籍や動画教材等を購入・シェアしながら勉強するため、コストを抑えて学べます</p>
            <br>
            <h5>2. 一気通貫したアプリ開発経験</h5>
            <p>
              動くものを作り切るまでがアプリ開発の学びです。フロントエンド/バックエンド問わず、全て各自で1から作ります。開発までのステップをみんなで一緒に経験します。
              <br>
              <a
                href="https://docs.google.com/presentation/d/1nLsdBQXrIku6JDs5YlCaY2y8Yy7OkBfCD6A7aY8OGzU/edit?usp=sharing"
                target="_blank"
              >参考:進め方キックオフ資料</a>
              <iframe
                src="https://docs.google.com/presentation/d/e/2PACX-1vQr0iuqH_hQoHLBCR_TNNj3EGnX8WrIizdaX-bAeq5KVNXGyNmXwhzsuPVikKtPJSP2CGT7oFPdAAxB/embed?start=false&loop=true&delayms=3000"
                frameborder="0"
                width="100%"
                height="100%"
                allowfullscreen="true"
                mozallowfullscreen="true"
                webkitallowfullscreen="true"
              ></iframe>
            </p>
            <br>
            <h5>3. 擬似的な実務経験</h5>
            <p>フリーランス案件や知り合いからの案件を請け負うメンバーをリーダーとして、小規模のプロジェクトチームを作って、実際の案件を経験します。アプリ開発に慣れた方はこのチームに参画することができます。</p>
            <br>
            <h4>活動概要</h4>
            <p>メインはWEB会議(hangout等)にて遠隔での勉強会を定期的に開催しています。メンバーのほとんどは会社員ですので、平日の夜が多いです。</p>
            <p>毎週月曜日 22:00から：WEBサイト開発勉強会</p>
            <p>毎週水曜日 22:00から：WEBアプリ開発勉強会</p>
            <p>毎週木曜日 22:00から：python勉強会</p>
            <p>ゲリラ開催（主に土曜日）： 復習会＠梅田など</p>
            <p>すべての勉強会に参加する必要はありません。すべて任意参加でゆる〜くやっています</p>
            <br>
            <h4>興味がある方はぜひご連絡ください</h4>
            <div style="display:flex">
              <img
                style="margin:0 2px"
                :src="twitterIcon"
                width="23px"
              >
              <a
                href="https://twitter.com/KnmsStr"
                target="_blank"
              >@KnmsStr</a>
            </div>
          </v-card-text>
        </material-card>
      </v-flex>
      <v-flex
        xs12
        md4
      >
        <v-layout
          justify-center
          row
          wrap
        >
          <v-flex
            xs12
            v-for="(block,i) in blocks"
            :key="i"
          >
            <material-card
              class="v-card-profile"
              style="width:100%"
            >
              <v-avatar
                slot="offset"
                class="mx-auto d-block"
                size="130"
              >
                <img :src="block.img">
              </v-avatar>
              <v-card-text class="text-xs-center">
                <h4>{{ block.title}}</h4>
                <h6>{{ block.subtitle}}</h6>
                <div class="text-xs-left">
                  <p
                    class="card-description font-weight-light"
                    v-for="text in block.texts"
                    :key="text"
                  >{{text}}</p>
                </div>
              </v-card-text>
            </material-card>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import hocLogo from "@/static/hoclogo.png";
import abuIcon from "@/static/abu.jpg";
import twitterIcon from "@/assets/twitter.png";
export default {
  data() {
    return {
      hocLogo,
      twitterIcon,
      title: "We are Members of Hands-on-Campus.com (HoC)",
      subtitle: "weekly apps developer",
      blocks: [
        {
          img: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
          title: "のーど",
          subtitle: "HOC 副代表",
          texts: ["アプリ千本ノックの発起人。"]
        },
        {
          img: abuIcon,
          title: "あぶ",
          subtitle: "HoC 代表",
          texts: [
            "のーどの企画に便乗した人。",
            "データサイエンスが本業。",
            "社内外問わずWEBアプリビジネスの企画/開発/運用を一気通貫して実施"
          ]
        }
      ]
    };
  }
};
</script>
