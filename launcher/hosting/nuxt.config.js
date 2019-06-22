const pkg = require('./package')

/*
const components = () => {
  const fs = require('fs')
  const $path = require('path')
  function getPaths(dirPath) {
    return fs.readdirSync(dirPath)
  }
  function getFiles(pathDir, include = '') {
    const paths = getPaths(pathDir)
    let files = []
    for (let path of paths) {
      path = `${pathDir}/${path}`
      const stat = fs.statSync(path)

      if (stat.isFile() && path.indexOf(include) >= 0) {
        const name = $path.basename(path, '.vue')
        files.push({ name, path: path.replace('.', '@') })
      }
      if (stat.isDirectory()) files = files.concat(getFiles(path))
    }
    return files
  }
  const components = getFiles('./components', '.vue')
//  console.log({ components })
  return components
}
*/

module.exports = {
  mode: 'spa',

  //  env: { components: components() },
  /*
   ** Headers of the page
   */
  head: {
    title: pkg.name,
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: pkg.description }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: 'stylesheet',
        href:
          'https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons'
      },
      {
        rel: 'stylesheet',
        href:
          '//cdn.materialdesignicons.com/3.6.95/css/materialdesignicons.min.css'
      }
    ],
    script: [
      /*
      { src: 'https://www.gstatic.com/firebasejs/5.11.1/firebase-app.js' },
      {
        src: 'https://www.gstatic.com/firebasejs/5.11.1/firebase-firestore.js'
      },
      { src: 'https://www.gstatic.com/firebasejs/5.11.1/firebase-auth.js' }
      */
    ]
  },

  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },

  /*
   ** Global CSS
   */
  //  css: ['~/assets/style/app.styl'],

  /*
   ** Plugins to load before mounting the App
   */
  plugins: ['@/plugins/firebase', '@/plugins/components'],

  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
    '@nuxtjs/vuetify'
  ],
  manifest: {
    name: 'Thous&Apps',
    lang: 'ja'
  },
  /*
   ** Axios module configuration
   */
  axios: {
    // See https://github.com/nuxt-community/axios-module#options
  },

  /*
   ** Build configuration
   */
  build: {
    //    transpile: ['vuetify/lib'],
    //    plugins: [new VuetifyLoaderPlugin()],
    /*
        loaders: {
          stylus: {
            import: ['~assets/style/variables.styl']
          }
        },
    */
    /*
     ** You can extend webpack config here
     */
    extend(config, ctx) {
      config.node = { fs: 'empty' }
    }
  }
}
