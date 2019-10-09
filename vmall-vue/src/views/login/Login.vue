<template>
  <div>
    <van-cell-group>
      <van-field
        v-model="username"
        required
        clearable
        label="用户名"
        placeholder="请输入用户名"
      />

      <van-field
        v-model="password"
        type="password"
        label="密码"
        placeholder="请输入密码"
        required
      />

    </van-cell-group>
    <van-row>
      <van-button type="info" size="large" @click="onLoginClick">登陆</van-button>
    </van-row>
  </div>
</template>

<script>
  import {mapMutations,mapState} from 'vuex'

  export default {
    name: 'Login',
    data() {
      return {
        username: 'goobai',
        password: '1'
      }
    },
    methods: {
      ...mapMutations(['RecordAccessToken', 'RecordRefreshToken', 'RecordLoginState', 'RecordUserInfo']),
      onLoginClick() {
        localStorage.removeItem('userInfo')
        if (this.username != '' & this.password != '') {
          this.$api.userLogin(this.username, this.password).then(res => {
              if (res.code == 1) {
                // localStorage.setItem('info', JSON.stringify(this.reResult.data.user_info))
                // localStorage.setItem('accessToken', JSON.stringify(this.reResult.data.access_token))
                // localStorage.setItem('refreshToken', JSON.stringify(this.reResult.data.refresh_token))
                this.RecordRefreshToken(res.data.refresh_token)
                this.RecordAccessToken(res.data.access_token)
                this.RecordLoginState(true)
                this.RecordUserInfo(res.data.user_info)
                this.$toast({
                  mask: true,
                  type: 'success',
                  duration: 1000, // 持续展示 toast
                  forbidClick: true, // 禁用背景点击
                  message: '登陆成功'
                })
                try {
                  if (this.$route.query.redirect) {
                    let url = decodeURIComponent(this.$route.query.redirect)
                    console.log(url)
                    this.$router.push({path: url});

                  } else {
                    this.$router.push({path: '/'});

                  }

                } catch (err) {
                  this.$router.push({path: '/'});

                }
              } else {
                this.$toast({
                  mask: true,
                  type: 'fail',
                  duration: 2000, // 持续展示 toast
                  forbidClick: true, // 禁用背景点击
                  message: '登陆失败：' + res.msg
                })
              }
            }
          )

        } else {
          this.$toast('账号或者密码格式不正确')
        }
      }
    },
    computed: {
      ...mapState['login']
    }
  }
</script>

<style scoped>

</style>
