<template>
      <!-- ▼▼▼▼▼ header ▼▼▼▼▼ -->
    <div id="header" class="box_header" style="position: absolute">
      <a id="btn" class="name_service" href="login.html">Sinapse</a>
      <input
        type="search"
        class="input_search"
        placeholder="🔍キーワード、#ハッシュタグを入力..."
      />
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
export default {
  name: 'Header'
}
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
#btn:hover {
  opacity: 0.8; /* 透明度を上げることで、画像の色を薄く見せる。*/
  cursor: pointer; /* リンクをホバーしたときのカーソルにする。*/
}

.btn_login {
  width: 100px;
  height: 20px;
  margin: 50px 150px 15px 150px;
  display: inline-block;
  border-radius: 5px; /* 角丸       */
  font-size: 12pt; /* 文字サイズ */
  text-align: center; /* 文字位置   */
  cursor: pointer; /* カーソル   */
  padding: 10px; /* 余白       */
  background: #525e6a; /* 背景色     */
  color: #ffffff; /* 文字色     */
  line-height: 1em; /* 1行の高さ  */
  border: 2px solid #525e6a; /* 枠の指定 */
  text-decoration: none; /* テキストアンダーライン */
}
.btn_login:hover {
  color: #525e6a; /* 背景色     */
  background: #ffffff; /* 文字色     */
}

.btn_sns {
  width: 400px;
  height: 20px;
  border-radius: 5px; /* 角丸       */
  font-size: 10pt; /* 文字サイズ */
  text-align: center; /* 文字位置   */
  cursor: pointer; /* カーソル   */
  padding: 10px 0px; /* 余白       */
  color: #ffffff; /* 文字色     */
  border: none; /* 枠の指定 */
}

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
  background: #525e6a; /* 背景色     */
  color: #ffffff; /* 文字色     */
  line-height: 1em; /* 1行の高さ  */
  border: 2px solid #525e6a; /* 枠の指定 */
  text-decoration: none; /* テキストアンダーライン */
}
.btn_create:hover {
  color: #525e6a; /* 背景色     */
  background: #ffffff; /* 文字色     */
}
.btn_headerUser {
  width: 50px;
  height: 50px;
  margin: 5px;
  border-radius: 25px;
  background: #ffffff;
}
.btn_boardsUser {
  width: 44px;
  height: 44px;
  border-radius: 25px;
}
/* ▲▲▲▲▲ ボタン ▲▲▲▲▲ */

/* ▼▼▼▼▼ テキスト関係 ▼▼▼▼▼ */
h2.indexTitle {
  font-size: 24px;
  line-height: 32px;
  padding-bottom: 4px;
  color: #525e6a;
  font-weight: bold;
}
p.indexSubheading {
  font-size: 14px;
  line-height: 20px;
  padding-bottom: 14px;
  color: #87929d;
}
p.indexHashtag {
  font-size: 16px;
  color: #b4bdc6;
}
p.indexHashtag {
  font-size: 16px;
  color: #b4bdc6;
}
p.indexUsername {
  font-size: 18px;
  color: #87929d;
}
p.indexHashtag {
  font-size: 16px;
  color: #b4bdc6;
}
p.indexCreatdate {
  font-size: 14px;
  color: #b4bdc6;
}
.login_passInfo {
  font-size: 14px;
  color: #b4bdc6;
}
.login_signupInfo {
  font-size: 14px;
  color: #b4bdc6;
  font-weight: bold;
}
.input_login {
  width: 400px;
  height: 40px;
  border-radius: 5px; /* 角丸       */
  font-size: 10pt; /* 文字サイズ */
  border: solid 1px #87929d; /* 枠の指定 */
}
.input_search {
  width: 400px;
  height: 40px;
  border-radius: 20px; /* 角丸       */
  font-size: 10pt; /* 文字サイズ */
  border: none; /* 枠の指定 */
  padding: 10px;
  margin: 10px;
}

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
.box_header {
  position: fixed; /* ヘッダーの固定 */
  top: 0px; /* 位置(上0px) */
  left: 0px; /* 位置(右0px) */
  display: flex;
  width: 100%;
  height: 60px;
  background-color: #e1e6eb;
}
.box_hashtag {
  width: 90px;
  margin: 7px;
  padding: 10px 20px;
  text-align: center; /* 文字位置   */
  border-radius: 5px; /* 角丸       */
  color: #ffffff;
  background: #87929d; /* 枠の指定 */
}
/* .box_indexBoards {
  width: 700px;
  background: #ffffff;
  display: flex;
  margin: 10px;
  border-radius: 10px;
}
.box_indexBoards:hover {
  box-shadow: 0px 0px 6px #5486b9;
} */
.box_boardsUser {
  width: 200px;
  height: 54px;
  margin: 10px;
  border-radius: 27px;
  display: flex;
  background: #87929d;
}

.box_boardsUsercontents {
  margin: 10px;
  text-align: center;
  color: #e1e6eb;
  font-size: 14px;
}

.box_boards1set {
  width: 745px;
  height: 290px;
  background: #ffffff;
  display: flex;
  border-radius: 10px;
  margin: 20px auto;
}
.box_boards1set:hover {
  box-shadow: 0px 0px 10px #5486b980;
}
.box_indexSns {
  margin: 10px;
  height: 370px;
  display: flex;
  flex-flow: column;
  justify-content: space-around;
}
.box_indexSns2 {
  margin: 16px 30px 0px 0px;
  height: 50px;
  display: flex;
  justify-content: space-around;
}
.box_indexSnscontents {
  margin: 10px;
  text-align: center;
  color: #b4bdc6;
}
/* ▲▲▲▲▲ ボックス ▲▲▲▲▲ */

/* ▼▼▼▼▼ サムネイル ▼▼▼▼▼ */
.thumbnail_indexBoards {
  width: 150px;
  height: 150px;
  margin: 30px 30px 0px 0px;
  border-radius: 10px;
  border: solid 1px #e1e6eb; /* 枠の指定 */

  background-size: cover;
}

.thumbnail_indexBoards2 {
  width: 200px;
  height: 350px;
  margin: 10px;
  border-radius: 10px;
  border: solid 1px #e1e6eb; /* 枠の指定 */

  background-size: cover;
}
/* ▲▲▲▲▲ サムネイル ▲▲▲▲▲ */

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
