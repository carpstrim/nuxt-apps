import Vue from 'vue'

import MaterialCard from '@/components/MaterialCard'
import HelperOffset from '@/components/Offset'
import UploadBtn from '@/components/UploadBtn'
import DatetimePicker from 'vue-ctk-date-time-picker'
import 'vue-ctk-date-time-picker/dist/vue-ctk-date-time-picker.css';

Vue.mixin({
  components: {
    MaterialCard,
    HelperOffset,
    UploadBtn,
    DatetimePicker
  }
})
