import Vue from 'vue';
import Vuex from 'vuex';
import axiosAuth from '../auth'
import router from '../router';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: null
  },
  getters: {
    token: state => state.token
  },
  mutations: {
    updateToken(state, token) {
      state.token = token
    }
  },
  actions: {
    // tokenの有効期限を考慮していない
    autoLogin({ commit }) {
      const token = localStorage.getItem('token')
      if (!token) return
      commit('updateToken', token)
    },
    login({ commit }, authDate) {
      axiosAuth({
        method: "POST",
        url: 'login/',
        data: {
          email: authDate.email,
          password: authDate.password
        },
      })
      .then((res) => {
        console.log(res.data)
        commit('updateToken', res.data.token)
        // localStorageよりはcookieの方が安全
        localStorage.setItem('token', res.data.token)
        router.push('/')
        // this.$axios.defaults.headers.common['Authorization'] = `JWT ${res.data.token}`
        // this.$router.push('/')
      })
      .catch(() => { })
    },
    register({ commit }, authDate) {
      axiosAuth({
        method: "POST",
        url: 'log/register/',
        data: {
          username: authDate.username,
          email: authDate.email,
          password: authDate.password
        },
      })
      .then((res) => {
        console.log(res.data)
        commit('updateToken', res.data.token)
        router.push('/login')
        // this.$axios.defaults.headers.common['Authorization'] = `JWT ${res.data.token}`
        // this.$router.push('/')
      })
      .catch(() => { })
    },
    logout({ commit }) {
      commit('updateToken', null)
      localStorage.removeItem('token')
      router.push('/login')
    }
  }
});
