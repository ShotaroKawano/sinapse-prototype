<template>
  <div>
    <div class="modal" v-if="visible">
      <div class="thumbnail">
        <img :src="nodeForm.thumbnail" alt="" class="box_thumbnail" />
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
          ></textarea>
        </div>
      </div>
      <div class="footer">
        <button id="btn" @click="handleClickCancelSaveNode">
          <p>Cancel</p>
        </button>
        <button id="btn" class="btn_delete" @click="deleteNode">
          <p class="text_delete">Delete</p>
        </button>
        <button id="btn" class="btn_save" @click="handleClickSaveNode">
          <p class="text_save">Save</p>
        </button>
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
      // nodeForm: {name: null, id: null, type: null, approver: []},
      // approvers: [{id: 1, name: 'Joyce'}, {id: 2, name: 'Allen'}, {id: 3, name: 'Teresa'}],
    };
  },
  methods: {
    deleteNode() {
      // TODO: 画面上のカードもdelete
      const tail = "api/cards/" + this.node.id + "/";
      this.$axios({
        method: "DELETE",
        url: tail,
      })
        .then((res) => {
          console.dir(res.status);
          // console.log(res.data.board_id);
          this.$emit("myremove", this.node);
          console.log("発火");
          this.$emit("update:visible", false);
        })
        .catch((err) => {
          console.log("ERROR!! occurred in Backend.");
          console.log(err);
        });
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
        console.dir(res.data);
        this.nodeForm.thumbnail = res.data.soup_img;
        this.nodeForm.title = res.data.soup_title;
        this.nodeForm.summary = res.data.soup_desc;
      })
      .catch((err) => {
        console.log("ERROR!! occurred in Backend.");
        console.log(err);
      });
    },
    // save押下時に実行される
    handleClickSaveNode() {
      // console.log(this.nodeForm.url)
      // console.log(this.nodeForm.title)
      // console.log(this.nodeForm.summary)
      // console.log(this.nodeForm.thumbnail)
      // console.log(parseInt(this.node.x))
      // console.log(parseInt(this.node.y))
      // console.log(parseInt(this.$route.params.id))
      const tail = "api/cards/" + this.node.id + "/";
      this.$axios({
        method: "PUT",
        url: tail,
        data: {
          // url: this.nodeForm.url,
          // title: this.nodeForm.title,
          // summary: this.nodeForm.summary,
          // thumbnail: this.nodeForm.thumbnail,
          // position_x: 1,
          // position_y: 1,
          // board: 2
          url: this.nodeForm.url,
          title: this.nodeForm.title,
          summary: this.nodeForm.summary,
          thumbnail: this.nodeForm.thumbnail,
          position_x: parseInt(this.node.x),
          position_y: parseInt(this.node.y),
          // board_idはread_onlyにして送信しないようにしたい
          board: parseInt(this.$route.params.id),
        },
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.log("ERROR!! occurred in Backend.");
          console.log(err);
        });

      this.$emit(
        "update:node",
        Object.assign(this.node, {
          url: this.nodeForm.url,
          title: this.nodeForm.title,
          thumbnail: this.nodeForm.thumbnail,
          summary: this.nodeForm.summary,
        })
      );
      // console.log(this.nodeForm.url);
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
