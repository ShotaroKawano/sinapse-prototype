import Vue from "vue";
import Router from "vue-router";
import BoardsHome from "./components/BoardsHome";
import Board from "./components/Board";
import Login from "./pages/Login";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    { path: "/", component: BoardsHome },
    { path: "/boards/:id", component: Board },
    { path: "/search", component: BoardsHome },
    { path: "/login", component: Login }
  ]
});
