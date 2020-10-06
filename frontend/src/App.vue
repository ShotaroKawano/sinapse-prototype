<template>
  <div class="body">
    <Header></Header>
    <router-view></router-view>
    <!-- <BoardHeader></BoardHeader> -->
  </div>
</template>

<script>
// import * as d3 from "d3";
// import { roundTo20 } from "../utils/math";
// scriptタグでないと機能しないのか？
import './assets/css/reset.css';
import Header from "./components/Header"

export default {
  components: {
    Header,
  }
}
</script>
