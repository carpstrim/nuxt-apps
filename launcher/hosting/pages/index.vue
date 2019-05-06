<template>
  <v-layout column justify-center align-center>
    <v-flex xs12 sm8 md6>
      <v-card>
        <v-card-title class="headline">Welcome to Thous&Apps Page</v-card-title>
        <v-card-text>
          <p>This page is for platform of our awesome apps.</p>
          <p>
            To see all apps, click
            <nuxt-link to="/apps">HERE</nuxt-link>.
          </p>
          <p>
            To see any infomations about us, click
            <nuxt-link to="/aboutus">HERE</nuxt-link>.
          </p>
          <div class="text-xs-right">
            <em>
              <small>&mdash; Hands-on-Campus.com</small>
            </em>
          </div>
          <hr class="my-3">
          <a href="https://app-senbonknock.com/" target="_blank">Developer's Blog</a>
        </v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {};
</script>
