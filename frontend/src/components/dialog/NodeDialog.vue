<template>
  <div>
    <div class="modal" v-if="visible">
      <div>
        <div class="thumbnail">
          <!-- <div class="box_tool">
            <div class="btn_tabOpen">
              <img class="img_tabOpen" src="@/assets/images/icons/icons_tabopen.png"
          alt="URLを開く">
            </div>
          </div> -->
          <!-- <img :src="nodeForm.thumbnail" alt="" class="box_thumbnail" /> -->
          <img
            v-if="!isEditting"
            @click="isEditting = !isEditting"
            :src="nodeForm.thumbnail"
            alt="No image"
            class="box_thumbnail"
          />
          <div class="box_img-urlControl">
            <input
              v-if="isEditting"
              @focusout="handleClickSaveNode"
              type="url"
              class="img-urlControl"
              id="thumbnail"
              v-model="nodeForm.thumbnail"
            />
          </div>
        </div>
      </div>
      <div class="body">
        <!-- <input class="form-control" v-model="nodeForm.thumbnail"/> -->
        <label for="url">URL</label>
        <div class="box_urlEdit">
          <input
            type="url"
            class="form-urlControl"
            id="url"
            v-model="nodeForm.url"
          />
          <button v-if="isAuthor" id="btn" class="btn_get" @click="handleClickGetInfo">
            <p class="text_get">Get</p>
          </button>
          <!-- <div v-else id="btn" class="btn_tabOpen" @click="newTabOpen" target="_blank"> -->
            <!-- <p class="text_get">Open</p> -->
            <!-- <img class="img_tabOpen" src="@/assets/images/icons/icons_tabopen.png" alt="URLを開く"> -->
          <!-- </div> -->
        </div>

        <div class="form-allControl">
          <label for="title">Title</label>
          <!-- <input class="form-control" id="title" v-model="nodeForm.title" /> -->
          <textarea
            class="form-titleControl"
            name="title"
            id="title"
            rows="3"
            v-model="nodeForm.title"
            @focusout="handleClickSaveNode"
          ></textarea>
        </div>

        <div class="form-allControl">
          <label for="summary">Note</label>
          <!-- <input class="form-control" id="summary" v-model="nodeForm.summary" /> -->
          <textarea
            class="form-summaryControl"
            name="summary"
            id="summary"
            rows="9"
            v-model="nodeForm.summary"
            @focusout="handleClickSaveNode"
          ></textarea>
        </div>
        <div class="box_footerButton">
          <div id="" style="width: 50px;" @click="handleClickCancelSaveNode">
            <!-- <p>Cancel</p> -->
            <div class="btn_cancel">
              <img
              class="img_cancel"
              src="/static/img/icons_cancel.png"
              alt="閉じる">
            </div>
          </div>
          <div class="footerButton">
            <div  v-if="isAuthor" id="btn" class="btn_delete" @click="deleteNode">
              <p class="text_delete">Delete</p>
            </div>
            <!-- <div  v-if="isAuthor" id="btn" class="btn_save" @click="handleClickSaveNode">
              <p class="text_save">Save</p>
            </div> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {

  props: {
    visible: {
      type: Boolean,
      // default: false,
      default: true,
    },
    node: {
      type: Object,
      default: null,
    },
    isAuthor: {
      type: Boolean,
      defult: false
    }
  },

  data: function () {
    return {
      nodeForm: {
        id: null,
        url: null,
        title: null,
        summary: null,
        thumbnail: null,
        // thumbnail: require('@/assets/images/icons/noimage.jpg'),
      },
      isEditting: false
      // nodeForm: {name: null, id: null, type: null, approver: []},
      // approvers: [{id: 1, name: 'Joyce'}, {id: 2, name: 'Allen'}, {id: 3, name: 'Teresa'}],
    };
  },
  computed: {
    token() {
      return this.$store.getters.token
    },
  },
  methods: {
    newTabOpen () {
      console.log(this.nodeForm.url);
      // this.$router.go(this.nodeForm.url, '_blank')
      window.open(this.nodeForm.url, '_blank,noopener')
    },
    deleteNode() {
      let result = confirm('削除した場合、元には戻せません。本当に削除しますか？');
      if (result) {
        this.$emit("handle-delete-node", this.node);
        this.$emit("update:visible", false);
      } else {
        // 何もしない
      }
    },
    handleClickGetInfo() {
      this.$axios({
        method: "POST",
        url: "api/scrape/",
        headers: {
          Authorization: `JWT ${this.token}`
        },
        data: {
          url: this.nodeForm.url,
        },
      })
      .then((res) => {
        this.nodeForm.thumbnail = res.data.soup_img;
        this.nodeForm.title = res.data.soup_title;
        this.nodeForm.summary = res.data.soup_desc;
        this.handleClickSaveNode()
      })
      .catch(() => {});
    },
    // save押下時に実行される
    handleClickSaveNode() {
      this.isEditting = false
      this.$axios({
        method: "PATCH",
        url: "api/cards/" + this.node.id + "/",
        headers: {
          Authorization: `JWT ${this.token}`
        },
        data: {
          url: this.nodeForm.url,
          title: this.nodeForm.title,
          summary: this.nodeForm.summary,
          thumbnail: this.nodeForm.thumbnail,
          position_x: parseInt(this.node.x),
          position_y: parseInt(this.node.y),
          // board_idはread_onlyにして送信しないようにしたい
          // board: parseInt(this.$route.params.id),
        },
      })
      .then(() => {})
      .catch(() => {});
      this.$emit(
        "update:node",
        Object.assign(this.node, {
          url: this.nodeForm.url,
          title: this.nodeForm.title,
          thumbnail: this.nodeForm.thumbnail,
          summary: this.nodeForm.summary,
        })
      );
      // this.$emit("update:visible", false);
    },
    handleClickCancelSaveNode() {
      this.$emit("update:visible", false);
    },
    // handleChangeApprover(e) {
    //   // this.nodeForm.approver = this.approvers.filter(i => i.id === parseInt(e.target.value))[0];
    //   this.nodeForm.summary = this.approvers.filter(i => i.id === parseInt(e.target.value))[0];
    // },
  },
  watch: {
    node: {
      immediate: true,
      handler(val) {
        if (!val) {
          return;
        }
        this.nodeForm.id = val.id;
        this.nodeForm.thumbnail = val.thumbnail;
        this.nodeForm.url = val.url;
        this.nodeForm.title = val.title;
        this.nodeForm.summary = val.summary;
        // if (val.approvers && val.approvers.length > 0) {
        //   this.nodeForm.approver = val.approvers[0];
        // }
      },
    },
  },
}
</script>

<style src="./dialog.css"></style>
