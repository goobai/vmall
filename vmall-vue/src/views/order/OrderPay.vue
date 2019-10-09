<template>
  <div>
    <HeaderTop title="收银台"> head</HeaderTop>
    <div class="price center-hv card">￥{{price}}</div>
    <div class="card">
      <van-radio-group v-model="radio">
        <div class="pay-icon-container">
          <div class="pay-icon">
            <div class="icon">
              <font-awesome-icon class="iconweixin" :icon="['fab','weixin']"/>
            </div>
            <div class="text"> 微信</div>
          </div>
          <van-radio slot="right-icon" name="1"/>
        </div>

        <div class="pay-icon-container">
          <div class="pay-icon">
            <div class="icon">
              <font-awesome-icon class="iconalipay" :icon="['fab','alipay']"/>
            </div>
            <div class="text"> 支付宝</div>
          </div>
          <van-radio slot="right-icon" name="2"/>
        </div>

      </van-radio-group>
    </div>

    <div class="pay-bottom-wrapper">
      <van-button size="large" type="danger" @click="OnPay">立即支付：￥{{price}}</van-button>
    </div>
  </div>
</template>

<script>
  import {Button, Toast, RadioGroup, Radio, CellGroup, Cell} from 'vant'
  import HeaderTop from '../header/HeaderTop'

  export default {
    name: 'OrderPay',
    components: {
      HeaderTop,
      [Button.name]: Button,
      [RadioGroup.name]: RadioGroup,
      [Radio.name]: Radio,
      [CellGroup.name]: CellGroup,
      [Cell.name]: Cell,
      [Toast.name]: Toast,
    },
    data() {
      return {
        price: 500050005000,
        radio: '1',
        icon: {
          active: 'https://img.yzcdn.cn/vant/user-active.png',
          inactive: 'https://img.yzcdn.cn/vant/user-inactive.png'
        },
      }
    },

    methods: {
      OnPay() {
        this.$toast("正在付款中....")
      }
    },
  }
</script>

<style scoped lang="scss">
  @import '../../style/mixin';

  .price {
    font-weight: 600;
    font-size: 20px;
    color: #e93b3d;
    height: 30px;
  }

  .pay-icon-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 30px;

    .pay-icon {
      display: flex;

      .icon {
        font-size: 18px;
        color: #eb3c3c;
        display: flex;
        align-items: center;
        justify-content: center;
        padding-right: 10px;

      }

      .text {
        font-size: 12px;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
        padding-right: 10px;
      }
    }
  }

  .iconalipay {
    @include sc(16px, rgb(90, 158, 247));
  }

  .iconweixin {
    @include sc(16px, rgb(0, 200, 0))
  }

  .pay-bottom-wrapper {
    position: fixed;
    left: 0;
    bottom: 0;
    right: 0;
    padding: 2px;
  }

  .iconfont {
    width: 1em;
    height: 1em;
    vertical-align: -0.15em;
    fill: currentColor;
    overflow: hidden;

  }


</style>
