<template>
  <div>
    <van-cell-group>
      <van-field
        v-model="username"
        label="用户名"
        placeholder="请输入用户名"
        required
        clearable
      />

      <van-field
        v-model="password"
        type="password"
        label="密码"
        placeholder="请输入密码"
        required
      />
      <van-field
        v-model="password1"
        type="password"
        label="密码"
        placeholder="请再次输入密码"
        required
      />
      <van-field
        v-model="phone"
        label="手机"
        placeholder="你的手机号"
        required
      />
      <van-field
        v-model="sms"
        label="短信验证码"
        placeholder="请输入短信验证码"
        clearable
        required
      >
        <van-button slot="button" size="small" type="info">发送验证码</van-button>
      </van-field>
    </van-cell-group>
    <van-row>
      <van-button @click="onClickReg" type="info" size="large">注册账号</van-button>
    </van-row>
  </div>
</template>

<script>

export default {
  name: 'Register',
  data () {
    return {
      username: 'goobai',
      password: '1',
      password1: '1',
      sms: '1',
      phone: '15208177009',
      reResult: null
    }
  },
  methods: {
    onClickReg() {
      if ((this.password == this.password1) & this.username != '' & this.sms != '') {
        this.$api.userReg(this.username, this.password, this.phone, this.sms).then(res=>{
          if (res.code == 1) {
          this.$toast({
            mask: true,
            type: 'success',
            duration: 1000, // 持续展示 toast
            forbidClick: true, // 禁用背景点击
            message: '注册成功'
          })
          this.$router.push({ name: 'MyCenter' })
        } else {
          this.$toast({
            mask: true,
            type: 'fail',
            duration: 2000, // 持续展示 toast
            forbidClick: true, // 禁用背景点击
            message: '注册失败：' + res.msg
          })
        }
        })
      } else {
        this.$toast('账号或者密码格式不正确')
      }
    }
  }
}
</script>

<style scoped>

</style>
