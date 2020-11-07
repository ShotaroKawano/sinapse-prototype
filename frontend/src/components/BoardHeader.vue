<template>
  <!-- ▼▼▼▼▼ board_title ▼▼▼▼▼ -->
  <!-- <div class="section s_01"> -->
  <div class="section">
    <!-- <div class="accordion_one"> -->
    <div class="box_BoardHeader">
      <!-- ▼▼▼ accordion_header ▼▼▼ -->
      <!-- <div class="accordion_header open displayFlex" ref="accordion_header"> -->
      <!-- <div class="displayFlex"> -->
        <!-- read only のときはv-ifで表示を変えたりしないと -->
        <!-- <div>
          <div id="btn" class="menu" @click="isVisible = !isVisible">
            <span v-if="isVisible">
              <img
                class="icon_headerUpDown"
                src="@/assets/images/icons/icons_headerup.png"
                alt="▼"
              />
            </span>
            <span v-else>
              <img
                class="icon_headerUpDown"
                src="@/assets/images/icons/icons_headerdown.png"
                alt="▲"
              />
            </span>
          </div>
        </div> -->
      <!-- </div> -->
      <!-- <transition name="toggle"> -->
        <!-- ▼▼▼ accordion_inner ▼▼▼ -->
        <!-- <div v-if="isVisible" class="accordion_inner" ref="accordion_inner"> -->
        <div>
          <!-- <div class="accordion_inner" ref="accordion_inner"> -->
          <div class="">
            <textarea
              v-if="isAuthor"
              id="scrollbar"
              class="form_titleAuthor"
              placeholder="Title..."
              v-model="title"
              @focusout="updateBoard()"
            >
            </textarea>
            <p id="scrollbar" class="form_titleReader" v-else>
              {{ title }}
            </p>
            <div class="">
              <div class="box_accordion1">
                <div class="displayFlex">
                  <textarea
                    v-if="isAuthor"
                    id="scrollbar"
                    class="form_descriptionAuthor"
                    placeholder="Description..."
                    v-model="description"
                    @focusout="updateBoard()"
                  >
                  </textarea>
                  <p id="scrollbar" class="form_descriptionReader" v-else>
                    {{ description }}
                  </p>
                  <!-- <div
                    v-if="!isEditting2"
                    @click="isEditting2 = !isEditting2"
                    class="board_thumbnail"
                    :style="{ backgroundImage: 'url(' + thumbnail + ')' }"
                  >
                    <div id="" class="btn_edit" v-if="isAuthor">
                      <p>Edit</p>
                    </div>
                  </div>
                  <input
                    v-if="isEditting2"
                    @focusout="updateBoard()"
                    type="url"
                    class="box_thumbnailUrl"
                    id="thumbnail"
                    placeholder="thumbnail URL"
                    v-model="thumbnail"
                  /> -->
                </div>
                <div class="text_edit">
                  <input
                    v-if="isEditting"
                    class="form_common form_tagList"
                    v-model="convertBoardTagsToTagList"
                    @focusout="updateBoard()"
                    ref="form_tags"
                    id="form_tags"
                  />
                  <div
                    v-if="!isEditting"
                    class="form_tagList displayFlex"
                    @click="hadleClickTags()"
                  >
                    <div
                      v-for="tagWrapper in boardTags"
                      :key="tagWrapper.tag.id"
                    >
                      #{{ tagWrapper.tag.name }}
                    </div>
                    <!-- <div class="">#地球温暖化、</div>
                    <div class="">#自然電力</div> -->
                  </div>
                </div>
              </div>

              <div class="box_user1">
                <div class="box_user1">
                  <div class="box_user2">
                    <div class="box_user3">
                      <div class="displayFlex">
                        <div id="btn">
                          <img
                            class="btn_boardsUser"
                            src="@/assets/images/userimages/user_default.jpg"
                            alt="プロフィール画像"
                          />
                        </div>
                        <div class="box_NameAndCreatdate">
                          <div class="indexUsername">{{ user.username }}</div>
                          <div class="indexCreatdate">
                            {{ getNowDateWithString(updatedAt) }}
                          </div>
                        </div>
                      </div>
                    </div>

                    <div class="box_user1">
                      <div class="box_user4">
                        <div id="btn" class="box_indexSns3">
                          <img
                            class="icon_indexBoards"
                            src="@/assets/images/icons/icons_like.png"
                            alt="いいねボタン"
                          />
                          <div class="text_indexSns">
                            {{ likes }}
                          </div>
                        </div>
                        <!-- <div id="btn" class="box_indexSns3">
                          <img
                            class="icon_indexBoards"
                            src="@/assets/images/icons/icons_comment.png"
                            alt="コメントボタン"
                          />
                          <div class="text_indexSns">
                            {{ comments }}
                          </div>
                        </div> -->
                        <!-- <div id="btn" class="box_indexSns3">
                          <img
                            class="icon_indexBoards"
                            src="@/assets/images/icons/icons_share.png"
                            alt="シェアボタン"
                          />
                          <div class="text_indexSns">
                            {{ shares }}
                          </div>
                        </div> -->
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="box_deleteAndsaveButton">
              <div v-if="isAuthor" id="btn" class="btn_delete">
                <p @click="deleteBoard()" class="text_delete">Delete</p>
              </div>
              <!-- <div v-if="isAuthor" id="btn" class="btn_save">
                <p @click="updateBoard()" class="text_save">Save</p>
              </div> -->
            </div>
          </div>
        </div>
      <!-- </transition> -->

            <div>
              <div class="box_Thumbnail">
                <div class="btn_edit" v-if="isAuthor">
                  <p @click="isEditting2 = !isEditting2">Edit</p>
                </div>
                <img
                  v-if="!isEditting2"
                  class="board_thumbnail"
                  :src=" thumbnail "
                >
              </div>
              <input
                v-if="isEditting2"
                @focusout="updateBoard()"
                type="url"
                class="box_thumbnailUrl"
                id="thumbnail"
                placeholder="thumbnail URL"
                v-model="thumbnail"
              />
            </div>

    </div>
  </div>
  <!-- ▲▲▲▲▲ board_title ▲▲▲▲▲ -->
