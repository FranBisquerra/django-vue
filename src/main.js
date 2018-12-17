import Vue from 'vue'
import App from '@/App.vue'

import router from '@/router'
import $backend from '@/backend'
import 'bootstrap/dist/css/bootstrap.min.css'

Vue.prototype.$backend = $backend
Vue.config.productionTip = false

// Vue.use(VueRouter)

const vue = new Vue({
  router,
  render: h => h(App)
})

vue.$mount('#app')
