<template>

  <div >
    <h1>{{refreshToken}}</h1>
    <van-checkbox v-model="checked">复选框</van-checkbox>
    <van-button type="default" @click="changeToken">默认按钮</van-button>


    <div class="panel-container">
      <h1>商铺名称</h1>
    </div>


    <div class="container" style="margin: 0 auto">
       <div class="card" v-for="x in 30">
         <img class="img-card" src="//pic.xiami.net/images/album/img45/91/5c7b9691b98be_4557445_1551603345.jpg?x-oss-process=image/resize,limit_0,s_410,m_fill/quality,q_80" alt="">
       </div>
    </div>
    <div class="main">
      <div class="h1">
        <div ref="h1"><input type="text" v-model="msg"></div>
      </div>
      <div class="h2">
        <div ref="h2"><input type="text" v-model="msg1"></div>
      </div>
      <div class="h3">
        <div>
          <van-checkbox @click="onAllCheckClick" v-model="allChecked">全选</van-checkbox>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { Checkbox, CheckboxGroup, Button, Toast } from 'vant'
  import { mapState, mapMutations } from 'vuex'

  export default {
    name: 'Chat',
    components: {
      [CheckboxGroup.name]: CheckboxGroup,
      [Checkbox.name]: Checkbox,
      [Button.name]: Button,
      [Toast.name]: Toast,
    },
    data () {
      return {
        checked: 0,
        activeKey: 0,
        msg: null,
        msg1: null,
        count: 0
      }
    },
    computed: {
      allChecked () {
        return this.msg == this.msg1 ? true : false
      },
      ...mapState(['accessToken', 'refreshToken'])
    },
    methods: {
      ...mapMutations(['RecordRefreshToken']),
      onChange (key) {
        this.activeKey = key
      },
      onAllCheckClick () {
      },
      changeToken () {
        this.RecordRefreshToken('i change token' + this.count++)
      }
    }
  }
</script>

<style scoped lang="scss">
  * {
  }

  .box1 {
    width: 100%;
    height: 700px;
    background-color: aliceblue;

  }

  .box2 {
    position: absolute;
    width: 80%;
    height: 200px;
    margin-top: 30px;
    background-color: silver;
  }
.container{
  display: flex;
  flex-wrap: wrap;
  justify-content: start;
}
  .main {
    position: fixed;
    left: 0;
    bottom: 50px;
    display: flex;
    width: 100%;
    height: 50px;
    justify-content: space-between;
    align-items: center;
    z-index: 9999;
    opacity: 1;
    background-color: #ffffff;

    .h1 {
      flex-grow: 1;
    }

    .h2 {
      flex-grow: 1;
    }

    .h3 {
      flex-grow: 2;
    }
  }
</style>
