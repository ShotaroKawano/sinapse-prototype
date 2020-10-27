<template>
  <div>
    <Header></Header>
    <!-- ▼▼▼▼▼ 新boards ▼▼▼▼▼ -->
    <div class="boardsHomeWrapper">

      <!-- ▼▼▼ sideMenu ▼▼▼ -->
      <div class="box_sideMenu">
        <div class="btn_sideMenu">
          <img
            class="icon_sideMenu"
            src="@/assets/images/icons/icons_home.png"
            alt="ホームボタン"
          />
          <p>ホーム</p>
        </div>
        <div class="btn_sideMenu">
          <img
            class="icon_sideMenu"
            src="@/assets/images/icons/icons_bookmark.png"
            alt="ブックマークボタン"
          />
          <p>いいねしたボード</p>
        </div>
        <div class="btn_sideMenu">
          <img
            class="icon_sideMenu"
            src="@/assets/images/icons/icons_myboards.png"
            alt="ホームボタン"
          />
          <p>自分の投稿</p>
        </div>
      </div>
      <!-- ▲▲▲ sideMenu ▲▲▲ -->

      <div class="boardsWrapper">
        <!-- <div>
          <h1>q = {{ this.$route.query.q }}</h1>
        </div> -->
        <!-- ▼▼▼ board1set ▼▼▼ -->
        <router-link
          v-for="board in boards"
          :key="board.id"
          v-bind:to="`boards/${board.id}`"
          class="box_boards1set"
        >
          <!-- ▼▼ 概要 ▼▼ -->
          <div class="box_indexBoards">
            <div class="box_indexBoardTitleSubheading">
              <!-- ▼ タイトル ▼ -->
              <div>
                <h2 class="indexTitle">
                  {{ board.title }}
                </h2>
              </div>
              <!-- ▼ 見出し ▼ -->
              <div>
                <p class="indexSubheading">
                  {{ board.description }}
                </p>
              </div>
            </div>
            <!-- ▼ ハッシュタグ ▼ -->
            <!-- <div id="tags" class="box_indexHashtag"> -->
              <!-- <ul v-for="tag of limitCount" :key="tag.name">
                <li>
                  <p id="btn" class="indexHashtag">{{ tag.name }}</p>
                </li>
              </ul> -->
              <!-- <div
                id="btn"
                v-for="tagWrapper in board.board_tags"
                :key="tagWrapper.tag.id"
              >
                <p class="indexHashtag">#{{ tagWrapper.tag.name }}</p>
              </div>
            </div> -->

            <!-- ▼▼ プロフボタン ▼▼ -->
            <div class="box_UserAndCreatdate">
              <div id="btn">
                <img
                  v-if="board.user.user_icon"
                  class="btn_boardsUser"
                  :src="board.user.user_icon"
                />
                <img
                  v-else
                  class="btn_boardsUser"
                  src="@/assets/images/userimages/user_default.jpg"
                />
              </div>
              <div class="box_NameAndCreatdate">
                <div>
                  <p class="indexUsername">{{ board.user.username }}</p>
                </div>
                <div>
                  <p class="indexCreatdate">{{ getNowDateWithString(board.updated_at) }}</p>
                </div>
              </div>
              <!-- ▼▼ SNS ▼▼ -->
              <div class="box_indexSns">
                <div
                  @click.stop.prevent="addLike(board.id)"
                  id="btn2"
                  class="box_indexSnscontents"
                >
                  <img
                    class="icon_indexBoards"
                    src="@/assets/images/icons/icons_like.png"
                    alt="いいねボタン"
                  />
                  <!-- <div>{{ board.comments }}</div> -->
                  <div class="box_indexBoardsText">{{ board.like_count }}</div>
                </div>
                <!-- <div id="btn2" class="box_indexSnscontents">
                  <img
                    class="icon_indexBoards"
                    src="@/assets/images/icons/icons_comment.png"
                    alt="コメントボタン"
                  />
                  <div>777</div>
                </div> -->
              </div>
            </div>
          </div>
          <div class="box_indexThumbnail">
            <!-- ▼▼ サムネ画像 ▼▼ -->
            <!-- <div
              class="thumbnail_indexBoards"
              :style="{ backgroundImage: 'url(' + board.thumbnail + ')' }"
            ></div> -->
            <img
              v-if="board.thumbnail"
              class="thumbnail_indexBoards"
              :src=" board.thumbnail "
              onerror="this.onerror = null; this.src='';"
              border="0"
            >
          </div>
        </router-link>
      </div>
    </div>
    <!-- ▲▲▲ boards1set ▲▲▲ -->
    <!-- ▲▲▲▲▲ 新boards ▲▲▲▲▲ -->
  </div>
