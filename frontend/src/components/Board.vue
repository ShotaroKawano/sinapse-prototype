<template>
  <div>
    <BoardHeader
      @update-is-author="handleUpdateAuthor"
      :isAuthor="isAuthor"
    >
    </BoardHeader>
    <div class="container">
      <!-- <div id="toolbar"> -->
      <!-- positionを渡さないaddだったのか -->
      <!-- <button @click="handleDblClick">
          Add(Double-click canvas)
        </button> -->
      <!-- <button
          @click="
            $refs.chart.add({
              id: +new Date(),
              x: 10,
              y: 10,
              url: '',
              title: 'Title',
              summary: 'Summary',
              thumbnail: 'https://placehold.jp/150x100.png',
            })
          "
        >
          Add(Double-click canvas)
        </button> -->
      <!-- <button @click="$refs.chart.remove()">Delete(Del)</button>
        <button @click="$refs.chart.editCurrent()">
          Edit(Double-click node)
        </button>
        <button @click="$refs.chart.save()">Save</button> -->
      <!-- </div> -->
      <!-- <flowchart
        :nodes="nodes"
        :connections="connections"
        @editnode="handleEditNode"
        :readonly="false"
        @dblclick="handleDblClick"
        @editconnection="handleEditConnection"
        @save="handleChartSave"
        ref="chart"
        :render="render"
      >
      </flowchart> -->
      <div class="inner">
        <flowchart
          :nodes="nodes"
          :connections="connections"
          @editnode="handleEditNode"
          :readonly="false"
          @dblclick="handleDblClick"
          @editconnection="handleEditConnection"
          @save="handleChartSave"
          ref="chart"
          :isAuthor="isAuthor"
        >
        </flowchart>
      </div>
      <node-dialog
        :visible.sync="nodeDialogVisible"
        :node.sync="nodeForm.target"
        @handle-delete-node="$refs.chart.removeNode($event)"
        :isAuthor="isAuthor"
        >
        </node-dialog>
      <connection-dialog
        :visible.sync="connectionDialogVisible"
        :connection.sync="connectionForm.target"
        :operation="connectionForm.operation"
        @handle-delete-connection="$refs.chart.removeConnection($event)"
        :isAuthor="isAuthor"
      >
      </connection-dialog>
    </div>
  </div>
</template>

<script>
import ConnectionDialog from "./dialog/ConnectionDialog";
import NodeDialog from "./dialog/NodeDialog";
import Flowchart from "./flowchart/Flowchart";
// import * as d3 from "d3";
// import { roundTo20 } from "../utils/math";
// scriptタグでないと機能しないのか？
import "@/assets/css/reset.css";
import BoardHeader from "./BoardHeader";