</template>

<script>

export default {
  name: "BoardHeader",
  props: {
    isAuthor: {
      type: Boolean,
      defult: false
    },
    zoom: {
      type: Number,
      defult: 1
    }
  },
  data: function () {
    return {
      isVisible: false,

      title: null,
      // title: "１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８",
      description: null,
      // description: "１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０１２３４５６７８９０",
      thumbnail: "../assets/images/icons/noimage.jpg",
      url_tail: "12345",
      is_published: true,

      tagList: this.convertTagsToTaglist,
      boardTags: null,
      // tags: [
      //   { id: 1, value: '気候変動' },
      //   { id: 2, value: '地球温暖化' },
      //   { id: 3, value: '自然電力' },
      // ],
      createdAt: null,
      updatedAt: null,
      likes: null,
      comments: "14",
      shares: "56",
      isEditting: false,
      isEditting2: false,
      // userId: null,
      user: null,
    };
  },
  computed: {
    token() {
      return this.$store.getters.token
    },
    // TODO:重複してる
    getNowDateWithString() {
      return function(date) {
        var dt = new Date(date);
        var y = dt.getFullYear();
        var m = ("00" + (dt.getMonth() + 1)).slice(-2);
        var d = ("00" + dt.getDate()).slice(-2);
        var result = y + "/" + m + "/" + d;
        return result;
      }
    },
    convertBoardTagsToTagList: function () {
      // console.log('kokodesu');
      var tagList = "";
      this.boardTags.forEach((tagWrapper, index) => {
        // console.log(tagWrapper)
        if (index === 0) {
          tagList += tagWrapper.tag.name;
        } else {
          tagList += "," + tagWrapper.tag.name;
        }
      });
      return tagList;
    },
    // convertTagsToTaglist: function() {
    //   return this.tags.join(" #");
    // }
  },
  // computed: {
  //   isAuthor () {
  //     return this.$store.state.userId === parseInt(this.userId)
  //   }
  // },
  methods: {
    updateBoard() {
      if (this.isAuthor) {
        this.isEditting = false
        this.isEditting2 = false
        this.$axios({
          method: "PATCH",
          // method: "PUT",
          url: "api/boards/" + this.$route.params.id + "/",
          headers: {
            Authorization: `JWT ${this.token}`
          },
          data: {
            title: this.title,
            description: this.description,
            thumbnail: this.thumbnail,
            // url_tail: this.url_tail,
            is_published: this.is_published,
            // zoom: this.zoom,
            // user_id: this.$store.getters.userId,
            // "tagList": [ "気候変動", "地球温暖化", "自然電力" ]
            // tagList: this.convertTaglistToTags
          },
        })
        .then(() => {})
        .catch(() => {})
      }
    },
    deleteBoard() {
      let result = confirm('削除した場合、元には戻せません。本当に削除しますか？');
      if (result) {
        this.$axios({
          method: "DELETE",
          url: "api/boards/" + this.$route.params.id,
          headers: {
            Authorization: `JWT ${this.token}`
          },
        })
        .then((res) => {
          this.$router.push("/");
        })
        .catch(() => {});
      } else {
        // 何もしない
      }
    },
    // convertTagsToTaglist: function() {
    //   this.tagList =
    // }
    hadleClickTags() {
      this.isEditting = !this.isEditting;
      // なぜ存在するのに取得できない？ライフサイクルの問題？
      // const el = document.getElementById('form_tags')
      // console.log(el)
      // console.log(this.$refs.form_tags)
      // this.$refs.form_tags.focus()
      // el.focus()
    },
    // convertBoardTagsToTagList: function() {
    //   console.log('kokodesu');
    //   var tagList = ''
    //   boardTags.forEach(tagWrapper => {
    //     console.log(tagWrapper);
    //     tagList += ', ' + tagWrapper.name
    //   });
    //   return tagList
    // }
  },
  created: function () {
    this.$axios({
      method: "GET",
      url: "api/boards/" + this.$route.params.id,
      headers: {
        Authorization: `JWT ${this.token}`
      },
    })
    .then((res) => {
      // this.userId = res.data.user.id
      this.user = res.data.user
      // console.log('user');
      // console.log(this.$store.state.userId);
      // console.log(parseInt(this.userId));
      // console.log(this.$store.state.userId === parseInt(this.userId));
      const isAuthor = (this.$store.getters.userId === parseInt(this.user.id)) || (this.$store.getters.userId === 1)
      console.log(isAuthor);
      this.$emit('update-is-author', isAuthor)
      this.$emit('change-zoom', res.data.zoom)
      this.title = res.data.title
      this.description = res.data.description
      this.boardTags = res.data.board_tags
      this.thumbnail = res.data.thumbnail
      this.createdAt = res.data.created_at
      this.updatedAt = res.data.updated_at
      this.likes = res.data.like_count
    })
    .catch(() => {});
  },
  // mounted: function () {
  //       $('.s_01 .accordion_one .accordion_header').click(function () {
  //       // クリックされた.accordion_oneの中の.accordion_headerに隣接する.accordion_innerが開いたり閉じたりする。
  //       $(this).next('.accordion_inner').slideToggle()
  //       $(this).toggleClass('open')
  //       console.log($(this));
  //     })
  // toggleBoarHeader () {
  // console.log(this);
  // this.$ref.accordion_inner
  //   $(this).next('.accordion_inner').slideToggle()
  //   $(this).toggleClass('open')
  // }
  // }
};
</script>

