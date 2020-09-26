<template>
  <!-- ▼▼▼▼▼ board_title ▼▼▼▼▼ -->
  <div class="section s_01" style="width: 100%; z-index: 0">
    <div class="accordion_one">
      <!-- ▼▼▼ accordion_header ▼▼▼ -->
      <div class="accordion_header" style="display: flex" ref="accordion_header">
        <div
          class=""
          style="
            overflow-wrap: break-word;
            height: 84px;
            width: 684px;
            font-size: 36px;
            line-height: 38px;
            margin: 10px 0px 5px 0px;
          "
        >
          気候変動の影響による日本の危険性と今できること
        </div>
        <div class="">
          <div
            id="btn"
            class="menu"
            style="width: 70px; margin-top: 50px; color: #b4bdc6"
          >
            ▼
          </div>
        </div>
      </div>
      <!-- ▼▼▼ accordion_inner ▼▼▼ -->
      <div class="accordion_inner" ref="accordion_inner">
        <div class="" style="display: flex">
          <div class="">
            <div class="" style="width: 684px">
              <div style="display: flex">
                <div
                  class=""
                  style="
                    height: 160px;
                    font-size: 20px;
                    line-height: 30px;
                    width: 500px;
                    color: #525e6a;
                  "
                >
                  『世界気候リスク指数2020』によると、気候変動によりもっとも人命に危機が及ぶ可能性が高い国が日本とされています。<br />本記事では温暖化のメカニズムと、私たちが今できるもっとも手軽で効果的な対策を紹介しています。
                </div>
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
                  display: flex;
                  width: 684px;
                  color: #b4bdc6;
                  margin-top: 20px;
                "
                class=""
              >
                <div class="">#気候変動、</div>
                <div class="">#地球温暖化、</div>
                <div class="">#自然電力</div>
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
                          2020/09/20
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
                        <div class="" style="color: #b4bdc6">000</div>
                      </div>
                      <div id="btn" class="" style="margin: 0px 14px">
                        <img
                          class="icon_indexBoards"
                          src="@/assets/images/icons/icons_comment.png"
                          alt="コメントボタン"
                          style="padding-left: 5px; margin: 5px 0px 5px 0px"
                        />
                        <div class="" style="color: #b4bdc6">000</div>
                      </div>
                      <div id="btn" class="" style="margin: 0px 14px">
                        <img
                          class="icon_indexBoards"
                          src="@/assets/images/icons/icons_share.png"
                          alt="シェアボタン"
                          style="padding-left: 5px; margin: 5px 0px 5px 0px"
                        />
                        <div class="" style="color: #b4bdc6">000</div>
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
              <p style="font-size: 14px; color: #525e6a">Delet</p>
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
              <p style="font-size: 14px; color: #ffffff">Save</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- ▲▲▲▲▲ board_title ▲▲▲▲▲ -->
</template>

<script>
export default {
  name: 'BoardHeader',
  mounted: function () {
        $('.s_01 .accordion_one .accordion_header').click(function () {
        // クリックされた.accordion_oneの中の.accordion_headerに隣接する.accordion_innerが開いたり閉じたりする。
        $(this).next('.accordion_inner').slideToggle()
        $(this).toggleClass('open')
        console.log($(this));
      })
    // toggleBoarHeader () {
      // console.log(this);
      // this.$ref.accordion_inner
    //   $(this).next('.accordion_inner').slideToggle()
    //   $(this).toggleClass('open')
    // }
  }
}
</script>

<style>
  .board_thumbnail {
    width: 150px;
    height: 150px;
    border-radius: 10px;
    border: solid 1px #e1e6eb;
    background-image: url('../assets/images/treediagram.png');
    background-size: cover;
    margin-left: 20px;
  }
</style>