export default {
  name: "Board",
  components: {
    ConnectionDialog,
    NodeDialog,
    Flowchart,
    BoardHeader,
  },
  data: function () {
    return {
      // APIとキーを合わせれば代入が楽なのに
      nodes: [
        // {
        //   id: 11,
        //   x: 500,
        //   y: 50,
        //   url: "https://www.econetworks.jp/translationtips/2019/12/cri/",
        //   title: "気候変動の影響、日本が世界一に",
        //   summary:
        //     "日本は世界で最も温暖化による人命危機が及びやすい国である。日本は世界で最も温暖化による人命危機が及びやすい国である。日本は世界で最も温暖化による人命危機が及びやすい国である。日本は世界で最も温暖化による人命危機が及びやすい国である。日本は世界で最も温暖化による人命危機が及びやすい国である。",
        //   thumbnail:
        //     "https://www.germanwatch.org/sites/germanwatch.org/files/2019-12/climate_risk_index_2020_world_map_ranking_2018.jpg",
        // },
        // {
        //   id: 21,
        //   x: 200,
        //   y: 320,
        //   url:
        //     "https://www.ecolosia.jp/2019/10/08/%E7%AC%AC43%E5%9B%9E%E3%82%AF%E3%83%A9%E3%82%A4%E3%83%A1%E3%83%BC%E3%83%88-%E3%83%AA%E3%82%A2%E3%83%AA%E3%83%86%E3%82%A3-%E3%83%AA%E3%83%BC%E3%83%80%E3%83%BC%E3%82%B7%E3%83%83%E3%83%97-%E3%82%B3%E3%83%9F%E3%83%A5%E4%BA%8C%E3%83%86%E3%82%A3-%E3%83%88%E3%83%AC%E3%83%BC%E4%BA%8C%E3%83%B3%E3%82%B0/",
        //   title:
        //     "第43回クライメート・リアリティ・リーダーシップ・コミュ二ティ・トレー二ング",
        //   summary:
        //     "プレゼン画像に注目。この数十年の間に異常なまでにCO2濃度が増加。",
        //   thumbnail:
        //     "https://image.jimcdn.com/app/cms/image/transf/dimension=1920x400:format=jpg/path/s49d62a7e9b605c1c/image/ic5df63fe831d41ec/version/1570517714/image.jpg",
        // },
        // {
        //   id: 22,
        //   x: 800,
        //   y: 320,
        //   url: "https://youtu.be/s87C3jBMC6w",
        //   title: "海面上昇72ｍ!? 私たちが数千年の人類の運命を決める",
        //   summary:
        //     "【2倍速再生推奨】動画でわかりやすく海面上昇のヤバさが解説されている。",
        //   thumbnail: "https://i.ytimg.com/vi/s87C3jBMC6w/maxresdefault.jpg",
        // },
        // {
        //   id: 31,
        //   x: 200,
        //   y: 590,
        //   url: "https://youtu.be/WvX18sbbOwE",
        //   title: "３分でわかる「地球温暖化のメカニズム」",
        //   summary: "3分で端的に地球温暖化のメカニズムを理解できる",
        //   thumbnail: "https://i.ytimg.com/vi/WvX18sbbOwE/hqdefault.jpg",
        // },
        // {
        //   id: 32,
        //   x: 800,
        //   y: 590,
        //   url: "https://www.newsweekjapan.jp/stories/world/2020/07/4-119.php",
        //   title:
        //     "海洋メタンの4分の１が存在する南極から、メタンの活発な放出が確認された",
        //   summary:
        //     "温暖化したら極地の氷山が解ける。氷山が解けると中のメタンガスが大気に盛れる。",
        //   thumbnail:
        //     "https://www.newsweekjapan.jp/stories/assets_c/2020/07/50113628681_bdebc21612_c-thumb-720xauto-208187.jpg",
        // },
        // {
        //   id: 41,
        //   x: 500,
        //   y: 860,
        //   url: "http://daily-ondanka.es-inc.jp/basic/data_09.html",
        //   title: "日本の家庭からの二酸化炭素（CO2）排出量",
        //   summary:
        //     "普段自分たちがどのようにCO2を排出しているかを知ろう。その40％が電力発電からである。",
        //   thumbnail:
        //     "http://daily-ondanka.es-inc.jp/basic/img/i_bsc_data_09_1.gif",
        // },
        // {
        //   id: 51,
        //   x: 50,
        //   y: 1130,
        //   url: "https://hachidori-denryoku.jp/",
        //   title: "ハチドリ電力",
        //   summary: "電気代の1％は社会活動に携わる組織や個人へ",
        //   thumbnail:
        //     "https://hachidori-denryoku.jp/wp-content/uploads/2020/08/share_ogp_new.png",
        // },
        // {
        //   id: 52,
        //   x: 550,
        //   y: 1130,
        //   url: "https://a-eru.co.jp/denki/",
        //   title: "aeru電気",
        //   summary: "電気代の1％は日本の伝統工芸に携わる職人さんへ",
        //   thumbnail: "https://a-eru.co.jp/denki/img/0616_1.png",
        // },
        // {
        //   id: 53,
        //   x: 1050,
        //   y: 1130,
        //   url:
        //     "https://shizendenryoku.jp/?from=gadwse&gclid=Cj0KCQjws536BRDTARIsANeUZ5_NhfYu1Lq8OxSjA_1lXqdBEji_K7Qxqx3f_ZQVp5XT7N9hozArcXwaAgIqEALw_wcB",
        //   title: "自然電力のでんき",
        //   summary: "ハチドリ電力もaeru電気も供給源は自然電力",
        //   thumbnail:
        //     "https://venturetimes.jp/cms/wp-content/uploads/2019/10/8fc2e32322d6fbffacbecb3ac271ea1c.png",
        // },
      ],
      connections: [
        // {
        //   source: { id: 11, position: "left" },
        //   destination: { id: 21, position: "top" },
        //   id: 1,
        //   type: "pass",
        //   name: "CO2の異常な濃度上昇",
        // },
        // {
        //   source: { id: 11, position: "right" },
        //   destination: { id: 22, position: "top" },
        //   id: 2,
        //   type: "pass",
        //   name: "海面上昇について",
        // },
        // {
        //   source: { id: 21, position: "bottom" },
        //   destination: { id: 31, position: "top" },
        //   id: 3,
        //   type: "pass",
        //   name: "CO2と温暖化の関係",
        // },
        // {
        //   source: { id: 22, position: "bottom" },
        //   destination: { id: 32, position: "top" },
        //   id: 4,
        //   type: "pass",
        //   name: "温暖化と海面上昇の連鎖",
        // },
        // {
        //   source: { id: 31, position: "bottom" },
        //   destination: { id: 41, position: "top" },
        //   id: 5,
        //   type: "pass",
        //   name: "まずは電力を切り替えよう",
        // },
        // {
        //   source: { id: 32, position: "bottom" },
        //   destination: { id: 41, position: "top" },
        //   id: 6,
        //   type: "pass",
        //   name: "",
        // },
        // {
        //   source: { id: 41, position: "left" },
        //   destination: { id: 51, position: "top" },
        //   id: 7,
        //   type: "pass",
        //   name: "電気で非営利組織を応援",
        // },
        // {
        //   source: { id: 41, position: "bottom" },
        //   destination: { id: 52, position: "top" },
        //   id: 8,
        //   type: "pass",
        //   name: "電気で日本文化を応援",
        // },
        // {
        //   source: { id: 41, position: "right" },
        //   destination: { id: 53, position: "top" },
        //   id: 9,
        //   type: "pass",
        //   name: "左2つ大元はこの会社",
        // },
      ],
      nodeForm: { target: null },
      connectionForm: { target: null, operation: null },
      nodeDialogVisible: false,
      connectionDialogVisible: false,
      isAuthor: false,
    };
  },
  computed: {
    token() {
      return this.$store.getters.token
    },
    // isAuthor() {
    //   return this.$store.userId === this.userId
    // }
  },
  methods: {
    handleUpdateAuthor(isAuthor) {
      console.log('koko');
      console.log(isAuthor);
      this.isAuthor = isAuthor
    },
    handleDblClick(position) {
      const tail = "api/cards/";
      this.$axios({
        method: "POST",
        url: tail,
        headers: {
          Authorization: `JWT ${this.token}`
        },
        data: {
          url: "nanika",
          title: "Title",
          summary: "Summary",
          // thumbnail: "https://placehold.jp/150x100.png",
          thumbnail: require('@/assets/images/icons/noimage.jpg'),
          position_x: parseInt(position.x),
          position_y: parseInt(position.y),
          // board_idはread_onlyにして送信しないようにしたい
          board: parseInt(this.$route.params.id),
        },
      })
      .then((res) => {
        this.$refs.chart.add({
          // id: +new Date(),
          // id: (new Date()).getTime(),
          id: res.data.id,
          x: position.x,
          y: position.y,
          // thumbnail: "https://placehold.jp/150x100.png",
          thumbnail: require('@/assets/images/icons/noimage.jpg'),
          url: "dummyurl",
          title: "Title",
          summary: "Summary",
        });
      })
      .catch(() => {});
    },
    async handleChartSave(nodes, connections) {
      // axios.post(url, {nodes, connection}).then(resp => {
      //   this.nodes = resp.nodes;
      //   this.connections = resp.connections;
      //   // Flowchart will refresh after this.nodes and this.connections changed
      // });
    },
    handleEditNode(node) {
      this.nodeForm.target = node;
      this.nodeDialogVisible = true;
    },
    handleEditConnection(connection) {
      this.connectionForm.target = connection;
      this.connectionDialogVisible = true;
    },
    // render: function (g, node, isSelected) {
    //   node.width = node.width || 400;
    //   node.height = node.height || 200;

    //   g.append('foreignObject')
    //     .attr("x", node.x)
    //     .attr("y", node.y)
    //     .style("width", node.width * 3 / 8 + "px")
    //     .style("height", node.height / 2 + "px")
    //     .append('xhtml:div')
    //     .style("width", node.width * 3 / 8 + "px")
    //     .style("height", node.height / 2 + "px")
    //     .style("background-image", `url(${node.thumbnail})`)
    //     .style("background-position", "center center")
    //     .style("background-size", "cover")
    //     .style("background-repeat", "no-repeat")
    //     .style("border-radius", "6px 0 0 0")
    //     .style("box-sizing", "border-box")
    //     .style("border-top", "1px solid white")
    //     .style("border-left", "1px solid white")

    //   g.append('foreignObject')
    //     .attr("x", node.x + node.width * 3 / 8)
    //     .attr("y", node.y)
    //     .attr("class", "title")
    //     .style("width", node.width * 5 / 8 + "px")
    //     .style("height", node.height / 2 + "px")
    //     .append('xhtml:div')
    //     .style("width", node.width * 5 / 8 + "px")
    //     .style("height", node.height / 2 + "px")
    //     .style("background-color", "#3F3F3F")
    //     .style("border-radius", "0 6px 0 0")
    //     .style("box-sizing", "border-box")
    //     .style("border-top", "1px solid white")
    //     .style("border-right", "1px solid white")

    //   g.append('foreignObject')
    //     .attr("x", node.x + node.width * 3 / 8)
    //     .attr("y", node.y)
    //     .attr("class", "unselectable")
    //     .style("width", node.width * 5 / 8 + "px")
    //     .style("height", node.height / 2 + "px")
    //     .style("display", "table")
    //     .append('xhtml:p')
    //     .style("display", "table-cell")
    //     .style("vertical-align", "middle")
    //     .style("width", node.width * 5 / 8 + "px")
    //     .style("height", node.height / 2 + "px")
    //     .style("box-sizing", "border-box")
    //     .style("padding", "4px 8px 4px 8px")
    //     .style("color", "white")
    //     .style("font-weight", "bold")
    //     .style("margin", 0)
    //     .style("overflow-wrap", "break-word")
    //     .text(() => node.name)

    //   g.append('foreignObject')
    //     .attr("x", node.x)
    //     .attr("y", node.y + node.height / 2)
    //     .style("width", node.width + "px")
    //     .style("height", node.height / 2 + "px")
    //     .append('xhtml:div')
    //     .style("width", node.width + "px")
    //     .style("height", node.height / 2 + "px")
    //     .style("background-color", "#707070")
    //     .style("box-sizing", "border-box")
    //     .style("border-radius", "0 0 6px 6px")
    //     .style("border-bottom", "1px solid white")
    //     .style("border-right", "1px solid white")
    //     .style("border-left", "1px solid white")

    //   g.append('foreignObject')
    //     .attr("x", node.x)
    //     .attr("y", node.y + node.height / 2)
    //     .attr("class", "unselectable")
    //     .style("width", node.width + "px")
    //     .style("height", node.height / 2 + "px")
    //     .append('xhtml:p')
    //     .style("width", node.width + "px")
    //     .style("height", node.height / 2 + "px")
    //     .style("box-sizing", "border-box")
    //     .style("padding", "4px 8px 4px 8px")
    //     .style("color", "white")
    //     .style("margin", 0)
    //     .style("overflow-wrap", "break-word")
    //     .text(() => node.summary)
    // },
  },
  created: function () {
    const tail =
      "api/cards/?board_id=" + this.$route.params.id;
    this.$axios({
      method: "GET",
      url: tail,
      headers: {
        Authorization: `JWT ${this.token}`
      },
    })
    .then((res) => {
      // this.nodes = [];
      let nodes2 = [];
      for (let i in res.data) {
        console.log(i);
        nodes2.push({
          id: res.data[i]["id"],
          x: res.data[i]["position_x"],
          y: res.data[i]["position_y"],
          thumbnail: res.data[i]["thumbnail"],
          url: res.data[i]["url"],
          title: res.data[i]["title"],
          summary: res.data[i]["summary"],
        });
        this.nodes = nodes2;
        // this.$refs.chart.add(
        //   {
        //     id: res.data[i]['id'],
        //     x: res.data[i]['position_x'],
        //     y: res.data[i]['position_y'],
        //     thumbnail: res.data[i]['thumbnail'],
        //     url: res.data[i]['url'],
        //     title: res.data[i]['title'],
        //     summary: res.data[i]['summary'],
        //   }
        // )
      }
    })
    .catch(() => {});
    const tail2 =
      "api/arrows/?board_id=" + this.$route.params.id;
    this.$axios({
      method: "GET",
      url: tail2,
      headers: {
        Authorization: `JWT ${this.token}`
      },
    })
    .then((res) => {
      // this.nodes = [];
      let connections2 = [];
      for (let i in res.data) {
        console.log(i);
        connections2.push({
          source: {
            id: res.data[i]["from_card"],
            position: res.data[i]["from_position"],
          },
          destination: {
            id: res.data[i]["to_card"],
            position: res.data[i]["to_position"],
          },
          id: res.data[i]["id"],
          type: res.data[i]["arrow_type"]["type"],
          name: res.data[i]["label"],
          // {
          //   source: { id: 11, position: "left" },
          //   destination: { id: 21, position: "top" },
          //   id: 1,
          //   type: "pass",
          //   name: "CO2の異常な濃度上昇",
          // },
        });
        this.connections = connections2;
      }
    })
    .catch(() => {});
  },
};
</script>

<style scoped>
/*  board内に表示されるnodeのCSSは(render.jsにある)  */

/* #toolbar {
  margin-bottom: 10px;
} */

.title {
  margin-top: 10px;
  margin-bottom: 0;
  color: white;
}

.subtitle {
  margin-bottom: 10px;
}

#toolbar > button {
  margin-right: 4px;
}

.container {
  /* width: 800px; */
  /* width: 96%; */
  width: 100%;
  /* min-height: 900px; */
  background-color: #f0f0f0;
  margin: auto;
  min-height: 90vh;
  overflow: auto;
}

.inner {
  width: 200%;
  height: 180vh;
  /* display: inline-block; */
  /* min-width: 100%; */
  /* min-height: 80vh; */
  box-sizing: border-box;
}
</style>
