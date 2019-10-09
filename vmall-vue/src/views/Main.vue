<template>
  <div>
    <div>
      <router-view></router-view>
    </div>
    <div>
      <van-tabbar v-model="active" @change="changeTabbar">
        <van-tabbar-item name="Home" icon="home-o">首页</van-tabbar-item>
        <van-tabbar-item name="ChatHome" icon="chat-o">消息</van-tabbar-item>
        <van-tabbar-item name="Category" icon="bars">分类</van-tabbar-item>
        <van-tabbar-item name="Cart" icon="cart-o">购物车</van-tabbar-item>
        <van-tabbar-item name="MyCenter" icon="user-o">个人中心</van-tabbar-item>
      </van-tabbar>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {}
    },
    methods: {
      changeTabbar(active) {
        if (active) {
          this.$router.push({name: active})
        }
      }
    },
    computed: {
      active: {
        get(){
          return  this.$route.name

        },
        set(value){
        }
      }
    }

  }
</script>

<style scoped>

</style>
