<template>
  <!-- ▼▼▼▼▼ 新boards ▼▼▼▼▼ -->
  <div class="center_lar boardsWrapper">
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
        <!-- ▼ ハッシュタグ ▼ -->
        <div id="tags" class="box_indexHashtag">
          <!-- <ul v-for="tag of limitCount" :key="tag.name">
            <li>
              <p id="btn" class="indexHashtag">{{ tag.name }}</p>
            </li>
          </ul> -->
          <div
            id="btn"
            v-for="tagWrapper in board.board_tags"
            :key="tagWrapper.tag.id"
          >
            <p class="indexHashtag">#{{ tagWrapper.tag.name }}</p>
          </div>
        </div>

        <!-- ▼▼ プロフボタン ▼▼ -->
        <div class="box_UserAndCreatdate">
          <div id="btn">
            <img
              class="btn_boardsUser"
              src="@/assets/images/userimages/user00.jpg"
              alt="プロフィール画像"
            />
          </div>
          <div class="box_NameAndCreatdate">
            <div>
              <p class="indexUsername">{{ board.user.username }}</p>
            </div>
            <div>
              <p class="indexCreatdate">{{ board.updated_at }}</p>
            </div>
          </div>
        </div>
      </div>
      <div>
        <!-- ▼▼ サムネ画像 ▼▼ -->
        <div class="thumbnail_indexBoards"></div>
        <!-- ▼▼ SNS ▼▼ -->
        <div class="box_indexSns2">
          <div id="btn" class="box_indexSnscontents">
            <img
              class="icon_indexBoards"
              src="@/assets/images/icons/icons_like.png"
              alt="いいねボタン"
            />
            <div>{{ board.comments }}</div>
          </div>
          <div id="btn" class="box_indexSnscontents">
            <img
              class="icon_indexBoards"
              src="@/assets/images/icons/icons_comment.png"
              alt="コメントボタン"
            />
            <div>{{ board.likes }}</div>
          </div>
        </div>
      </div>
    </router-link>
  </div>
  <!-- ▲▲▲ boards1set ▲▲▲ -->
  <!-- ▲▲▲▲▲ 新boards ▲▲▲▲▲ -->
</template>

<script>
import axios from "axios";

