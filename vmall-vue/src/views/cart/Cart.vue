<template>
  <div>
    <HeaderTop title="购物车"> this is my head</HeaderTop>
    <div class="card-goods " v-if="login">
      <div>
        <div v-for="(shop,index ) in cartProducts" :key="index" class="card">
          <div>
            <div class="shop-list">
              <div class="checkbox-container">
                <van-checkbox :key="shop.shop_id" :name="shop.shop_id" v-model="shop.checked"
                              @click="onShopCheckBoxClick(shop.shop_id,shop.checked)"></van-checkbox>
              </div>
              <div>
                <font-awesome-icon style="color: #747296" :icon="['fa','store']"/>
                <span style="margin-left: 10px;font-weight: 600">{{shop.name}}</span></div>
            </div>
            <div v-for="(product,index ) in shop.products" :key="index">
              <div>
                <div class="product-list">
                  <div class="checkbox-container">
                    <van-checkbox :key="product.id" :name="product.id" v-model="product.checked"
                                  @click="onProductCheckBoxClick(product.id,product.checked) "></van-checkbox>
                  </div>
                  <div><img :src="product.images[3]" style="width: 80px"></div>
                  <div class="p-info">
                    <div class="p-name" @click="onProductClick(product.id)">{{product.name}}</div>
                    <div class="p-count-change">
                      <div class="p-price">￥{{product.price}}.00</div>
                      <div class="p-count">
                        <div class="count-icon"
                             @click="modifyProductCount(product.id,product.count-1)">
                          <font-awesome-icon style="color: #8b9096"
                                             :icon="['fa','minus']"/>
                        </div>
                        <input type="text" style="font-size: 10px ;max-width: 30px" v-model="product.count" disabled>
                        <div class="count-icon" @click="modifyProductCount(product.id,product.count+1)">
                          <font-awesome-icon style="color: #8b9096" :icon="['fa','plus']"/>
                        </div>

                        <div class="count-icon" style="min-width: 40px;" @click="delCartProduct(product.id)">
                          <font-awesome-icon style="color: #8b9096" :icon="['fa','trash-alt']"/>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <van-button type="info" @click="goLoginPage">去登陆</van-button>
    </div>
    <div class="order-container">
      <div class="order-left">
        <div class="checkall-container">
          <van-checkbox @click="onAllCheckClick" v-model="allChecked">全选</van-checkbox>
        </div>
        <span style="font-weight: 600">合计:￥{{totalPrice}}.00</span>
      </div>
      <div class="order-right">
        <van-button type="danger" size="large" @click="onSubmitOrder">去结算({{totalCounts}})</van-button>
      </div>
    </div>

  </div>

</template>

<script>
  import HeaderTop from '../header/HeaderTop'
  import { Checkbox, CheckboxGroup, Button, Toast, Popup } from 'vant'
  import { mapState } from 'vuex'

  export default {
    name: 'Cart',
    components: {
      HeaderTop,
      [CheckboxGroup.name]: CheckboxGroup,
      [Checkbox.name]: Checkbox,
      [Button.name]: Button,
      [Toast.name]: Toast,
    },
    data () {
      return {
        checkedProducts: [],
        cartProducts: [],
        totalPrice: 0,
        totalCounts: 0,
        show: true,
        allChecked: 0
      }
    },
    computed: {

      ...mapState(['accessToken', 'login'])
    },

    methods: {
      //查询购物车商品数据（含其选中状态，店铺信息，总价，总选中商品数）
      getProducts () {
        this.$api.getCartProducts().then(res => {
          if (res.code == 1) {
            // this.cartProducts = res.data
            this.cartProducts = res.data.shops
            this.totalPrice = res.data.totalPrice
            this.totalCounts = res.data.totalCounts
            this.allChecked = res.data.allChecked
          } else {
            this.cartProducts = []
            this.totalPrice = 0
            this.totalCounts = 0
            this.allChecked = 0
          }
        })

      },
      //修改购物车中商品数量
      modifyProductCount (id, count) {
        if (count == 0) {
          this.$toast('该商品1件起售！')
        } else {
          this.$api.opCartProduct(id, 2, count).then(res => {
            this.getProducts()

          })
        }
      },
      async delCartProduct (id) {
        await opCartProduct(this.accessToken, id, 1)
        this.getProducts()
      },
      goLoginPage () {
        this.$router.push('login')
      },
      onProductClick (id) {
        this.$router.push({ 'path': '/product?id=' + id })
      },
      onSubmitOrder () {
        if (this.totalCounts < 1) {
          this.$toast('你还未选中结算商品！')
        }
        this.$router.push({ 'path': '/order/confirm' })
      },

      onAllCheckClick () {
        if (this.allChecked) {
          this.$api.modifyCartProductsChecked(0, 0).then(res => {
            this.getProducts()

          })
        } else {
          this.$api.modifyCartProductsChecked(0, 1).then(res => {
            this.getProducts()

          })
        }
      },
      //商品checkbox点击时：
      onProductCheckBoxClick (id, checked) {
        if (checked == 1) {
          //取消选择商品
          this.$api.modifyCartProductsChecked(2, 0, id).then(res => {
            this.getProducts()

          })

        } else {
          //选择商品
          this.$api.modifyCartProductsChecked(2, 1, id).then(res => {
            this.getProducts()

          })
        }
      },
      //店铺checkbox点击时：
      onShopCheckBoxClick (id, checked) {
        console.log(id)
        if (checked == 1) {
          //取消选择商品
          this.$api.modifyCartProductsChecked(1, 0, 0, id).then(res => {
            this.getProducts()
          })
        } else {
          //选择商品
          this.$api.modifyCartProductsChecked(1, 1, 0, id).then(res => {
            this.getProducts()

          })
        }
      }
    },
    created () {
      this.getProducts()
    }
  }
</script>

<style lang="less" scoped>
  .card-goods {
    margin-bottom: 100px;
  }

  .product-list {
    display: flex;
    flex-wrap: nowrap;
    margin-top: 10px;
  }

  .shop-list {
    display: flex;
    flex-wrap: nowrap;
    padding-top: 10px;
  }

  .checkbox-container {
    display: flex;
    flex: 0 0 50px;
    align-items: center;
    justify-content: center;
  }

  .checkall-container {
    display: flex;
    flex: 0 0 100px;
    align-items: center;
    justify-content: center;
  }


  .p-count-change {
    min-height: 30px;
    display: flex;
    justify-content: space-between;
    width: 100%;

    .p-price {
      font-size: 14px;
      font-weight: 600;
      color: red;
      flex-grow: 1;
      display: flex;
      align-items: center;
    }

    .p-count {
      display: flex;
      flex-wrap: nowrap;
      flex-grow: 1;
      align-items: center;
      justify-content: flex-end;

      .count-icon {
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
        padding: 0 2px;
      }

      input {
        width: 40px;
        text-align: center;
      }
    }
  }


  .order-container {
    position: fixed;
    left: 0;
    bottom: 50px;
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