<style scoped>
.box_BoardHeader{
  display: flex;
  max-width: 900px;
  max-height: 240px;
  margin: 0 auto;
}

.board_thumbnail {
  z-index: 0;
  /* width: 114px;
  height: 100px; */
  min-width: 200px;
  max-height: 222px;
  border-radius: 10px;
  /* border: solid 1px #e1e6eb; */
  border: none;
  /* background-image: url("../assets/images/icons/noimage.jpg"); */
  background-size: cover;
  margin-left: 10px;
  margin-bottom: 10px;
  background-position: center center;
}
.box_thumbnailUrl{
  z-index: 2;
  width: 260px;
  height: 26px;
  border-radius: 5px;
  border: 1px solid #e1e6eb;
  background: #ffffff;
  margin: 10px 0px 0px 10px;
  position: absolute;
}
.board_thumbnail > img {
  z-index: 0;
  object-fit: cover;
  min-width: 200px;
  max-height: 222px;
  border: none;
  /* object-fit: contain; */
    /* 画像を常に天地左右の中央に配置 */
  background-position: center center;

  /* 画像をタイル状に繰り返し表示しない */
  background-repeat: no-repeat;

  /* コンテンツの高さが画像の高さより大きい時、動かないように固定 */
  background-attachment: fixed;

  /* 表示するコンテナの大きさに基づいて、背景画像を調整 */
  background-size: cover;
}

