<template>
  <!-- ▼▼▼▼▼ header ▼▼▼▼▼ -->
  <div id="header" class="box_header">
    <router-link to="/" id="btn" class="name_service">Sinapse</router-link>
    <!-- <a id="btn" class="name_service" href="/">Sinapse</a> -->

    <div>
      <input
        class="input_search"
        placeholder="🔍キーワード、#ハッシュタグを入力..."
        type="search"
        id="q"
        @keypress.enter="onKeypressEnter"
      />
    </div>
    <!-- <div id="app">
      {{ info }}
    </div> -->

    <!-- <div v-for="post in posts" :key="post.id">
      <p>{{ post.title }}</p>
    </div> -->
    <div class="headerRightboxPosition">
      <div id="btn">
        <img
          class="btn_headerUser"
          src="@/assets/images/userimages/user00.jpg"
          alt="プロフィール画像"
        />
      </div>
      <div class="btn_create" @click="createBoard()">
        <p>✏︎ 投稿</p>
      </div>
    </div>
  </div>
  <!-- ▲▲▲▲▲ header ▲▲▲▲▲ -->
</template>

<script>
// import axios from "axios";
// import Vue from "vue";
// import App from './App'
import axios from "axios";

export default {
  name: "Header",
  methods: {
    onKeypressEnter: function () {
      // ↓↓↓検索ワード=qを取得
      var q = document.getElementById("q").value;

      if (q === null || q === "") {
        // 何もしない
        // console.log("returnKey押下：検索ワードがnullです");
      } else {
        // console.log("returnKey押下：検索ワードは{ " + q + " }です");

        // ページ遷移する
        this.$router.push("/search?q=" + q);
        // location.href = "http://localhost:8080/search?q=" + q;
      }
    },
    createBoard: function () {
      const URL_BASE = "http://127.0.0.1:8000/api/boards/";
      // const URL_BASE = "http://127.0.0.1:8000/admin/api/board/add/"
      axios({
        method: "POST",
        url: URL_BASE,
        // withCredentials: true,
        data: {
          title: "タイトル",
          description: "ディスクリプション",
          thumbnail: "12345",
          url_tail: "12345",
          is_published: true,
          user_id: 1,
          // "tagList": [ "気候変動", "地球温暖化", "自然電力" ]
          // tagList: this.convertTaglistToTags
        },
      })
        .then((res) => {
          console.log("koko");
          console.dir(res.data);
          this.$router.push("/boards/" + res.data.id);
        })
        .catch((err) => {
          console.log("ERROR!! occurred in Backend.");
          console.log(err);
        });
    },
  },
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
/* ヘッダーの固定 */
/* #header {
  position: fixed;
  top: 0px;
  left: 0px;
} */
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
.headerRightboxPosition {
  display: flex;
  margin-right: 1%;
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
  width: 500px;
  height: 40px;
  border-radius: 20px; /* 角丸       */
  font-size: 10pt; /* 文字サイズ */
  /* border: none; */
  border: solid 1px #87929d;
  padding: 10px;
  margin: 10px;
}

/* 必要 */
.name_service {
  font-size: 40px;
  /* color: #525e6a; */
  color: #5486b9;
  text-shadow: 0px 0px 10px #5486b990;
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
  position: absolute; /* ヘッダーの固定 */
  z-index: 10;
  top: 0px; /* 位置(上0px) */
  left: 0px; /* 位置(右0px) */
  display: flex;
  justify-content: space-between;
  width: 100%;
  height: 60px;
  background-color: #ffffff;
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
