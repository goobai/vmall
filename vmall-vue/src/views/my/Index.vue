<template>
  <div class="wrapper">
    <section id="user_section card">
      <div class="user-card">
        <div class="user-info">
          <div class="avatar">
            <img :src="userInfo.avatar" alt="">
          </div>
          <div class="info-wrap">
            <div class="nick-name title">{{userInfo.nickname}}</div>
          </div>
        </div>
        <div class="my">
          <div>
            <span>12</span>
            <span>商品关注</span>
          </div>
          <div>
            <span>23</span>
            <span>店铺关注</span>
          </div>
          <div>
            <span>100</span>
            <span>足迹</span>
          </div>
          <div>
            <span>100</span>
            <span>浏览记录</span>
          </div>
        </div>
      </div>


    </section>
    <section id="order-section" class="card">
      <div class="title">我的订单</div>
      <div class="order-icon-container">
        <div class="order-icon">
          <div class="icon">
            <font-awesome-icon :icon="['fa','credit-card']"/>
          </div>
          <div class="text"> 待付款</div>
        </div>
        <div class="order-icon">
          <div class="icon">
            <font-awesome-icon :icon="['fa','truck']"/>
          </div>
          <div class="text">待收货</div>
        </div>
        <div class="order-icon">
          <div class="icon">
            <font-awesome-icon :icon="['far','comment-alt']"/>
          </div>
          <div class="text">待评价</div>
        </div>
        <div class="order-icon">
          <div class="icon">
            <font-awesome-icon :icon="['fa','magic']"/>
          </div>
          <div class="text">退换/售后</div>
        </div>
        <div class="order-icon" @click="goMyOrder">
          <div class="icon">
            <font-awesome-icon :icon="['fa','list-alt']"/>
          </div>
          <div class="text">全部订单</div>
        </div>
      </div>
    </section>
    <section id="recommend-area">
      <div class="center-hv rec-title">为你精选</div>
      <div class="product-card-list card">
        <div class="p-card" v-for="product  in recommendProducts">
          <div @click="onProductClick(product.id)">
            <img class="p-card-img"
                 :src="product.img[0]"
                 alt="">
            <div class="p-name"> {{product.sku_name}}</div>

          </div>
          <div>
            <div class="flex-jc-sb center-hv">
              <div class="p-price">￥{{product.price}}.00</div>
              <div>
                <van-tag plain color="#e93b3d" round>找相似</van-tag>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
  import {mapState} from 'vuex'
  import {Sticky} from 'vant'

  export default {
    name: 'Index',
    components: {
      [Sticky.name]: Sticky
    },
    data() {
      return {
        recommendProducts: []
      }
    },
    methods: {
      goMyOrder() {
        this.$router.push('/my/order')
      },
      onProductClick(id) {
        this.$router.push({'path': '/product?id=' + id})
      },
      getRecProducts(offset) {
        let params = {'offset': offset, 'type': 1}

        this.$api.getRecommendProducts(params).then(res => {
          this.recommendProducts = res.data
        })
      },
    },
    computed: {
      ...mapState(['login', 'userInfo'])
    },
    created() {
      this.getRecProducts(0)
    }
  }
</script>

<style lang="less" scoped>
  .wrapper {
    margin-bottom: 50px;
  }

  .user-card {
    /*background-color: #FF5000;*/
    /*background-image: -webkit-linear-gradient(left, #FD9126, #FF5000);*/
    /*background-image: linear-gradient(to right, #FD9126, #FF5000);*/
    border-radius: 6px 6px 300px 300px/6px 6px 20px 20px;
    background: -webkit-linear-gradient(left, #eb3c3c, #ff7459);
    background: -webkit-gradient(linear, left top, right top, from(#eb3c3c), to(#ff7459));
    background: linear-gradient(90deg, #eb3c3c, #ff7459);
    min-height: 110px;
    color: #f8f8f2;

    .user-info {
      display: flex;
      padding: 25px 10px 10px;

      .avatar {
        width: 60px;
        height: 60px;
        overflow: hidden;
        box-shadow: 0 2px 10px rgba(0, 0, 0, .15);
        border: 1px solid hsla(0, 0%, 100%, .4);
        border-radius: 60px;

        img {
          width: 100%;
          height: 100%;
        }
      }

      .info-wrap {
        -webkit-box-flex: 1;
        -webkit-flex: 1;
        flex: 1;
        overflow: hidden;
        margin-left: 15px;
      }

      .nick-name {
        padding-top: 10px;
        max-width: 200px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }
    }

    .my {
      display: flex;
      flex: 1;
      justify-content: space-around;
      padding: 10px 0;

      span {
        display: block;
        text-align: center;
      }
    }
  }

  #member-area {
  }

  .order-icon-container {
    padding-top: 20px;
    display: flex;
    justify-content: space-around;
    align-items: center;
  }

  .product-card-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: start;

    .p-card {
      width: 44%;
      padding: 3%;
      @media (max-width: 300px) {
        padding: 3% 3%;
        width: 94%;
      }
      @media (min-width: 680px) {
        padding: 2%;
        width: 21%;
      }
    }

    .p-card-img {
      width: 100%;
    }
  }

  .rec-title {
    font-size: 14px;
    font-weight: 600;
    background-color: #fff;
    padding: 0;
    height: 30px;
    margin: 0 5px;
  }

</style>
