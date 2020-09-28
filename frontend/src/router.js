import Vue from 'vue'
import Router from 'vue-router'
import BoardsHome from './components/BoardsHome'
import BoardHeader from './components/BoardHeader'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    { path: '/', component: BoardsHome },
    { path: '/board', component: BoardHeader }
  ]
})
