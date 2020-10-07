<template>
  <!-- ▼▼▼▼▼ board_title ▼▼▼▼▼ -->
  <div class="section s_01">
    <div class="accordion_one">
      <!-- ▼▼▼ accordion_header ▼▼▼ -->
      <div class="accordion_header open displayFlex" ref="accordion_header">
        <!-- read only のときはv-ifで表示を変えたりしないと -->
        <textarea class="form_common form_title" v-model="title"> </textarea>
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
                    v-model="description"
                  >
                  </textarea>
                  <!-- TODO: thumnailも編集できるようにする -->
                  <!-- <div class="board_thumbnail">
                    <div id="" class="btn_edit">
                      <p>Edit</p>
                    </div>
                  </div> -->
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
                    <!-- <div class="">#地球温暖化、</div> -->
                    <!-- <div class="">#自然電力</div> -->
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
                            src="@/assets/images/userimages/user00.jpg"
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
import axios from "axios";

export default {
  name: "BoardHeader",
  data: function () {
    return {
      isVisible: false,

      title: null,
      description: null,
      thumbnail: "../assets/images/treediagram.png",
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
      const URL_BASE =
        "http://127.0.0.1:8000/api/boards/" + this.$route.params.id + "/";
      // const URL_BASE =
      //   "https://131994d0-4681-4385-92ea-5a73eeb84363.mock.pstmn.io/board/update";
      axios({
        method: "PUT",
        url: URL_BASE,
        // withCredentials: true,
        data: {
          title: this.title,
          description: this.description,
          thumbnail: this.thumbnail,
          url_tail: this.url_tail,
          is_published: this.is_published,
          user_id: 1,
          // "tagList": [ "気候変動", "地球温暖化", "自然電力" ]
          // tagList: this.convertTaglistToTags
        },
      })
        .then((res) => {
          // console.dir(res.data);
        })
        .catch((err) => {
          console.log("ERROR!! occurred in Backend.");
          console.log(err);
        });
    },
    deleteBoard() {
      // const URL_BASE = 'http://127.0.0.1:8000/newsapp/get';
      const URL_BASE =
        "http://127.0.0.1:8000/api/boards/" + this.$route.params.id;
      return axios({
        method: "DELETE",
        url: URL_BASE,
      })
        .then((res) => {
          // console.dir(res.data);
          this.$router.push("/");
          // console.log(res.data.board_id);
        })
        .catch((err) => {
          console.log("ERROR!! occurred in Backend.");
          console.log(err);
        });
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
    const URL_BASE =
      "http://127.0.0.1:8000/api/boards/" + this.$route.params.id;
    axios({
      method: "GET",
      url: URL_BASE,
    })
      .then((res) => {
        // console.dir(res.data);
        // console.dir(res);
        // this.board_id = res.data.board_info.board_id
        // console.log((typeof res.data));
        // console.log(res.data);
        this.title = res.data.title;
        this.description = res.data.description;
        this.boardTags = res.data.board_tags;
      })
      .catch((err) => {
        console.log("ERROR!! occurred in Backend.");
        console.log(err);
      });
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
  background-image: url("../assets/images/treediagram.png");
  background-size: cover;
  margin-left: 20px;
}

.form_common {
  /* appearance: none; が効かない*/
  border: none;
  resize: none;
  /* outline: none; */
  overflow-wrap: break-word;
}

.form_description {
  color: #525e6a;
  height: 160px;
  width: 500px;
  font-size: 20px;
  line-height: 30px;
  margin: 10px 0px 5px 0px;
}

.form_title {
  color: #525e6a;
  height: 84px;
  width: 684px;
  font-size: 36px;
  line-height: 38px;
  margin: 10px 0px 5px 0px;
}

.form_tagList {
  color: #525e6a;
  width: 70%;
  font-size: 16px;
}

.section {
  width: 100%;
  margin-top: 70px;
  font-size: 30px;
}

.menu {
  width: 70px;
  margin-top: 50px;
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
  margin: 10px;
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
  margin: 214px 0px 0px 50px;
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
</style>
