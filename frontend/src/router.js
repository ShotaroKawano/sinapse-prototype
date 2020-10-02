import Vue from "vue";
import Router from "vue-router";
import BoardsHome from "./components/BoardsHome";
import Board from "./components/Board";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    { path: "/", component: BoardsHome },
    { path: "/board", component: Board },
    { path: "/search", component: BoardsHome }
  ]
});
