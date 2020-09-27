<template>
      <!-- ▼▼▼▼▼ header ▼▼▼▼▼ -->
    <!-- じんさんのコンポーネントを再利用 -->
    <div id="header" class="box_header" style="z-index: 1">
      <a id="btn" class="name_service" href="login.html">Sinapse</a>
      <input
        type="search"
        class="input_search"
        placeholder="🔍キーワード、#ハッシュタグを入力..."
      />
      <div id="btn">
        <img
          class="btn_headerUser"
          src="@/assets/images/userimages/user00.jpg"
          alt="プロフィール画像"
        />
      </div>
      <div class="btn_create">
        <p>✏︎ 投稿</p>
      </div>
    </div>
    <!-- ▲▲▲▲▲ header ▲▲▲▲▲ -->
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style>

</style>
