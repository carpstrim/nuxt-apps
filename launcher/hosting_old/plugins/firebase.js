const firebaseConfig = {
  apiKey: 'AIzaSyAgK48Xis8n-Mufh1N96kf0_S6KvbltklM',
  authDomain: 'macaron-prod.firebaseapp.com',
  databaseURL: 'https://macaron-prod.firebaseio.com',
  projectId: 'macaron-prod',
  storageBucket: 'macaron-prod.appspot.com',
  messagingSenderId: '689145384407',
  appId: '1:689145384407:web:621473e25d3ff377'
}
// Initialize Firebase
firebase.initializeApp(firebaseConfig)

// login watcher
export default function(app) {
  const { redirect, store } = app
}