.box_Thumbnail{
  z-index: 0;
  /* max-width: 150px;
  max-height: 150px; */
  /* width: 150px;
  height: 150px; */
  border-radius: 10px;
}
.box_Thumbnail img {
  z-index: 0;
  object-fit: cover;
}
.box_Thumbnail > img {
  z-index: 0;
  max-width: 200px;
  max-height: 170px;
  /* object-fit: contain; */
}

.form_common {
  /* appearance: none; が効かない*/
  /* border: none; */
  border: solid 1px #e1e6eb;
  resize: none;
  /* outline: none; */
  overflow-wrap: break-word;
}

.form_titleAuthor {
  color: #525e6a;
  max-height: 66px;
  width: 684px;
  font-size: 24px;
  line-height: 36px;
  font-weight: bold;
  margin: 0px 0px 10px 0px;
  /* padding-top: 5px; */
  border-radius: 10px;
  /* overflow: hidden; */
  overflow-wrap:break-word;
  display: -webkit-box;
  overflow-x: hidden;
  overflow-y: scroll;
  /* -webkit-line-clamp: 2;
  -webkit-box-orient: vertical; */

  /* appearance: none; が効かない*/
  /* border: none; */
  border: solid 1px #e1e6eb;
  resize: none;
  /* outline: none; */
  overflow-wrap: break-word;
}
.form_titleAuthor::placeholder {
  color: #525e6a50;
}
.form_titleAuthor:hover {
  background-color: #B4BDC620;
}
.form_titleReader {
  color: #525e6a;
  max-height: 66px;
  width: 684px;
  font-size: 24px;
  line-height: 36px;
  font-weight: bold;
  margin: 0px 0px 10px 0px;
  /* padding-top: 5px; */
  /* border-radius: 10px; */
  /* overflow: hidden; */
  overflow-wrap:break-word;
  display: -webkit-box;
  overflow-x: hidden;
  overflow-y: scroll;
  /* -webkit-line-clamp: 2;
  -webkit-box-orient: vertical; */
  cursor: default;

  /* appearance: none; が効かない*/
  /* border: none; */
  /* border: solid 1px #e1e6eb; */
  resize: none;
  /* outline: none; */
  overflow-wrap: break-word;
}

