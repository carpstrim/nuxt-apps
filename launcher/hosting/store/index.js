export const state = () => ({
  camera: false
})

export const mutations = {
  switchCamera(state) {
    state.camera = !state.camera
  },
  stopCamera(state) {
    state.camera = false;
  }
}
