import Vue from 'vue'

import MaterialCard from '@/components/MaterialCard'
import HelperOffset from '@/components/HelperOffset'
import UploadBtn from '@/components/UploadBtn'
import VContextMenu from '@/components/VContextMenu'
import VImageUpload from '@/components/VImageUpload'
import VAddressForm from '@/components/VAddressForm'
import DatePicker from '@/components/DatePicker'
import CameraReader from '@/components/CameraReader'

Vue.mixin({
  components: {
    MaterialCard,
    CameraReader,
    HelperOffset,
    UploadBtn,
    VContextMenu,
    VImageUpload,
    VAddressForm,
    DatePicker
  }
})
