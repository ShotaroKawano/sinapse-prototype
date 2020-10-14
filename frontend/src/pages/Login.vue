<template>
    <div id="body">
      <div class="center_objecto">
        <!-- ▼▼▼▼▼ authentication ▼▼▼▼▼ -->
        <div id="" class="" >
          <!-- <img class="serviceLogo"
            src="../frontend/src/assets/images/logos/logos_Sinapse.png"
            alt="Sinapselogo" />  -->
          <p class="name_service">Sinapse</p>
        </div>
        <div>
          <!-- ▼▼▼ email login ▼▼▼ -->
          <form action="xxx.php" method="post">
              <div class="box_loginEmail">
                <input type="email" class="input_loginEmail" placeholder="Email"/>
              </div>
              <div class="box_loginPassword">
                <input type="password" class="input_loginPassword" placeholder="Password"/>
              </div>
              <div id="btn" class="login_passInfo" >パスワードを忘れた方はこちら</div>
              <!-- <input class="btn_login" type="submit" value="ログイン" /> -->
              <a class="btn_login" href="http://localhost:8080/">ログイン</a>
              <div id="btn" class="login_signupInfo" >新規登録</div>
          </form>
          <!-- ▲▲▲ email login ▲▲▲ -->
        </div>
        <!-- ▲▲▲▲▲ authentication ▲▲▲▲▲ -->
      </div>
    </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    submit() {
      alert('login!')
    }
  }
}
</script>

<style src="@/assets/css/login.css"></style>
