<template>
  <div>
    <div class="modal" v-if="visible">
      <!-- <div class="header">
        <span>Edit</span>
      </div> -->
      <div class="thumbnail">
        <img
          :src="nodeForm.thumbnail"
          alt=""
          style="width: 100%; border-radius: 10px 10px 0px 0px;"
        />
      </div>
      <div class="body">
        <!-- <input class="form-control" v-model="nodeForm.thumbnail"/> -->
        <label for="url">URL</label>
        <div style="display: flex;">
          <input class="form-urlControl" id="url" v-model="nodeForm.url" />
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
            rows="5"
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
// import '../assets/modal.css';
// Ajax通信ライブラリ
import axios from "axios";

export default {
  props: {
    visible: {
      type: Boolean,
      // default: false,
      default: true
    },
    node: {
      type: Object,
      default: null
    }
  },
  data: function() {
    return {
      nodeForm: {
        id: null,
        url: null,
        title: null,
        summary: null,
        thumbnail: null
      }
      // nodeForm: {name: null, id: null, type: null, approver: []},
      // approvers: [{id: 1, name: 'Joyce'}, {id: 2, name: 'Allen'}, {id: 3, name: 'Teresa'}],
    };
  },
  methods: {
    deleteNode() {
      // const URL_BASE = 'http://127.0.0.1:8000/newsapp/get';
      const URL_BASE =
        "https://131994d0-4681-4385-92ea-5a73eeb84363.mock.pstmn.io/card/delete";
      return axios({
        method: "DELETE",
        url: URL_BASE,
        data: {
          card_id: 45
        }
      })
        .then(res => {
          console.dir(res.status);
          // console.log(res.data.board_id);
        })
        .catch(err => {
          console.log("ERROR!! occurred in Backend.");
          console.log(err);
        });
    },

    handleClickGetInfo() {
      // const URL_BASE = 'http://127.0.0.1:8000/newsapp/get';
      const URL_BASE =
        "https://131994d0-4681-4385-92ea-5a73eeb84363.mock.pstmn.io/card/scrape";
      console.log(this.nodeForm.url);
      return axios({
        method: "POST",
        url: URL_BASE,
        data: {
          url: this.nodeForm.url
        }
      })
        .then(res => {
          console.dir(res.data);
          console.log(res.data.card_title);
          this.nodeForm.thumbnail = res.data.card_thumbnail;
          this.nodeForm.title = res.data.card_title;
          this.nodeForm.summary = res.data.card_summary;
        })
        .catch(err => {
          console.log("ERROR!! occurred in Backend.");
          console.log(err);
        });
    },
    // save押下時に実行される
    handleClickSaveNode() {
      const URL_BASE =
        "https://131994d0-4681-4385-92ea-5a73eeb84363.mock.pstmn.io/card/update";
      axios({
        method: "POST",
        url: URL_BASE,
        data: {
          card_id: 23,
          card_url: "https://www.econetworks.jp/translationtips/2019/12/cri/",
          card_title: "気候変動の影響、日本が世界一に",
          card_summary:
            "日本は世界で最も温暖化による人命危機が及びやすい国である。",
          card_thumbnail:
            "https://www.germanwatch.org/sites/germanwatch.org/files/2019-12/climate_risk_index_2020_world_map_ranking_2018.jpg"
        }
      })
        .then(res => {
          console.dir(res.data);
          console.log(res.data.card_id);
        })
        .catch(err => {
          console.log("ERROR!! occurred in Backend.");
          console.log(err);
        });

      console.log("koko");
      this.$emit(
        "update:node",
        Object.assign(this.node, {
          url: this.nodeForm.url,
          title: this.nodeForm.title,
          thumbnail: this.nodeForm.thumbnail,
          summary: this.nodeForm.summary
        })
      );
      // console.log(this.nodeForm.url);
      this.$emit("update:visible", false);
    },
    handleClickCancelSaveNode() {
      this.$emit("update:visible", false);
    }
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
      }
    }
  }
};
</script>

<style src="./dialog.css"></style>
