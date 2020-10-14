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
                <input
                  v-model="email"
                  type="email"
                  class="input_loginEmail"
                  placeholder="Email"/>
              </div>
              <div class="box_loginPassword">
                <input
                  v-model="password"
                  type="password"
                  class="input_loginPassword"
                  placeholder="Password"
                />
              </div>
              <div id="btn" class="login_passInfo" >パスワードを忘れた方はこちら</div>
              <!-- <input class="btn_login" type="submit" value="ログイン" /> -->
              <div class="btn_login" @click="submit">ログイン</div>
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
  data: function () {
    return {
      email: null,
      password: null,
    }
  },
  methods: {
    submit() {
      this.$axiosAuth({
        method: "POST",
        url: 'login/',
        data: {
          email: this.email,
          password: this.password
        },
      })
      .then((res) => {
        console.log(res.data)
        this.$axios.defaults.headers.common['Authorization'] = `JWT ${res.data.token}`
        this.$router.push('/')
      })
      .catch(() => {})
    }
  }
}
</script>

<style src="@/assets/css/login.css"></style>