.form_descriptionAuthor {
  color: #525e6a;
  max-height: 74px;
  /* width: 543px; */
  width: 684px;
  font-size: 16px;
  line-height: 24px;
  margin: 0px 0px 5px 0px;
  border-radius: 10px;
  /* overflow: hidden; */
  overflow-wrap:break-word;
  display: -webkit-box;
  overflow-x: hidden;
  overflow-y: scroll;
  /* -webkit-line-clamp: 5;
  -webkit-box-orient: vertical; */

  /* appearance: none; が効かない*/
  /* border: none; */
  border: solid 1px #e1e6eb;
  resize: none;
  /* outline: none; */
  overflow-wrap: break-word;
}
.form_descriptionAuthor::placeholder {
  color: #87929D50;
}
.form_descriptionAuthor:hover {
  background-color: #B4BDC620;
}
.form_descriptionReader {
  color: #525e6a;
  max-height: 74px;
  /* width: 543px; */
  width: 684px;
  font-size: 16px;
  line-height: 24px;
  margin: 0px 0px 5px 0px;
  /* border-radius: 10px; */
  /* overflow: hidden; */
  overflow-wrap:break-word;
  display: -webkit-box;
  overflow-x: hidden;
  overflow-y: scroll;
  /* -webkit-line-clamp: 5;
  -webkit-box-orient: vertical; */
  cursor: default;

  /* appearance: none; が効かない*/
  /* border: none; */
  /* border: solid 1px #e1e6eb; */
  resize: none;
  /* outline: none; */
  overflow-wrap: break-word;
}

#scrollbar::-webkit-scrollbar
{
  width:4px;
}
#scrollbar::-webkit-scrollbar-thumb
{
  background:#b4bdc6;
  -webkit-border-radius: 2px;
}

.form_tagList {
  height: 16px;
  color: #B4BDC6;
  width: 100%;
  font-size: 16px;
  /* margin: 10px 0px 0px 10px; */
  border-radius: 5px;
  /* border: solid 1px #e1e6eb; */
  border: none;
}

.section {
  width: 100%;
  padding-top: 70px;
  font-size: 30px;
  background-color: #ffffff;
}

.menu {
  /* width: 70px; */
  /* margin-top: 36px; */
  /* margin-bottom: 0px; */
  margin-left: 20px;
  /* height: 100%; */
  color: #b4bdc6;
}
.displayFlex {
  display: flex;
}

.box_accordion1 {
  width: 690px;
}
.box_user1 {
  display: flex;
  /* width: 684px; */
  width: 100%;
}
.box_user2 {
  display: flex;
  width: 100%;
  margin: 0px 10px 10px 10px;
}
.box_user3 {
  margin-top: 10px;
}
.box_user4 {
  display: flex;
  margin: 0 0 0 auto;
}

.box_indexSns3 {
  display: flex;
  margin: 0 0 0 auto;
}
.text_indexSns {
  color: #b4bdc6;
  font-size: 16px;
  margin: auto 0;
  padding-left: 5px;
}

.btn_edit {
  z-index: 1;
  width: 50px;
  height: 28px;
  /* margin: 117px 0px 0px 93px; */
  /* position: relative; */
  display: inline-block;
  border-radius: 5px; /* 角丸       */
  font-size: 14px; /* 文字サイズ */
  text-align: center; /* 文字位置   */
  cursor: pointer; /* カーソル   */
  color: #ffffff; /* 文字色     */
  background: #525e6a; /* 背景色     */
  line-height: 28px; /* 1行の高さ  */
  text-decoration: none; /* テキストアンダーライン */
  opacity: 0.6;
  margin-top: 10px;
  position: absolute;
  margin-left: 150px;
}
.btn_edit:hover {
  color: #ffffff; /* 文字色     */
  background: #525e6a; /* 背景色     */
  opacity: 1;
}
.text_edit {
  width: 690px;
  color: #b4bdc6;
}

/* .box_deleteAndsaveButton {
  display: flex;
  margin: 210px 0px 0px 10px;
} */
.btn_delete {
  width: 50px;
  height: 28px;
  border-radius: 5px;
  text-align: center;
  border: 1px solid #525e6a;
  background-color: #ffffff;
  line-height: 28px;
  margin-top: -44px;
  margin-left: -64px;
  position: fixed;
}
.text_delete {
  font-size: 14px;
  color: #525e6a;
}
.btn_save {
  width: 50px;
  height: 28px;
  border-radius: 5px;
  text-align: center;
  background-color: #5486b9;
  line-height: 28px;
  margin-left: 10px;
}
.text_save {
  font-size: 14px;
  color: #ffffff;
}

