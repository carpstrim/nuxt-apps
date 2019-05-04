<template>
  <v-layout
    column
    justify-center
    align-center
  >
    <v-flex
      xs12
      sm8
      md6
    >
      <v-card>
        <v-card-title class="headline">Welcome to GCJ Admin Page</v-card-title>
        <v-card-text>
          <p>This page is for admin users of GCJ. Please click(tap) on members or events from left bar / following links.</p>
          <p>To see all guests in GCJ, click <nuxt-link
            to="/members"
          >HERE</nuxt-link>.</p>
          <p>To see all events in GCJ, click <nuxt-link
            to="/events"
          >HERE</nuxt-link>.</p>
          <p>Thank you for operating GCJ and I look forward to bringing more exciting features in the future.</p>
          <div class="text-xs-right">
            <em><small>&mdash; Shutaro Kunimasa</small></em>
          </div>
          <hr class="my-3">
          <a
            href="https://gitlab.com/kunimasandbox/macaron"
            target="_blank"
          >Developer's Documentation</a>
        </v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>

export default {
}
</script>
