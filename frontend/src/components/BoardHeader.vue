<template>
  <!-- ▼▼▼▼▼ board_title ▼▼▼▼▼ -->
  <div class="section s_01">
    <div class="accordion_one">
      <!-- ▼▼▼ accordion_header ▼▼▼ -->
      <div class="accordion_header open displayFlex" ref="accordion_header">
        <!-- read only のときはv-ifで表示を変えたりしないと -->
        <textarea
          class="form_common form_title"
          maxlength="38"
          placeholder="タイトル（最大38文字）"
          v-model="title">
        </textarea>
        <div>
          <div id="btn" class="menu" @click="isVisible = !isVisible">
            <!-- ▼ -->
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
        </div>
      </div>
      <transition name="toggle">
        <!-- ▼▼▼ accordion_inner ▼▼▼ -->
        <div v-if="isVisible" class="accordion_inner" ref="accordion_inner">
          <!-- <div class="accordion_inner" ref="accordion_inner"> -->
          <div class="displayFlex">
            <div class="">
              <div class="box_accordion1">
                <div class="displayFlex">
                  <textarea
                    class="form_common form_description"
                    maxlength="125"
                    placeholder="見出し（最大125文字）"
                    v-model="description"
                  >
                  </textarea>
                  <!-- TODO: thumnailも編集できるようにする -->
                  <div class="board_thumbnail">
                    <div id="" class="btn_edit">
                      <p>Edit</p>
                    </div>
                  </div>
                </div>
                <div class="text_edit">
                  <input
                    v-if="isEditting"
                    class="form_common form_tagList"
                    v-model="convertBoardTagsToTagList"
                    @focusout="isEditting = !isEditting"
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
                <div class="">
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
                          <div class="indexUsername">内藤迅</div>
                          <div class="indexCreatdate">
                            {{ createdAt }}
                          </div>
                        </div>
                      </div>
                    </div>

                    <div class="displayFlex">
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
                        <div id="btn" class="box_indexSns3">
                          <img
                            class="icon_indexBoards"
                            src="@/assets/images/icons/icons_comment.png"
                            alt="コメントボタン"
                          />
                          <div class="text_indexSns">
                            {{ comments }}
                          </div>
                        </div>
                        <div id="btn" class="box_indexSns3">
                          <img
                            class="icon_indexBoards"
                            src="@/assets/images/icons/icons_share.png"
                            alt="シェアボタン"
                          />
                          <div class="text_indexSns">
                            {{ shares }}
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="box_deleteAndsaveButton">
              <div id="btn" class="btn_delete">
                <p @click="deleteBoard()" class="text_delete">Delete</p>
              </div>
              <div id="btn" class="btn_save">
                <p @click="updateBoard()" class="text_save">Save</p>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>
  </div>
  <!-- ▲▲▲▲▲ board_title ▲▲▲▲▲ -->
</template>

<script>

export default {
  name: "BoardHeader",
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
      createdAt: "2020/09/20",
      updatedAt: "",
      likes: "162",
      comments: "14",
      shares: "56",
      isEditting: false,
    };
  },
  methods: {
    updateBoard() {
      // console.log(this.title);
      const tail =
        "api/boards/" + this.$route.params.id + "/";
      // const URL_BASE =
      //   "https://131994d0-4681-4385-92ea-5a73eeb84363.mock.pstmn.io/board/update";
      this.$axios({
        method: "PATCH",
        // method: "PUT",
        url: tail,
        // withCredentials: true,
        data: {
          title: this.title,
          description: this.description,
          thumbnail: this.thumbnail,
          // url_tail: this.url_tail,
          is_published: this.is_published,
          // user_id: 1,
          // "tagList": [ "気候変動", "地球温暖化", "自然電力" ]
          // tagList: this.convertTaglistToTags
        },
      })
        .then(() => {})
        .catch(() => {})
    },
    deleteBoard() {
      // const URL_BASE = 'http://127.0.0.1:8000/newsapp/get';
      const tail =
        "api/boards/" + this.$route.params.id;
      this.$axios({
        method: "DELETE",
        url: tail,
      })
        .then((res) => {
          this.$router.push("/");
        })
        .catch(() => {});
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
  computed: {
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
  created: function () {
    const tail =
      "api/boards/" + this.$route.params.id;
    this.$axios({
      method: "GET",
      url: tail,
    })
      .then((res) => {
        this.title = res.data.title;
        this.description = res.data.description;
        this.boardTags = res.data.board_tags;
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
.board_thumbnail {
  width: 150px;
  height: 150px;
  border-radius: 10px;
  border: solid 1px #e1e6eb;
  background-image: url("../assets/images/icons/noimage.jpg");
  background-size: cover;
  margin-left: 20px;
  background-position: center center;
}

.form_common {
  /* appearance: none; が効かない*/
  border: none;
  resize: none;
  /* outline: none; */
  overflow-wrap: break-word;
}

.form_title {
  color: #525e6a;
  height: 84px;
  width: 684px;
  font-size: 36px;
  line-height: 44px;
  margin: 0px 0px 10px 0px;
  padding-top: 5px;
  overflow: hidden;
  border-radius: 10px;
}
.form_title:hover {
  background-color: #B4BDC620;
}

.form_description {
  color: #87929D;
  height: 150px;
  width: 500px;
  font-size: 20px;
  line-height: 30px;
  margin: 0px 0px 5px 0px;
  overflow: hidden;
  border-radius: 10px;
}
.form_description:hover {
  background-color: #B4BDC620;
}

.form_tagList {
  height: 16px;
  color: #B4BDC6;
  width: 70%;
  font-size: 16px;
  margin: 10px 0px 0px 10px;
}

.section {
  width: 100%;
  margin-top: 70px;
  font-size: 30px;
}

.menu {
  width: 70px;
  margin-top: 56px;
  color: #b4bdc6;
}
.displayFlex {
  display: flex;
}

.box_accordion1 {
  width: 684px;
}
.box_user1 {
  display: flex;
  width: 684px;
}
.box_user2 {
  display: flex;
  margin: 0px 10px 10px 10px;
}
.box_user3 {
  margin-top: 10px;
}
.box_user4 {
  display: flex;
  margin-left: 364px;
}

.box_indexSns3 {
  margin: 0px 14px;
}
.text_indexSns {
  color: #b4bdc6;
  font-size: 16px;
}

.btn_edit {
  width: 50px;
  height: 28px;
  margin: 117px 0px 0px 97px;
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
}
.btn_edit:hover {
  color: #ffffff; /* 文字色     */
  background: #525e6a; /* 背景色     */
  opacity: 1;
}
.text_edit {
  width: 684px;
  color: #b4bdc6;
}

.box_deleteAndsaveButton {
  display: flex;
  margin: 210px 0px 0px 50px;
}
.btn_delete {
  width: 50px;
  height: 28px;
  border-radius: 5px;
  text-align: center;
  border: 1px solid #525e6a;
  background-color: #ffffff;
  line-height: 28px;
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
  padding-left: 5px;
  margin: 5px 0px 5px 0px;
}
.icon_headerUpDown {
  width: 30px;
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
  max-width: 800px;
  margin: 0 auto;
}
.s_01 .accordion_one .accordion_header {
  color: #525e6a;
  /* font-size: 26px; */
  /* font-weight: bold; */
  /* padding: 20px 11%; */
  text-align: center;
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
  padding: 5px;
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
