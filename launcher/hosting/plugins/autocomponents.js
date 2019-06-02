import Vue from 'vue'

const mixinComponents = {}
for (let component of process.env.components) {
  let { name, path } = component
  path = path.replace('@', '..')
  console.log({
    name,
    path,
    isSame: path === '../components/HelperOffset.vue',
    hoge1: require('../components/HelperOffset.vue')
  })
  eval(`import _default from '${path}'`)
  mixinComponents[name] = _default
}

Vue.mixin({
  components: mixinComponents
})
