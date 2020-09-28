<template>
    <div>
        <div class="modal" v-if="visible">
            <div class="header">
                <span>Edit</span>
            </div>
            <div class="body">
                <label for="name">Name</label>
                <input id="name" class="form-control" v-model="connectionForm.name"/>
                <label for="type">Type</label>
                <select id="type" class="form-control" v-model="connectionForm.type">
                    <option :key="'connection-type-' + item.id"
                            v-for="item in [ { name: 'Pass', id: 'pass' }, { name: 'Reject', id: 'reject' } ]"
                            :value="item.id">
                        {{item.name}}
                    </option>
                </select>
            </div>
            <div class="footer">
                <button @click="deleteConnection()">Delete</button>
                <button @click="handleClickCancelSaveConnection">Cancel</button>
                <button @click="handleClickSaveConnection">Ok</button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

  export default {
    props: {
      visible: {
        type: Boolean,
        default: false,
      },
      connection: {
        type: Object,
        default: null,
      },
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
          expression: null,
        },
      };
    },
    methods: {
      async handleClickSaveConnection() {
        const URL_BASE = 'https://131994d0-4681-4385-92ea-5a73eeb84363.mock.pstmn.io/arrow/update';
        axios({
          method: 'POST',
          url: URL_BASE,
          data: {
            "arrow_id": 5,
            "from_id": 35,
            "to_id": 36,
            "label": "CO2の異常な濃度上昇",
            "board_id": 123,
            "arrow_type_id": 1,
          }
        }).then((res) => {
          console.dir(res.data);
          console.log(res.data.arrow_id);
        }).catch((err) => {
          console.log('ERROR!! occurred in Backend.')
          console.log(err)
        });

        this.$emit('update:visible', false);
        this.$emit('update:connection', Object.assign(this.connection, {
          name: this.connectionForm.name,
          type: this.connectionForm.type,
          expression: this.connectionForm.expression,
        }));
      },

      deleteConnection() {
        // const URL_BASE = 'http://127.0.0.1:8000/newsapp/get';
        const URL_BASE = 'https://131994d0-4681-4385-92ea-5a73eeb84363.mock.pstmn.io/arrow/delete';
        return axios({
          method: 'DELETE',
          url: URL_BASE,
          data: {
            "arrow_id": 45,
          },
        }).then((res) => {
          console.dir(res.status);
          // console.log(res.data.board_id);
        }).catch((err) => {
          console.log('ERROR!! occurred in Backend.')
          console.log(err)
        });
    },

      async handleClickCancelSaveConnection() {
        this.$emit('update:visible', false);
      },
    },
    watch: {
      connection: {
        immediate: true,
        handler(val) {
          if (!val) { return; }
          this.connectionForm.id = val.id;
          this.connectionForm.type = val.type;
          this.connectionForm.name = val.name;
          this.connectionForm.expression = val.expression;
        },
      },
    },
  };
</script>

<style src="./dialog.css"></style>
