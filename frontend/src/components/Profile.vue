<template>
  <div>
    <Header></Header>
    <!-- ▼▼▼▼▼ 新boards ▼▼▼▼▼ -->
    <div class="ProfileWrapper">
      <div class="box_Profile0">
        <div class="box_UserImage">
          <img
          class="img_Userimage"
          src="@/assets/images/userimages/user_default.jpg"
          alt="プロフィール画像"
          />
        </div>
        <div class="box_UserProfile">
          <div class="box_UserName">
          {{ username }}
          </div>
          <div class="box_UserEmail">
          {{ email }}
          </div>
        </div>
      </div>
      <div class="box_Profile0">
        <div class="btn_logout" @click="logout">LOGOUT</div>
      </div>
    </div>
    <!-- ▲▲▲▲▲ 新boards ▲▲▲▲▲ -->
  </div>
</template>

<script>
import Header from "./Header"

export default {
  name: "Profile",

  data: function () {
    return {
      username: null,
      email: null,
      icon: null,
    }
  },

  components: {
    Header,
  },

  methods: {
    logout: function () {
      this.$store.dispatch('logout')
    },
  },

  computed: {
  },

  watch: {
  },

  created: function () {
    console.log('koko');
    this.username = this.$store.getters.userName
    this.email = this.$store.getters.userEmail
    // this.icon = this.$store.getters.userIcon
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
  /* 必要 */
  position: absolute; /* body全体を指定 */
  left: 50%; /* 親要素の半分右にずらす */
  transform: translateX(-50%); /* 要素自体の半分左にずらす */
}
.ProfileWrapper {
  padding-top: 50px;
  position: absolute;
  background-color: #ffffff;
  width: 100%;
  min-height: 100%;
  margin: 0 auto;
}
/* ▲▲▲▲▲ 表示位置 ▲▲▲▲▲ */

/* ▼▼▼▼▼ ボタン ▼▼▼▼▼ */
#btn:hover {
  /* 必要 */
  opacity: 0.8; /* 透明度を上げることで、画像の色を薄く見せる。*/
  cursor: pointer; /* リンクをホバーしたときのカーソルにする。*/
}
#btn2:hover {
  /* 必要 */
  cursor: pointer; /* リンクをホバーしたときのカーソルにする。*/
}
.btn_logout{
  width: auto;
  margin: 0 0 0 auto;
  display: inline-block;
  border-radius: 18px; /* 角丸       */
  font-size: 14px; /* 文字サイズ */
  font-weight: bold;
  text-align: center; /* 文字位置   */
  padding: 10px; /* 余白       */
  background: #f8f8f8; /* 背景色     */
  color: #525e6a; /* 文字色     */
  line-height: 17px; /* 1行の高さ  */
  opacity: .6; /* 透明度を上げることで、画像の色を薄く見せる。*/
}
.btn_logout:hover {
  background: #f8f8f8; /* 背景色     */
  opacity: .8; /* 透明度を上げることで、画像の色を薄く見せる。*/
  cursor: pointer; /* リンクをホバーしたときのカーソルにする。*/
}
/* ▲▲▲▲▲ ボタン ▲▲▲▲▲ */

/* ▼▼▼▼▼ テキスト関係 ▼▼▼▼▼ */

/* ▲▲▲▲▲ テキスト関係 ▲▲▲▲▲ */

/* ▼▼▼▼▼ ボックス ▼▼▼▼▼ */
.box_Profile0{
  max-width: 50%;
  margin: 0 auto;
  margin-top: 50px;
  display: flex;
}
.box_Userimage{
}
.box_UserProfile{
  margin: auto 0;
  margin-left: 14px;
}
.box_UserName{
  font-size: 30px;
  color: #525e6a;
}
.box_UserEmail{
  margin-top: 8px;
  font-size: 20px;
  color: #525e6a;
}
/* ▲▲▲▲▲ ボックス ▲▲▲▲▲ */

/* ▼▼▼▼▼ サムネイル ▼▼▼▼▼ */

/* ▲▲▲▲▲ サムネイル ▲▲▲▲▲ */

/* ▼▼▼▼▼ アイコン ▼▼▼▼▼ */
.img_Userimage{
  width: 100px;
  border-radius: 50px;
}
/* ▲▲▲▲▲ アイコン ▲▲▲▲▲ */
</style>
