<template>

  <div class="bg">
    <HeaderTop title="确认订单"> head</HeaderTop>
    <div v-if="login">
      <div id="addressSection" class="card" @click="onAddressClick">
        <div class="fa-icon">
          <font-awesome-icon style="color:#e93b3d" :icon="['fa','map-marker-alt']"/>
        </div>
        <div>
          <span>{{addressInfo.name}}</span> <span>{{addressInfo.tel}}</span>
          <div>{{addressInfo.address}}</div>

        </div>
      </div>

      <div id="productsSection">
        <div v-for="(shop,index ) in products" :key="index">
          <div class="card">
            <div class="shop-list">
              <div>
                <font-awesome-icon style="color: #747296" :icon="['fa','store']"/>
                <span style="margin-left: 10px;font-weight: 500">{{shop.name}}</span></div>
            </div>
            <div v-for="(product,index ) in shop.products" :key="index">
              <div>
                <div class="product-list fss">

                  <div><img :src="product.images[0]" class="img-card"></div>
                  <div class="p-info">
                    <div class="p-name">{{product.name}}</div>
                    <div class="p-count-change space-between">
                      <div class="p-price">￥{{product.price}}.00</div>
                      <div class="p-count">
                        <span>x{{product.count}}</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
      <div id="summarySection">
        <div class="order-container">
          <div class="order-left">
            <span style="font-weight: 600; color: #e93b3d">合计:￥{{totalPrice}}.00</span>
          </div>
          <div class="order-right">
            <van-button type="danger" size="large" @click="onOrderClick">提交订单</van-button>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <van-button type="info" @click="goLoginPage">去登陆</van-button>
    </div>

  </div>
</template>

<script>
  import { Button, Toast } from 'vant'
  import HeaderTop from '../header/HeaderTop'
  import { mapState } from 'vuex'

  export default {
    name: 'ConfirmOrder',
    components: {
      HeaderTop,
      [Button.name]: Button,
      [Toast.name]: Toast,
    },
    data () {
      return {
        shops: [1, 23, , 3],
        products: [],
        addressId: 2,
        addressInfo: {},
        totalPrice: 0
      }
    },
    methods: {
      onAddressClick(){
        this.$router.push({name:"AddressIndex"})
      },
      onOrderClick () {

        this.$toast.loading({
          duration: 3,       // 持续展示 toast
          forbidClick: true, // 禁用背景点击
          loadingType: 'spinner',
          message: '正在处理！'
        })
        this.$api.postOrderProducts(this.products, this.addressId).then(res => {
          if (res.code == 1) {
            this.$router.push({ 'path': '/order/pay' })
          } else if (res.code == 0) {
            this.$toast.clear()
            this.$toast.fail(res.msg)
          } else {
            this.$toast.clear()
            this.$toast.fail('订单提交失败！')
          }
        })

      },
      initData () {

        this.$api.getOrderConfirmData().then(res => {
          if (res.code == 1) {
            this.products = res.data.shops
            this.totalPrice = res.data.totalPrice
          } else {
            this.products = []
          }
          if (this.products.length == 0) {
            this.$router.push('/cart')
          }
          let params={}
          this.$api.getUserAddress(params).then(res => {
            if (res.code == 1) {
              console.log(res.data.address)
              this.addressInfo = res.data
              this.addressId = res.data.id
            } else {
              console.log('获取默认地址失败')
            }
          })
        })

      },
      goLoginPage () {
        this.$router.push('login')
      },
    },
    computed: {
      computePrice () {
        return function (price) {
          return (price / 100).toFixed(2)
        }
      },
      ...mapState(['accessToken', 'login'])
    },
    created () {
      this.initData()
    },
  }
</script>

<style scoped lang="scss">
  #addressSection {
    display: flex;
  }

  #productsSection {
    margin-bottom: 50px;
    height: 100%;
  }

  .fa-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    padding: 0 2px;
    width: 50px;
  }

  .order-container {
    position: fixed;
    left: 0;
    bottom: 0px;
    display: flex;
    width: 100%;
    height: 50px;
    justify-content: space-between;
    align-items: center;
    z-index: 100;
    opacity: 1;
    background-color: #ffffff;

    .order-left {
      display: flex;
      flex-wrap: nowrap;
      justify-content: start;
      flex-grow: 2;
      align-items: center;
    }

    .order-right {
      display: flex;
      flex-grow: 1;
    }
  }

  .space-between {
    width: 100%;
    display: flex;
    justify-content: space-between;
  }
</style>
