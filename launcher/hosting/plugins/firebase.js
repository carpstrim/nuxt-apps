const firebaseConfig = {}
// Initialize Firebase
//firebase.initializeApp(firebaseConfig)

// login watcher
export default function(app, inject) {
  inject('shortenUrl', async url => {
    const dinamicLinkKey = 'AIzaSyDBvDpoOMev5cei3JtX9I7dN28pcBrxP4U'
    const endpoint = `https://firebasedynamiclinks.googleapis.com/v1/shortLinks?key=${dinamicLinkKey}`
    const data = {
      longDynamicLink: `https://thousandapps.page.link/?link=${url}`
    }
    const { shortLink } = await app.$axios.$post(endpoint, data, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    return shortLink
  })
}