export default {
  name: "BoardsHome",
  // watch: {
  //   $route() {
  //     console.log("ページ遷移");
  //   }
  // },
  methods: {
    search: function () {
      // console.log('koko');
      const URL_BASE = "http://127.0.0.1:8000/api/boards?title=" + "気候変動";
      // console.log("生成されたURL：" + URL_BASE);
      return axios({
        method: "GET",
        url: URL_BASE,
      })
        .then((res) => {
          // console.dir(res.data);
          // console.log(res.data.board_list);
          this.boards = res.data.board_list;
        })
        .catch((err) => {
          console.log("ERROR!! occurred in Backend.");
          console.log(err);
        });
    },
  },
  data: function () {
    return {
      boards: [
        {
          id: 1,
          title: "気候変動の影響による日本の危険性と今できること",
          description:
            "気候変動により人命にもっとも危機が及ぶ可能性が高い国は日本である。気候変動を抑える対策として、我々がもっとも手軽で効果的なことは電気会社を切り替えることだあああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ。",
          thunbnail: "aa",
          // tags: [
          //   { name: "#気候変動" },
          //   { name: "#地球温暖化" },
          //   { name: "#自然電力" }
          // ],
          board_tags: [
            {
              tag: { id: 1, name: "気候変動" },
              tag: { id: 2, name: "地球温暖化" },
              tag: { id: 3, name: "自然電力" },
            },
            // { id: 2, name: "地球温暖化" },
            // { id: 3, name: "自然電力" }
          ],
          user: {
            user_name: "川野 翔太郎",
            user_icon: "user00",
          },
          updated_at: "2020/09/20",
          comment_count: 123,
          like_count: 456,
        },
        {
          id: 2,
          title: "気候変動の影響による日本の危険性と今できること",
          description:
            "気候変動により人命にもっとも危機が及ぶ可能性が高い国は日本である。気候変動を抑える対策として、我々がもっとも手軽で効果的なことは電気会社を切り替えることだ。",
          thunbnail: "aa",
          // tags: [
          //   { name: "#気候変動" },
          //   { name: "#地球温暖化" },
          //   { name: "#自然電力" }
          // ],
          board_tags: [
            {
              tag: { id: 1, name: "気候変動" },
              tag: { id: 2, name: "地球温暖化" },
              tag: { id: 3, name: "自然電力" },
            },
          ],
          user: {
            user_name: "川野 翔太郎",
            user_icon: "user00",
          },
          updated_at: "2020/09/20",
          comment_count: 123,
          like_count: 456,
        },
        {
          id: 3,
          title: "気候変動の影響による日本の危険性と今できること",
          description:
            "気候変動により人命にもっとも危機が及ぶ可能性が高い国は日本である。気候変動を抑える対策として、我々がもっとも手軽で効果的なことは電気会社を切り替えることだ。",
          board_thunbnail: "aa",
          // tags: [
          //   { name: "#気候変動" },
          //   { name: "#地球温暖化" },
          //   { name: "#自然電力" }
          // ],
          tag_list: [
            {
              tag: { id: 1, name: "気候変動" },
              tag: { id: 2, name: "地球温暖化" },
              tag: { id: 3, name: "自然電力" },
            },
          ],
          user: {
            user_name: "川野 翔太郎",
            user_icon: "user00",
          },
          updated_at: "2020/09/20",
          comment_count: 123,
          like_count: 456,
        },
      ],
    };
  },
  computed: {
    limitCount() {
      return this.tags.slice(0, 3);
    },
  },
  watch: {
    $route() {
      // console.log('route');
      // console.log(this.$route);
      // console.log(this.$route.query.q);
      let URL_BASE;
      if (this.$route.path === "/search") {
        URL_BASE =
          "http://127.0.0.1:8000/api/boards?title=" + this.$route.query.q;
      } else {
        URL_BASE = "http://127.0.0.1:8000/api/boards";
      }
      axios({
        method: "GET",
        url: URL_BASE,
      })
        .then((res) => {
          // console.log(res.data);
          this.boards = res.data;
        })
        .catch((err) => {
          console.log("ERROR!! occurred in Backend.");
          console.log(err);
        });
    },
  },
  created: function () {
    // console.log('route');
    // console.log(this.$route);
    // console.log(this.$route.query.q);
    const URL_BASE = "http://127.0.0.1:8000/api/boards";
    axios({
      method: "GET",
      url: URL_BASE,
    })
      .then((res) => {
        console.log(res.data);
        this.boards = res.data;
      })
      .catch((err) => {
        console.log("ERROR!! occurred in Backend.");
        console.log(err);
      });
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
  margin-top: 60px;
}
.boardsWrapper {
  position: absolute;
  margin-top: 50px;
  background-color: #f0f0f0;
  width: 100%;
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
  width: 44px;
  height: 44px;
  border-radius: 25px;
}
/* ▲▲▲▲▲ ボタン ▲▲▲▲▲ */

/* ▼▼▼▼▼ テキスト関係 ▼▼▼▼▼ */
h2.indexTitle {
  /* 必要 */
  margin: 10px;
  font-size: 24px;
  line-height: 32px;
  padding-bottom: 4px;
  color: #525e6a;
  font-weight: bold;
}
p.indexSubheading {
  /* 必要 */
  margin: 10px 10px 0px 10px;
  height: 80px;
  font-size: 14px;
  line-height: 20px;
  color: #87929d;
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
  padding-top: 4px;
  font-size: 18px;
  color: #87929d;
}
p.indexCreatdate {
  /* 必要 */
  padding-top: 6px;
  font-size: 14px;
  color: #b4bdc6;
}
/* ▲▲▲▲▲ テキスト関係 ▲▲▲▲▲ */

/* ▼▼▼▼▼ ボックス ▼▼▼▼▼ */
.box_boards1set {
  /* 必要 */
  width: 745px;
  height: 290px;
  background: #ffffff;
  display: flex;
  border-radius: 10px;
  margin: 30px auto 10px auto;
  text-decoration: none;
}
.box_boards1set:hover {
  /* 必要 */
  box-shadow: 0px 0px 10px #5486b990;
}
.box_indexSns2 {
  /* 必要 */
  margin: 16px 30px 0px 0px;
  height: 50px;
  display: flex;
  justify-content: space-around;
}
.box_indexSnscontents {
  /* 必要 */
  margin: 10px;
  text-align: center;
  color: #b4bdc6;
}
.box_indexBoards {
  margin: 20px 20px 30px 30px;
  width: 505px;
}
.box_indexHashtag {
  display: flex;
  flex-wrap: wrap;
  height: 16px;
  margin: 14px 10px 12px 10px;
}
.box_UserAndCreatdate {
  display: flex;
  margin: 0px 0px 0px 10px;
}
.box_NameAndCreatdate {
  padding-left: 12px;
}
/* ▲▲▲▲▲ ボックス ▲▲▲▲▲ */

/* ▼▼▼▼▼ サムネイル ▼▼▼▼▼ */
.thumbnail_indexBoards {
  /* 必要 */
  width: 150px;
  height: 150px;
  margin: 30px 30px 0px 0px;
  border-radius: 10px;
  border: solid 1px #e1e6eb; /* 枠の指定 */
  background-image: url(../assets/images/treediagram.png);
  background-size: cover;
}
/* ▲▲▲▲▲ サムネイル ▲▲▲▲▲ */

/* ▼▼▼▼▼ アイコン ▼▼▼▼▼ */
.icon_indexBoards {
  /* 必要 */
  width: 20px;
  height: 20px;
}
/* ▲▲▲▲▲ アイコン ▲▲▲▲▲ */
</style>
