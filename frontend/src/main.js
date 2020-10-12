// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'

Vue.config.productionTip = false

// var api = axios.defaults.baseURL = "http://127.0.0.1:8000/api"
// new Vue の前に読み込まないとundefindになる
Vue.prototype.$axios = axios.create({
  // baseURL: 'http://127.0.0.1:8000/',
  baseURL: 'https://sinapse-202010111705.herokuapp.com/',
  // timeout: 2000,
  // headers: { 'X-Custom-Header': 'CustomHeader2' }
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
