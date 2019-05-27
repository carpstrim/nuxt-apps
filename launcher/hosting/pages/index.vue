<template>
  <v-container fill-height>
    <v-layout
      row
      justify-center
      align-center
    >
      <v-flex
        xs12
        sm8
        md8
        lg5
      >
        <v-card>
          <v-img
            src="/icon_origin.jpg"
            aspect-ratio="1"
          />
          <v-card-text>
            <h4>ようこそ！</h4>
          </v-card-text>
          <v-card-text>
            <v-subheader>非IT会社員が毎週アプリをロンチし、いつか千本のアプリを作る「アプリ千本ノック」企画から生まれたアプリ達をまとめています。</v-subheader>
          </v-card-text>
          <v-card-actions>
            <v-layout
              row
              justify-end
            >
              <v-flex
                xs12
                style="display:flex; justify-content:flex-end;"
              >
                <v-btn
                  to="/apps"
                  color="info"
                  class="ma-1"
                >アプリ一覧</v-btn>
                <v-btn
                  href="https://app-senbonknock.com/"
                  target="_blank"
                  flat
                  outline
                  color="secondary"
                  class="ma-1"
                >ブログ<v-icon
                    small
                    left
                  >mdi-launch</v-icon>
                </v-btn>
              </v-flex>
            </v-layout>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  layout: "plain"
};
</script>

<style>
</style>
