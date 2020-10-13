<template>
  <!-- ▼▼▼▼▼ header ▼▼▼▼▼ -->
  <div id="header" class="box_header">
    <!-- <router-link to="/" id="btn" class="name_service">Sinapse</router-link> -->
    <router-link to="/" class="box_servicelogo"
      ><img
        src="@/assets/images/logos/logos_Sinapse_blue.png"
        alt="Sinapselogo"
        class="img_servicelogo"
    /></router-link>
    <!-- <a id="btn" class="name_service" href="/">Sinapse</a> -->

    <div class="box_inputsearch">
      <img
        class="icon_headerSearch"
        src="@/assets/images/icons/icons_search.png"
        alt="いいねボタン"
      />
      <input
        class="input_search"
        placeholder="キーワード、#ハッシュタグを入力..."
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
      <div class="box_headerUser">
        <img
          class="btn_headerUser"
          src="@/assets/images/userimages/user_default.jpg"
          alt="プロフィール画像"
        />
      </div>
      <div class="btn_create" @click="createBoard()">
        <p>作成</p>
      </div>
    </div>
  </div>
  <!-- ▲▲▲▲▲ header ▲▲▲▲▲ -->
</template>

<script>
// import axios from "axios";
// import Vue from "vue";
// import App from './App'

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
      const tail = "api/boards/";
      this.$axios({
        method: "POST",
        url: tail,
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
          this.$router.push("/boards/" + res.data.id);
        })
        .catch(() => {});
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
/* ▼ヘッダーの固定 */
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
  width: 50px;
  /* height: 20px; */
  display: inline-block;
  border-radius: 18px; /* 角丸       */
  font-size: 15px; /* 文字サイズ */
  text-align: center; /* 文字位置   */
  cursor: pointer; /* カーソル   */
  padding: 8px; /* 余白       */
  margin: 8px;
  background: #6f9fd0; /* 背景色     */
  color: #ffffff; /* 文字色     */
  line-height: 17px; /* 1行の高さ  */
  /* border: 2px solid #5486b9;  */
  text-decoration: none; /* テキストアンダーライン */
}
.btn_create:hover {
  background: #5486b9; /* 背景色     */
  color: #ffffff; /* 文字色     */
}

/* 必要 */
.btn_headerUser {
  width: 35px;
  height: 35px;
  margin: 8px 2px 5px 0px;
  border-radius: 20px;
  background: #ffffff;
}
/* ▲▲▲▲▲ ボタン ▲▲▲▲▲ */

/* ▼▼▼▼▼ テキスト関係 ▼▼▼▼▼ */
/* 必要 */
.input_search {
  width: 92%;
  height: 100%;
  color: #525e6a;
  font-size: 10pt; /* 文字サイズ */
  /* border: none; */
  /* padding: 10px; */
  margin: 0px 5px 0px 4px;
  border: none;
  border-radius: 20px; /* 角丸       */
}

/* 必要 */
.name_service {
  padding: 3px 10px 5px 0px;
  margin-left: 1%;
  font-size: 40px;
  /* color: #525e6a; */
  color: #5486b9;
  text-shadow: 0px 0px 10px #5486b990;
  text-decoration: none; /* テキストアンダーライン */
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
  height: 50px;
  background-color: #ffffff;
  box-shadow: 0px 1px 6px #f0f0f0;
}
.box_servicelogo{
  margin-left: 1%;
}
.img_servicelogo{
  width: 150px;
  height: 50px;
}

.box_headerUser {
  opacity: 0.8; /* 透明度を上げることで、画像の色を薄く見せる。*/
}
.box_headerUser:hover {
  opacity: 1; /* 透明度を上げることで、画像の色を薄く見せる。*/
}
.box_inputsearch {
  width: 36%;
  height: 36px;
  border-radius: 20px; /* 角丸       */
  border: solid 1px #b4bdc6;
  margin-top: 6px;
  display: flex;
}
.box_inputsearch:hover {
  box-shadow: 0px 0px 3px #5486b9;
  border: solid 1px #5486b990;
  transition-duration: 0.5s;
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
.icon_headerSearch {
  width: 14px;
  height: 14px;
  padding: 11px 0px 12px 10px;
}
/* ▲▲▲▲▲ アイコン ▲▲▲▲▲ */
</style>
