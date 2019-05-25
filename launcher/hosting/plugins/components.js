import Vue from 'vue'

import MaterialCard from '@/components/MaterialCard'
import HelperOffset from '@/components/Offset'
import UploadBtn from '@/components/UploadBtn'
import VContextMenu from '@/components/VContextMenu'
import VImageUpload from '@/components/VImageUpload'

Vue.mixin({
  components: {
    MaterialCard,
    HelperOffset,
    UploadBtn,
    VContextMenu,
    VImageUpload
  }
})
