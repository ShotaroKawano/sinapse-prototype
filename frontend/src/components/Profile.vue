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
          内藤迅
          </div> 
          <div class="box_UserEmail">
          jin@jin.com
          </div> 
        </div> 
      </div>
    </div>
    <!-- ▲▲▲▲▲ 新boards ▲▲▲▲▲ -->
  </div>
</template>

<script>
import Header from "./Header"

export default {
  name: "Profile",

  components: {
    Header,
  },

  methods: {
  },
  
  computed: {
  },

  watch: {
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
.btn_boardsUser {
  /* 必要 */
  width: 38px;
  height: 38px;
  border-radius: 25px;
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
