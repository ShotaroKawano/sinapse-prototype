import Vue from 'vue';
import Vuex from 'vuex';
import axiosAuth from './auth'
import router from './router';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: null,
    userId: null,
    userName: null,
    userEmail: null,
  },
  getters: {
    token: state => state.token,
    userId: state => state.userId,
    userName: state => state.userName,
    userEmail: state => state.userEmail,
  },
  mutations: {
    updateToken(state, token) {
      state.token = token
    },
    updateUserId(state, userId) {
      state.userId = userId
    },
    updateUserName(state, userName) {
      state.userName = userName
    },
    updateUserEmail(state, userEmail) {
      state.userEmail = userEmail
    },
  },
  actions: {
    // tokenの有効期限を考慮していない
    async autoLogin({ commit }) {
      const token = localStorage.getItem('token')
      if (!token) return
      commit('updateToken', token)
    },
    login({ commit, dispatch }, authDate) {
      axiosAuth({
        method: "POST",
        url: 'auth/',
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
        dispatch('getUserInfo')
        router.push('/')
        // this.$axios.defaults.headers.common['Authorization'] = `JWT ${res.data.token}`
        // this.$router.push('/')
      })
      .catch(() => { })
    },
    register({ commit }, authDate) {
      axiosAuth({
        method: "POST",
        url: 'user/register/',
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
      commit('updateUserId', null)
      commit('updateUserName', null)
      commit('updateUserEmail', null)
      localStorage.removeItem('token')
      router.push('/login')
    },
    getUserInfo({ commit, state }) {
      // await this.dispatch('autoLogin')
      // console.log(state.token);
      if (state.token) {
        console.log(state.token);
        axiosAuth({
          method: "GET",
          url: 'user/mypage/',
          headers: {
            Authorization: `JWT ${state.token}`
          },
        })
        .then((res) => {
          // console.log('koko');
          commit('updateUserId', res.data.id)
          commit('updateUserName', res.data.username)
          commit('updateUserEmail', res.data.email)
        })
        .catch(() => { });
      }
    },
    profile({ commit }) {
      router.push('/profile')
    },
  }
});
