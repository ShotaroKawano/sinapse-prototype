import Vue from "vue";
import Router from "vue-router";
import BoardsHome from "../components/BoardsHome";
import Board from "../components/Board";
import Login from "../views/Login";
import Register from "../views/Register";
import store from '../store';
import Profile from "../components/Profile";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path:"/",
      component: BoardsHome,
      beforeEnter(to, from, next) {
        if (store.getters.token) {
          next()
        } else {
          next('/login')
        }
      }
    },
    {
      path: "/boards/:id",
      component: Board,
      beforeEnter(to, from, next) {
        if (store.getters.token) {
          next()
        } else {
          next('/login')
        }
      }
    },
    { path: "/search", component: BoardsHome },
    {
      path: "/login",
      component: Login,
      beforeEnter(to, from, next) {
        if (store.getters.token) {
          next('/')
        } else {
          next()
        }
      }
    },
    {
      path: "/register",
      component: Register,
      beforeEnter(to, from, next) {
        if (store.getters.token) {
          next('/')
        } else {
          next()
        }
      }
    },
    {
      path: "/profile",
      component: Profile,
    },
  ]
});
