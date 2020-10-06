<template>
  <div>
    <div class="modal_arrow" v-if="visible">
      <div class="body">
        <div class="form-allControl">
          <label for="name">Name</label>
          <input
            id="name"
            class="form-control form-arrowNameControl"
            v-model="connectionForm.name"
          />
        </div>
        <div class="form-arrowControl">
          <label for="type">Type</label>
          <select
            id="type"
            class="form-control form-arrowTypeControl"
            v-model="connectionForm.type"
          >
            <option
              :key="'connection-type-' + item.id"
              v-for="item in [
                { name: 'Pass', id: 'pass' },
                { name: 'Reject', id: 'reject' }
              ]"
              :value="item.id"
            >
              {{ item.name }}
            </option>
          </select>
        </div>
      </div>
      <div class="footer">
        <button @click="handleClickCancelSaveConnection">Cancel</button>
        <button id="btn" class="btn_delete" @click="deleteConnection()">
          <p class="text_delete">Delete</p>
        </button>
        <button id="btn" class="btn_save" @click="handleClickSaveConnection">
          <p class="text_save">Save</p>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    visible: {
      type: Boolean,
      default: false
    },
    connection: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      connectionForm: {
        type: null,
        sourceId: null,
        sourcePosition: null,
        destinationId: null,
        destinationPosition: null,
        name: null,
        expression: null
      }
    };
  },
  methods: {
    async handleClickSaveConnection() {
      const URL_BASE =
        "http://127.0.0.1:8000/api/arrows/" + this.connection.id + "/";
      console.log(parseInt(this.connection.source.id));
      console.log(this.connection.source.position);
      console.log(parseInt(this.connection.destination.id));
      console.log(this.connection.destination.position);
      console.log(1);
      console.log(this.connectionForm.name);
      console.log(parseInt(this.$route.params.id));
      axios({
        method: "PUT",
        url: URL_BASE,
        data: {
          from_card: parseInt(this.connection.source.id),
          from_position: this.connection.source.position,
          to_card: parseInt(this.connection.destination.id),
          to_position: this.connection.destination.position,
          arrow_type: 1,
          // arrow_type: {
          //   id: 1,
          //   type: "片方向矢印"
          // },
          label: this.connectionForm.name,
          board_id: parseInt(this.$route.params.id)
        }
      })
        .then(res => {
          console.log('PUT成功');
          console.dir(res.data);
          console.log(res.data.arrow_id);
        })
        .catch(err => {
          console.log("ERROR!! occurred in Backend.");
          console.log(err);
        });

      this.$emit("update:visible", false);
      this.$emit(
        "update:connection",
        Object.assign(this.connection, {
          name: this.connectionForm.name,
          type: this.connectionForm.type,
          expression: this.connectionForm.expression
        })
      );
    },

    deleteConnection() {
      // const URL_BASE = 'http://127.0.0.1:8000/newsapp/get';
      const URL_BASE =
        "https://131994d0-4681-4385-92ea-5a73eeb84363.mock.pstmn.io/arrow/delete";
      return axios({
        method: "DELETE",
        url: URL_BASE,
        data: {
          arrow_id: 45
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

    async handleClickCancelSaveConnection() {
      this.$emit("update:visible", false);
    }
  },
  watch: {
    connection: {
      immediate: true,
      handler(val) {
        if (!val) {
          return;
        }
        this.connectionForm.id = val.id;
        this.connectionForm.type = val.type;
        this.connectionForm.name = val.name;
        this.connectionForm.expression = val.expression;
      }
    }
  }
};
</script>

<style src="./dialog.css"></style>
