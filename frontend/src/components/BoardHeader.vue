<template>
  <!-- ▼▼▼▼▼ board_title ▼▼▼▼▼ -->
  <div class="section s_01" style="width: 100%; z-index: 0">
    <div class="accordion_one">
      <!-- ▼▼▼ accordion_header ▼▼▼ -->
      <div class="accordion_header open" style="display: flex" ref="accordion_header">
        <!-- read only のときはv-ifで表示を変えたりしないと -->
        <textarea
          class="form_common form_title"
          v-model="title"
        >
        </textarea>
        <div class="">
          <div
            id="btn"
            class="menu"
            style="width: 70px; margin-top: 50px; color: #b4bdc6"
            @click="isVisible = !isVisible"
          >
            ▼
          </div>
        </div>
      </div>
      <transition name="toggle">
        <!-- ▼▼▼ accordion_inner ▼▼▼ -->
        <div v-if="isVisible" class="accordion_inner" ref="accordion_inner">
        <!-- <div class="accordion_inner" ref="accordion_inner"> -->
          <div class="" style="display: flex">
            <div class="">
              <div class="" style="width: 684px">
                <div style="display: flex">
                  <textarea
                    class="form_common form_description"
                    v-model="description">
                  </textarea>
                  <div
                    class="board_thumbnail"
                    style=""
                  >
                    <div id="" class="btn_edit">
                      <p>Edit</p>
                    </div>
                  </div>
                </div>
                <div
                  style="
                    width: 684px;
                    color: #b4bdc6;
                  "
                  class=""
                >
                <input
                  v-if="isEditting"
                  class="form_common form_tagList"
                  v-model="convertTagsToTaglist"
                  @focusout="isEditting = !isEditting"
                  ref="form_tags"
                  id="form_tags"
                >
                <div
                  v-if="!isEditting"
                  class="form_tagList"
                  style="display: flex;"
                  @click="hadleClickTags()"
                >
                  <div v-for="tag in tags" :key="tag">#{{ tag }}</div>
                  <!-- <div class="">#地球温暖化、</div> -->
                  <!-- <div class="">#自然電力</div> -->
                </div>
                </div>
              </div>

              <div class="" style="display: flex; width: 684px">
                <div class="">
                  <div style="display: flex; margin: 10px">
                    <div class="">
                      <div style="display: flex">
                        <div id="btn">
                          <img
                            class="btn_boardsUser"
                            src="@/assets/images/userimages/user00.jpg"
                            alt="プロフィール画像"
                          />
                        </div>
                        <div>
                          <div
                            class=""
                            style="
                              color: #87929d;
                              font-size: 20px;
                              margin: 3px 0px 0px 10px;
                            "
                          >
                            内藤迅
                          </div>
                          <div
                            class=""
                            style="
                              color: #b4bdc6;
                              font-size: 14px;
                              margin: 5px 0px 0px 10px;
                            "
                          >
                            {{ createdAt }}
                          </div>
                        </div>
                      </div>
                    </div>

                    <div style="display: flex">
                      <div class="" style="display: flex; margin-left: 360px">
                        <div id="btn" class="" style="margin: 0px 14px">
                          <img
                            class="icon_indexBoards"
                            src="@/assets/images/icons/icons_like.png"
                            alt="いいねボタン"
                            style="padding-left: 5px; margin: 5px 0px 5px 0px"
                          />
                          <div class="" style="color: #b4bdc6; font-size: 16px;">{{ likes }}</div>
                        </div>
                        <div id="btn" class="" style="margin: 0px 14px;">
                          <img
                            class="icon_indexBoards"
                            src="@/assets/images/icons/icons_comment.png"
                            alt="コメントボタン"
                            style="padding-left: 5px; margin: 5px 0px 5px 0px"
                          />
                          <div class="" style="color: #b4bdc6; font-size: 16px;">{{ comments }}</div>
                        </div>
                        <div id="btn" class="" style="margin: 0px 14px">
                          <img
                            class="icon_indexBoards"
                            src="@/assets/images/icons/icons_share.png"
                            alt="シェアボタン"
                            style="padding-left: 5px; margin: 5px 0px 5px 0px"
                          />
                          <div class="" style="color: #b4bdc6; font-size: 16px;">{{ shares }}</div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div style="display: flex; margin: 220px 0px 0px 50px" class="">
              <div
                id="btn"
                class=""
                style="
                  width: 50px;
                  height: 28px;
                  border-radius: 5px;
                  text-align: center;
                  border: 1px solid #525e6a;
                  background-color: #ffffff;
                  line-height: 28px;
                "
              >
                <p @click="deleteBoard()" style="font-size: 14px; color: #525e6a">Delete</p>
              </div>
              <div
                id="btn"
                class=""
                style="
                  width: 50px;
                  height: 28px;
                  border-radius: 5px;
                  text-align: center;
                  background-color: #5486b9;
                  line-height: 28px;
                  margin-left: 10px;
                "
              >
                <p @click="updateBoard()" style="font-size: 14px; color: #ffffff">Save</p>
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
import axios from 'axios';

