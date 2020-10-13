<template>
  <div>
    <div class="modal" v-if="visible">
      <div class="thumbnail">
        <!-- <img :src="nodeForm.thumbnail" alt="" class="box_thumbnail" /> -->
        <img
          v-if="!isEditting"
          @click="isEditting = !isEditting"
          :src="nodeForm.thumbnail"
          alt="No image"
          class="box_thumbnail"
        />
        <input
            v-if="isEditting"
            @focusout="isEditting = !isEditting"
            type="url"
            class="form-urlControl"
            id="thumbnail"
            v-model="nodeForm.thumbnail"
        />
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
            placeholder="URL"
          />
          <button id="btn" class="btn_get" @click="handleClickGetInfo">
            <p class="text_get">Get</p>
          </button>
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
            placeholder="Title"
          ></textarea>
        </div>

        <div class="form-allControl">
          <label for="summary">Summary</label>
          <!-- <input class="form-control" id="summary" v-model="nodeForm.summary" /> -->
          <textarea
            class="form-summaryControl"
            name="summary"
            id="summary"
            rows="9"
            v-model="nodeForm.summary"
            placeholder="Summary"
          ></textarea>
        </div>
        <div class="box_footerButton">
          <div class="footerButton">
            <button id="btn" style="width: 50px;" @click="handleClickCancelSaveNode">
              <p>Cancel</p>
            </button>
            <div id="btn" class="btn_delete" @click="deleteNode">
              <p class="text_delete">Delete</p>
            </div>
            <div id="btn" class="btn_save" @click="handleClickSaveNode">
              <p class="text_save">Save</p>
            </div>
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
  },

  data: function () {
    return {
      nodeForm: {
        id: null,
        url: null,
        title: null,
        summary: null,
        thumbnail: null,
      },
      isEditting: false
      // nodeForm: {name: null, id: null, type: null, approver: []},
      // approvers: [{id: 1, name: 'Joyce'}, {id: 2, name: 'Allen'}, {id: 3, name: 'Teresa'}],
    };
  },

  methods: {

    deleteNode() {
      this.$emit("handle-delete-node", this.node);
      this.$emit("update:visible", false);
    },

    handleClickGetInfo() {
      // const URL_BASE = 'http://127.0.0.1:8000/newsapp/get';
      const tail = "api/scrape/";
      console.log(this.nodeForm.url);
      this.$axios({
        method: "POST",
        url: tail,
        data: {
          url: this.nodeForm.url,
        },
      })
      .then((res) => {
        this.nodeForm.thumbnail = res.data.soup_img;
        this.nodeForm.title = res.data.soup_title;
        this.nodeForm.summary = res.data.soup_desc;
      })
      .catch(() => {});
    },

    // save押下時に実行される
    handleClickSaveNode() {
      const tail = "api/cards/" + this.node.id + "/";
      this.$axios({
        method: "PATCH",
        url: tail,
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
      this.$emit("update:visible", false);
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
};
</script>

<style src="./dialog.css"></style>
