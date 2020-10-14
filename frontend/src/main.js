// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import store from './store'

Vue.config.productionTip = false

// var api = axios.defaults.baseURL = "http://127.0.0.1:8000/api"
// new Vue の前に読み込まないとundefindになる
Vue.prototype.$axios = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
  // baseURL: 'https://sinapse-202010111705.herokuapp.com/',
})

Vue.prototype.$axiosAuth = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
  // baseURL: 'https://sinapse-202010111705.herokuapp.com/',
})

Vue.prototype.$axios.interceptors.response.use(
  res => {
    console.log(res.status)
    if (res.data) {
      console.log(res.data)
    }
    return res
  },
  err => {
    window.alert('処理に失敗しました')
    console.log(err)
    return Promise.reject(err)
  }
)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