export default {
  name: 'BoardHeader',
  data: function () {
    return {
      isVisible: true,
      title: null,
      description: null,
      thumbnail: '../assets/images/treediagram.png',
      tagList: this.convertTagsToTaglist,
      tags: null,
      // tags: [
      //   { id: 1, value: '気候変動' },
      //   { id: 2, value: '地球温暖化' },
      //   { id: 3, value: '自然電力' },
      // ],
      urlTail: '',
      isPublished: true,
      createdAt: '2020/09/20',
      updatedAt: '',
      likes: '162',
      comments: '14',
      shares: '56',
      isEditting: false
    }
  },
  methods: {
    updateBoard() {
      // const URL_BASE = 'http://127.0.0.1:8000/newsapp/get';
      const URL_BASE = 'https://131994d0-4681-4385-92ea-5a73eeb84363.mock.pstmn.io/board/update';
      return axios({
        method: 'POST',
        url: URL_BASE,
        data: {
          "board_id": 45,
          "board_title": this.title,
          "board_description": this.description,
          "board_thumbnail": this.thumbnail,
          "board_url_tail": this.url_tail,
          "isPublished": this.isPublished,
          "user_id": 31,
          // "tagList": [ "気候変動", "地球温暖化", "自然電力" ]
          "tagList": this.convertTaglistToTags
        },
      }).then((res) => {
        console.dir(res.data);
        console.log(res.data.board_id);
      }).catch((err) => {
        console.log('ERROR!! occurred in Backend.')
        console.log(err)
      });
    },
    deleteBoard() {
      // const URL_BASE = 'http://127.0.0.1:8000/newsapp/get';
      const URL_BASE = 'https://131994d0-4681-4385-92ea-5a73eeb84363.mock.pstmn.io/board/delete';
      return axios({
        method: 'DELETE',
        url: URL_BASE,
        data: {
          "board_id": 45,
        },
      }).then((res) => {
        console.dir(res.data);
        // console.log(res.data.board_id);
      }).catch((err) => {
        console.log('ERROR!! occurred in Backend.')
        console.log(err)
      });
    },
    // convertTagsToTaglist: function() {
    //   this.tagList =
    // }
    hadleClickTags() {
      this.isEditting = !this.isEditting
      // なぜ存在するのに取得できない？ライフサイクルの問題？
      // const el = document.getElementById('form_tags')
      // console.log(el)
      // console.log(this.$refs.form_tags)
      // this.$refs.form_tags.focus()
      // el.focus()
    },
    convertTaglistToTags: function() {
      return this.tagList.split(',')
    }
  },
  computed: {
    // convertTaglistToTags: function() {
    //   return this.tagList.split(',')
    // }
    convertTagsToTaglist: function() {
      return this.tags.join(' #')
    }
  },
  mounted: function() {
    const URL_BASE = 'http://127.0.0.1:8000/api/board/2';
    return axios({
      method: 'GET',
      url: URL_BASE,
    }).then((res) => {
      // console.dir(res.data);
      console.dir(res);
      // this.board_id = res.data.board_info.board_id
      // console.log((typeof res.data));
      console.log(res.data.board_info);
      console.log(res.data.title);
      this.title = res.data.title
      this.description = res.data.description
      this.tags = res.data.tag_list
    }).catch((err) => {
      console.log('ERROR!! occurred in Backend.')
      console.log(err)
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
}
</script>

<style scoped>
.toggle-enter {
  /* display: none; */
}
.toggle-enter-active {
  /* animation: display 1s; */
  /* transition: all 0.5s; */
  /* overflow: hidden; */
}
.toggle-enter-to {
  /* animation: slide-in 0.5s; */
  /* display: block; */
}
.toggle-leave {

}
.toggle-leave-active {

}
.toggle-leave-to {
  /* animation: slide-in 0.5s reverse; */
  /* height: 0; */
  /* transition: all 0.5s; */
}

/* @keyframes slide-in {
  from {
    transform: translateY(0);
  }
  to {
    transform: translateY(100px);
  }
} */

  .board_thumbnail {
    width: 150px;
    height: 150px;
    border-radius: 10px;
    border: solid 1px #e1e6eb;
    background-image: url('../assets/images/treediagram.png');
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
    margin-top: 70px;
    font-size: 30px;
  }
</style>
