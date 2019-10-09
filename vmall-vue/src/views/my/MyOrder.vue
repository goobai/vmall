<template>
  <div>
    <HeaderTop title="我的订单"></HeaderTop>
    <div>

      <van-tabs swipeable sticky type="line" v-model="activeStatus" @change="onChange()">
        <van-tab v-for="keys in tabNames" :title="keys.key" :name="keys.value">
          <div class="card" v-for="(order,index) in orderList" :key="index">
            <div class="flex-jc-sb">
              <div class="shop">
              <font-awesome-icon class="icon" :icon="['fa','store']"/>
                <span class="text">{{order.products[0].shop_name}}</span></div>
              </div>
              <div class="order-status">{{showOrderStatus(order.order_status)}}</div>

            <div>
              <div class="product-card" v-for="(product,index) in order.products" :key="index">
                <div>
                  <img class="img-card"
                       :src="product.img"
                       alt="">
                </div>
                <div class="p-info">
                  <div class="p-name">{{product.sku_name}}</div>
                  <div class="flex-jc-sb">
                    <span>￥ {{product.price}}</span>
                    <span>x{{product.count}}</span>
                    <span>￥{{product.total_price}}</span>

                  </div>
                </div>
              </div>
            </div>
          </div>
        </van-tab>
      </van-tabs>

    </div>
  </div>
</template>

<script>
  import HeaderTop from '../header/HeaderTop'
  import {Button, Tab, Tabs, List} from 'vant'
  import {mapState} from 'vuex'

  export default {
    name: 'MyOrder',
    components: {
      HeaderTop,
      [Button.name]: Button,
      [Tab.name]: Tab,
      [Tabs.name]: Tabs,
    },
    data() {
      return {
        orderList: [],
        loading: false,
        finished: false,
        activeStatus: 0,
        orderStatus: 0,
        orderOffset: 0,
        params: {accessToken: '', orderStatus: 0, offset: 0},
        tabNames: [{
          key: '全部',
          value: 1,
        }, {
          key: '待付款',
          value: 2,
        }, {
          key: '待收货',
          value: 3,
        }, {
          key: '已完成',
          value: 4,
        }, {
          key: '已取消',
          value: 5,
        }]
      }
    },
    methods: {
      onChange() {
        if (this.activeStatus == 1) {
          this.orderStatus = 5
        } else if (this.activeStatus == 2) {
          this.orderStatus = 0
        } else if (this.activeStatus == 3) {
          this.orderStatus = 2
        } else if (this.activeStatus == 4) {
          this.orderStatus = 3
        } else {
          console.log()
        }
        this.getOrders()
        console.log(this.activeStatus)
      },
      showOrderStatus(status) {
        switch (status) {
          //订单状态状态 0:生成订单，待付款 ；1：付款完成，待发货；2：发货完成，物流中，待收货 ；3：收货，待评价 4：评价完商品，订单完成 5：已取消
          case 0:
            return '待付款'
            break
          case 1:
            return '待发货'
            break
          case 2:
            return '待收货'
            break
          case 4:
            return '已完成'
            break
          case 5:
            return '已取消'
            break
        }
      },
      getOrders() {
        this.params.offset = this.offset
        this.params.orderStatus = this.orderStatus
        this.orderList = []
        this.orderOffset = 0
        this.$api.getMyOrder(this.params).then(res => {
          if (res.code == 1) {
            this.orderList = res.data
          } else if (res.code == 0) {
            this.$toast(res.msg)
          } else {
            this.$toast('订单信息请求失败！')
          }
        })

      }
    },
    created() {
      this.getOrders()
    },
    computed: {
      ...mapState(['accessToken', 'login']),

    }
  }
</script>

<style scoped lang="scss">
  @import '../../style/mixin';

  .order-status {
    color: #e93b3d;
  }
</style>
