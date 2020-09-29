<template>
  <!-- ▼▼▼▼▼ header ▼▼▼▼▼ -->
  <div id="header" class="box_header" style="position: absolute">
    <a id="btn" class="name_service" href="login.html">Sinapse</a>
    <!-- <input
        type="search"
        class="input_search"
        placeholder="🔍キーワード、#ハッシュタグを入力..."
      /> -->

    <div>
      <input
        class="input_search"
        placeholder="🔍キーワード、#ハッシュタグを入力..."
        type="search"
        v-model="search"
        @keypress.enter="onKeypressEnter"
      />
    </div>

    <div v-for="post in posts" :key="post.id">
      <p>{{ post.title }}</p>
    </div>
    <div id="btn">
      <img
        class="btn_headerUser"
        src="@/assets/images/userimages/user00.jpg"
        alt="プロフィール画像"
      />
    </div>
    <div class="btn_create">
      <p>✏︎ 投稿</p>
    </div>
  </div>
  <!-- ▲▲▲▲▲ header ▲▲▲▲▲ -->
</template>

<script>
import axios from "axios";

export default {
  name: "Header",
  methods: {
    onKeypressEnter: function() {
      console.log("returnKeyが押されました");
      const URL_BASE =
        "https://e1bca722-eae2-4b02-bb29-f560fd850314.mock.pstmn.io/search?q=気候変動";
      return axios({
        method: "GET",
        url: URL_BASE
      })
        .then(res => {
          console.dir(res.data);
          console.log(res.data.board_id);
        })
        .catch(err => {
          console.log("ERROR!! occurred in Backend.");
          console.log(err);
        });
    }
  }
};
</script>

<style scoped>
/* ▼▼▼▼▼ 叩き台 ▼▼▼▼▼ */
.pfBox {
  background-color: #00234608;
}
.pfBox2 {
  background: #35353510;
  padding: 5px;
  margin: 5px;
}
/* ▲▲▲▲▲ 叩き台 ▲▲▲▲▲ */

/* ▼▼▼▼▼ 表示位置 ▼▼▼▼▼ */
/* 必要 */
#header {
  position: fixed; /* ヘッダーの固定 */
  top: 0px; /* 位置(上0px) */
  left: 0px; /* 位置(右0px) */
}
.center_objecto {
  position: absolute; /* body全体を指定 */
  top: 50%; /* 親要素の半分下にずらす */
  left: 50%; /* 親要素の半分右にずらす */
  transform: translateY(-50%) translateX(-50%); /* 要素自体の半分、上と左にずらす */
}
.center_ual {
  position: absolute; /* body全体を指定 */
  top: 50%; /* 親要素の半分下にずらす */
  transform: translateY(-50%); /* 要素自体の半分上にずらす */
}
.center_lar {
  position: absolute; /* body全体を指定 */
  left: 50%; /* 親要素の半分右にずらす */
  transform: translateX(-50%); /* 要素自体の半分左にずらす */
}
/* ▲▲▲▲▲ 表示位置 ▲▲▲▲▲ */

/* ▼▼▼▼▼ ボタン ▼▼▼▼▼ */
/* 必要 */
#btn:hover {
  opacity: 0.8; /* 透明度を上げることで、画像の色を薄く見せる。*/
  cursor: pointer; /* リンクをホバーしたときのカーソルにする。*/
}
/* 必要 */
.btn_create {
  width: 80px;
  height: 20px;
  display: inline-block;
  border-radius: 10px; /* 角丸       */
  font-size: 18px; /* 文字サイズ */
  text-align: center; /* 文字位置   */
  cursor: pointer; /* カーソル   */
  padding: 8px; /* 余白       */
  margin: 10px;
  background: #5486b9; /* 背景色     */
  color: #ffffff; /* 文字色     */
  line-height: 1em; /* 1行の高さ  */
  border: 2px solid #5486b9; /* 枠の指定 */
  text-decoration: none; /* テキストアンダーライン */
}
.btn_create:hover {
  color: #5486b9; /* 背景色     */
  background: #ffffff; /* 文字色     */
}

/* 必要 */
.btn_headerUser {
  width: 50px;
  height: 50px;
  margin: 5px;
  border-radius: 25px;
  background: #ffffff;
}
/* ▲▲▲▲▲ ボタン ▲▲▲▲▲ */

/* ▼▼▼▼▼ テキスト関係 ▼▼▼▼▼ */

/* 必要 */
.input_search {
  width: 400px;
  height: 40px;
  border-radius: 20px; /* 角丸       */
  font-size: 10pt; /* 文字サイズ */
  border: none; /* 枠の指定 */
  padding: 10px;
  margin: 10px;
}

/* 必要 */
.name_service {
  font-size: 40px;
  color: #525e6a;
  padding: 10px;
  text-decoration: none; /* テキストアンダーライン */
}
.name_user {
  padding: 20px 4px;
  font-size: 16px;
  color: #ffffff;
}
/* ▲▲▲▲▲ テキスト関係 ▲▲▲▲▲ */

/* ▼▼▼▼▼ ボックス ▼▼▼▼▼ */
/* 必要 */
.box_header {
  position: fixed; /* ヘッダーの固定 */
  top: 0px; /* 位置(上0px) */
  left: 0px; /* 位置(右0px) */
  display: flex;
  width: 100%;
  height: 60px;
  background-color: #e1e6eb;
}
/* ▲▲▲▲▲ ボックス ▲▲▲▲▲ */

/* ▼▼▼▼▼ アイコン ▼▼▼▼▼ */
.icon_indexBoards {
  width: 20px;
  height: 20px;
}
.icon_boardsUser {
  width: 18px;
  height: 18px;
}
/* ▲▲▲▲▲ アイコン ▲▲▲▲▲ */
</style>
