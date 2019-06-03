// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import VeeValidate from 'vee-validate'
import VuejsPaginate from 'vuejs-paginate'
import App from './App'
import axios from 'axios'
import 'es6-promise/auto'
import router from './router'
import store from './store'

Vue.config.productionTip = false

export const HTTP = axios.create({
  baseURL: new URL('api', window.location.origin).href
})
Vue.prototype.$http = HTTP

Vue.use(VeeValidate)
Vue.component('paginate', VuejsPaginate)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router: router,
  store: store,
  components: { App },
  template: '<App/>'
})
