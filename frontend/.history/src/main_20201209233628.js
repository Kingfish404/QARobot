import Vue from 'vue'
import App from './App.vue'
import Buefy from 'buefy'
imoprt import 'buefy/dist/buefy.css'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