</template>

<script>
import Header from "./Header"

export default {
  name: "BoardsHome",
  // watch: {
  //   $route() {
  //     console.log("ページ遷移");
  //   }
  // },
  components: {
    Header,
  },
  methods: {
    // いいねを外した場合も要実装
    addLike(boardId) {
      this.$axios({
        method: "POST",
        url: "api/likes/",
        // headers: {
        //   Authorization: `JWT ${this.token}`
        // },
        data: {
          board: boardId,
          user: this.$store.getters.userId
        }
      })
      .then((res) => {
        this.boards.forEach(board => {
          if (res.data.board === board.id) {
            board.like_count++
          }
        });
      })
      .catch(() => {});
    }
    // search: function () {
    //   // console.log('koko');
    //   // const URL_BASE = "http://127.0.0.1:8000/api/boards?title=" + "気候変動";
    //   // console.log("生成されたURL：" + URL_BASE);
    //   this.$axios({
    //     method: "GET",
    //     // TODO: 気候変動を可変に
    //     url: "api/boards?title=" + "気候変動",
    //     headers: {
    //       Authorization: `JWT ${this.token}`
    //     },
    //   })
    //   .then((res) => {
    //     this.boards = res.data.board_list;
    //   })
    //   .catch(() => {});
    // },
  },
  data: function () {
    return {
      boards: [
      //   {
      //     id: 1,
      //     title: "気候変動の影響による日本の危険性と今できること",
      //     description:
      //       "気候変動により人命にもっとも危機が及ぶ可能性が高い国は日本である。気候変動を抑える対策として、我々がもっとも手軽で効果的なことは電気会社を切り替えることだあああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ。",
      //     thunbnail: require("@/assets/images/treediagram.png"),
      //     // tags: [
      //     //   { name: "#気候変動" },
      //     //   { name: "#地球温暖化" },
      //     //   { name: "#自然電力" }
      //     // ],
      //     board_tags: [
      //       {
      //         tag: { id: 1, name: "気候変動" },
      //         tag: { id: 2, name: "地球温暖化" },
      //         tag: { id: 3, name: "自然電力" },
      //       },
      //       // { id: 2, name: "地球温暖化" },
      //       // { id: 3, name: "自然電力" }
      //     ],
      //     user: {
      //       user_name: "川野 翔太郎",
      //       user_icon: require("@/assets/images/userimages/user00.jpg"),
      //     },
      //     updated_at: "2020/09/20",
      //     comment_count: 123,
      //     like_count: 456,
      //   },
        // {
        //   id: 2,
        //   title: "気候変動の影響による日本の危険性と今できること",
        //   description:
        //     "気候変動により人命にもっとも危機が及ぶ可能性が高い国は日本である。気候変動を抑える対策として、我々がもっとも手軽で効果的なことは電気会社を切り替えることだ。",
        //   thunbnail: "aa",
        //   // tags: [
        //   //   { name: "#気候変動" },
        //   //   { name: "#地球温暖化" },
        //   //   { name: "#自然電力" }
        //   // ],
        //   board_tags: [
        //     {
        //       tag: { id: 1, name: "気候変動" },
        //       tag: { id: 2, name: "地球温暖化" },
        //       tag: { id: 3, name: "自然電力" },
        //     },
        //   ],
        //   user: {
        //     user_name: "川野 翔太郎",
        //     user_icon: "user00",
        //   },
        //   updated_at: "2020/09/20",
        //   comment_count: 123,
        //   like_count: 456,
        // },
        // {
        //   id: 3,
        //   title: "気候変動の影響による日本の危険性と今できること",
        //   description:
        //     "気候変動により人命にもっとも危機が及ぶ可能性が高い国は日本である。気候変動を抑える対策として、我々がもっとも手軽で効果的なことは電気会社を切り替えることだ。",
        //   board_thunbnail: "aa",
        //   // tags: [
        //   //   { name: "#気候変動" },
        //   //   { name: "#地球温暖化" },
        //   //   { name: "#自然電力" }
        //   // ],
        //   tag_list: [
        //     {
        //       tag: { id: 1, name: "気候変動" },
        //       tag: { id: 2, name: "地球温暖化" },
        //       tag: { id: 3, name: "自然電力" },
        //     },
        //   ],
        //   user: {
        //     user_name: "川野 翔太郎",
        //     user_icon: "user00",
        //   },
        //   updated_at: "2020/09/20",
        //   comment_count: 123,
        //   like_count: 456,
        // },
      ],
    };
  },
  computed: {
    token() {
      return this.$store.getters.token
    },
    // limitCount() {
    //   return this.tags.slice(0, 3);
    // },
    getNowDateWithString() {
      return function(date) {
        var dt = new Date(date);
        var y = dt.getFullYear();
        var m = ("00" + (dt.getMonth() + 1)).slice(-2);
        var d = ("00" + dt.getDate()).slice(-2);
        var result = y + "/" + m + "/" + d;
        return result;
      }
    }
  },
  watch: {
    $route() {
      // console.log('route');
      // console.log(this.$route);
      // console.log(this.$route.query.q);
      let tail;
      if (this.$route.path === "/search") {
        tail =
          "api/boards?search=" + this.$route.query.q;
      } else {
        tail = "api/boards";
      }
      this.$axios({
        method: "GET",
        url: tail,
        headers: {
          Authorization: `JWT ${this.token}`
        },
      })
        .then((res) => {
          this.boards = res.data;
        })
        .catch(() => {});
    },
  },
  created: function () {
    this.$axios({
      method: "GET",
      url: 'api/boards',
      headers: {
        Authorization: `JWT ${this.token}`
      },
    })
    .then((res) => {
      this.boards = res.data;
    })
    .catch(() => {});
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
.boardsHomeWrapper {
  /* position: absolute; */
  display: flex;
  /* position: absolute; */
  /* margin-top: 40px; */
  padding-top: 50px;
}
.boardsWrapper{
  z-index: 0;
  position: absolute;
  background-color: #f0f0f0;
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
.btn_sideMenu{
  display: flex;
  /* width: 100％; */
  /* font-weight: bold; */
  /* background-color: #ffffff50; */
  padding: 14px 0px 14px 14px;
  margin-bottom: 20px;
  margin-left: 10%;
  border-radius: 30px;
  /* opacity: 0.8; */
  cursor: pointer;
}
.btn_sideMenu:hover {
  /* width: 25px; */
  background-color: #ffffff70;
  /* opacity: 1; */
}
.btn_sideMenu > p{
  color: #525e6a;
  font-size: 18px;
  margin: auto 0;
}

/* ▲▲▲▲▲ ボタン ▲▲▲▲▲ */

/* ▼▼▼▼▼ テキスト関係 ▼▼▼▼▼ */
h2.indexTitle {
  /* 必要 */
  margin: 0px 0px 14px 0px;
  font-size: 24px;
  line-height: 32px;
  color: #525e6a;
  font-weight: bold;
  overflow-wrap:break-word;
  display: -webkit-box;
  overflow: hidden;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}
p.indexSubheading {
  /* 必要 */
  margin: 10px 0px 0px 0px;
  max-height: 80px;
  font-size: 14px;
  line-height: 20px;
  color: #525e6a;
  overflow-wrap:break-word;
  display: -webkit-box;
  overflow: hidden;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
}
p.indexHashtag {
  /* 必要 */
  font-size: 16px;
  color: #b4bdc6;
}
p.indexUsername {
  /* 必要 */
  font-size: 18px;
  color: #87929d;
}
p.indexCreatdate {
  /* 必要 */
  padding-top: 4px;
  font-size: 14px;
  color: #b4bdc6;
}
/* ▲▲▲▲▲ テキスト関係 ▲▲▲▲▲ */

/* ▼▼▼▼▼ ボックス ▼▼▼▼▼ */
.box_sideMenu{
  z-index: 1;
  position: absolute;
  width: 16%;
  max-width: 240px;
  margin-top: 30px;
  margin-left: 0%;
}
.box_boards1set {
  /* 必要 */
  width: 745px;
  margin: 30px auto 10px auto;
  padding: 20px 0px 20px 30px;
  /* height: 290px; */
  background: #ffffff;
  display: flex;
  border-radius: 10px;
  text-decoration: none;
}
.box_boards1set:hover {
  /* 必要 */
  box-shadow: 0px 0px 10px #5486b990;
}

.box_indexBoardTitleSubheading{
  min-height: 88px;
  padding-bottom: 20px;
}

.box_indexSns {
  /* 必要 */
  /* padding-right: 30px; */
  margin: 0px 10px 0px auto;
  height: 38px;
  display: flex;
  justify-content: space-around;
}
.box_indexSnscontents {
  /* 必要 */
  /* margin: auto 0; */
  margin: auto 0;
  flood-color: #b4bdc6;
  opacity: 0.6;
  display: flex;
}
.box_indexSnscontents:hover{
  opacity: 1;
}

.box_indexBoards {
  margin: 0px 20px 0px 0px;
  width: 100%;
}
.box_indexBoardsText{
  text-align: center;
  color: #b4bdc6;
  font-size: 16px;
  margin-left: 4px;
  padding-top: 4px;
}

.box_indexHashtag {
  display: flex;
  flex-wrap: wrap;
  /* height: 16px; */
  margin: 14px 10px 12px 10px;
}
.box_UserAndCreatdate {
  display: flex;
  padding: 0px 0px 0px 10px;
  margin: auto 0 0 0;
}
.box_NameAndCreatdate {
  padding-left: 12px;
}

.box_indexThumbnail{
  /* max-width: 150px;
  max-height: 150px; */
  /* width: 150px;
  height: 150px; */
  border-radius: 10px;
}
.box_indexThumbnail img {
  object-fit: cover;
}
/* ▲▲▲▲▲ ボックス ▲▲▲▲▲ */

/* ▼▼▼▼▼ サムネイル ▼▼▼▼▼ */
.thumbnail_indexBoards {
  /* 必要 */
  /* max-width: 150px;
  max-height: 150px; */
  /* width: 150px;
  height: 150px; */
  border-radius: 10px;
  margin: 0px 20px 0px 0px;
  /* border: solid 1px #e1e6eb; */
  /* background-image: url(../assets/images/icons/noimage.jpg); */
  /* 画像を常に天地左右の中央に配置 */
  background-position: center center;

  /* 画像をタイル状に繰り返し表示しない */
  background-repeat: no-repeat;

  /* コンテンツの高さが画像の高さより大きい時、動かないように固定 */
  background-attachment: fixed;

  /* 表示するコンテナの大きさに基づいて、背景画像を調整 */
  background-size: cover;
  background-color: #f8f8f8;
}
.box_indexThumbnail > img {
  max-width: 170px;
  max-height: 150px;
  /* object-fit: contain; */
}
/* ▲▲▲▲▲ サムネイル ▲▲▲▲▲ */

/* ▼▼▼▼▼ アイコン ▼▼▼▼▼ */
.icon_indexBoards {
  /* 必要 */
  width: 20px;
  height: 20px;
}
.icon_sideMenu{
  max-width: 30px;
  max-height: 28px;
  margin-right: 10px;
}
/* ▲▲▲▲▲ アイコン ▲▲▲▲▲ */
</style>