.box_NameAndCreatdate {
  padding-left: 12px;
}
.indexUsername {
  /* 必要 */
  padding-top: 4px;
  font-size: 18px;
  color: #87929d;
}
.indexCreatdate {
  /* 必要 */
  padding-top: 6px;
  font-size: 14px;
  color: #b4bdc6;
}

.icon_indexBoards {
  width: 20px;
  height: 20px;
  /* padding-left: 5px;
  margin: 5px 0px 5px 0px; */
  padding-bottom: 5px;
  margin: auto 0;
}
.icon_headerUpDown {
  width: 30px;
  /* margin-top: 100%; */
}

.btn_boardsUser {
  width: 44px;
  height: 44px;
  border-radius: 25px;
}

/*====================================================================
.s_01 .accordion_one
====================================================================*/
.s_01 .accordion_one {
  max-width: 900px;
  margin: 0 auto;
}
.s_01 .accordion_one .accordion_header {
  color: #525e6a;
  /* font-size: 26px; */
  /* font-weight: bold; */
  /* padding: 20px 11%; */
  /* text-align: center; */
  position: relative;
  z-index: +1;
  /* cursor: pointer; */
  transition-duration: 0.2s;
}

.s_01 .accordion_one .accordion_header:hover {
  opacity: 0.8;
}
.s_01 .accordion_one .accordion_header .i_box {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  top: 50%;
  right: 5%;
  width: 40px;
  height: 40px;
  border: 1px solid #fff;
  margin-top: -20px;
  box-sizing: border-box;
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
  transform-origin: center center;
  transition-duration: 0.2s;
}
.s_01 .accordion_one .accordion_header .i_box .one_i {
  display: block;
  width: 18px;
  height: 18px;
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
  transform-origin: center center;
  transition-duration: 0.2s;
  position: relative;
}
.s_01 .accordion_one .accordion_header.open .i_box {
  -webkit-transform: rotate(-360deg);
  transform: rotate(-360deg);
}
.s_01 .accordion_one .accordion_header .i_box .one_i:before,
.s_01 .accordion_one .accordion_header .i_box .one_i:after {
  display: flex;
  content: "";
  background-color: #fff;
  border-radius: 10px;
  width: 18px;
  height: 4px;
  position: absolute;
  top: 7px;
  left: 0;
  -webkit-transform: rotate(0deg);
  transform: rotate(0deg);
  transform-origin: center center;
}
.s_01 .accordion_one .accordion_header .i_box .one_i:before {
  width: 4px;
  height: 18px;
  top: 0;
  left: 7px;
}
.s_01 .accordion_one .accordion_header.open .i_box .one_i:before {
  content: none;
}
.s_01 .accordion_one .accordion_header.open .i_box .one_i:after {
  -webkit-transform: rotate(-45deg);
  transform: rotate(-45deg);
}
.s_01 .accordion_one .accordion_inner {
  /* display: none; */
  box-sizing: border-box;
}

.s_01 .accordion_one .accordion_inner .box_one {
  height: 300px;
}
.s_01 .accordion_one .accordion_inner p.txt_a_ac {
  margin: 0;
}
@media screen and (max-width: 760px) {
  .s_01 .accordion_one .accordion_header {
    font-size: 18px;
  }
  .s_01 .accordion_one .accordion_header .i_box {
    width: 30px;
    height: 30px;
    margin-top: -5px;
  }
}
@media screen and (max-width: 767px) {
  .s_01 .accordion_one .accordion_header {
    font-size: 16px;
    text-align: left;
    padding: 5px 10px 5px 5px;
  }
}
</style>
