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
        md6
      >
        <v-card>
          <v-img :src="icon"></v-img>
          <v-card-text class="text-xs-center">
            <v-flex xs12>
              <v-text-field
                class="purple-input"
                label="Email Address"
                　@keyup.enter="enter"
                v-model="email"
              />
            </v-flex>
            <v-flex xs12>
              <v-text-field
                @keyup.enter="enter"
                class="purple-input"
                v-model="password"
                :append-icon="show ? 'visibility' : 'visibility_off'"
                :type="show ? 'text' : 'password'"
                label="Password"
                @click:append="show = !show"
              ></v-text-field>
            </v-flex>
            <v-flex
              xs12
              class="btn"
            >
              <v-btn
                color=secondary
                id="loginid"
                @click="login"
                :loading="loading"
              >Login</v-btn>
            </v-flex>
            <v-flex xs12>
              <p class="err">{{ errorText }}</p>
            </v-flex>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import icon from "~/static/icon.png";
export default {
  data() {
    return {
      showDialog: false,
      email: null,
      password: null,
      errorText: "",
      loading: false,
      show: false,
      icon
    };
  },
  methods: {
    enter() {
      document.getElementById("loginid").click();
    },
    login() {
      if (!this.email || !this.password) return;
      this.loading = true;
      firebase
        .auth()
        .signInWithEmailAndPassword(this.email, this.password)
        .then(() => {
          this.$router.push("/");
        })
        .catch(err => {
          this.errorText = err;
        })
        .finally(() => {
          this.loading = false;
        });
    }
  }
};
</script>
