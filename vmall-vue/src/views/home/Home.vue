<template>
  <div class="container">
    <section id="ad-area" class="card">
      <van-swipe @change="onChange">
        <van-swipe-item v-for="image in adImages">
          <img v-lazy="image">
        </van-swipe-item>
        <div class="custom-indicator" slot="indicator">
          {{ current + 1 }}/{{adImages.length}}
        </div>
      </van-swipe>
    </section>
    <section id="category-area" class="card">
      <div class=" icon-list-container">
        <div class="icon-button" @click="goCategory(76)">
          <div class="item"><img class="img"
                                 src="../../images/手机.png"
                                 alt=""></div>
          <div class="item">
            <div class="text">
              <span>手机</span>
            </div>
          </div>
        </div>
        <div class="icon-button">
          <div class="item"><img class="img"
                                 src="../../images/笔记本.png"
                                 alt=""></div>
          <div class="item">
            <div class="text">
              <span>笔记本</span>
            </div>
          </div>
        </div>
        <div class="icon-button">
          <div class="item"><img class="img"
                                 src="../../images/数码.png"
                                 alt=""></div>
          <div class="item">
            <div class="text">
              <span>数码</span>
            </div>
          </div>
        </div>

        <div class="icon-button">
          <div class="item"><img class="img"
                                 src="../../images/相机.png"
                                 alt=""></div>
          <div class="item">
            <div class="text">
              <span>相机</span>
            </div>
          </div>
        </div>

        <div class="icon-button">
          <div class="item"><img class="img"
                                 src="../../images/显示器.png"
                                 alt=""></div>
          <div class="item">
            <div class="text">
              <span>显示器</span>
            </div>
          </div>
        </div>
        <div class="icon-button">
          <div class="item"><img class="img"
                                 src="../../images/服装.png"
                                 alt=""></div>
          <div class="item">
            <div class="text">
              <span>服装</span>
            </div>
          </div>
        </div>
        <div class="icon-button">
          <div class="item"><img class="img"
                                 src="../../images/化妆品.png"
                                 alt=""></div>
          <div class="item">
            <div class="text">
              <span>化妆品</span>
            </div>
          </div>
        </div>
        <div class="icon-button">
          <div class="item"><img class="img"
                                 src="../../images/洗面奶.png"
                                 alt=""></div>
          <div class="item">
            <div class="text">
              <span>洗面奶</span>
            </div>
          </div>
        </div>
        <div class="icon-button">
          <div class="item"><img class="img"
                                 src="../../images/香水.png"
                                 alt=""></div>
          <div class="item">
            <div class="text">
              <span>香水</span>
            </div>
          </div>
        </div>
        <div class="icon-button">
          <div class="item"><img class="img"
                                 src="../../images/更多.png"
                                 alt=""></div>
          <div class="item">
            <div class="text">
              <span>更多</span>
            </div>
          </div>
        </div>

      </div>

    </section>
    <section id="hot-area">
      <div class="title center-h card ">今日热卖商品</div>
      <div class="product-card-list card ">
        <div class="p-card " v-for="product  in hotProducts">
          <div @click="onProductClick(product.sku_id)">
            <img class="p-card-img"
                 :src="product.img[0]"
                 alt="">
            <div class="p-name"> {{product.sku_name}}</div>

          </div>
          <div>
            <div class="flex-jc-sb center-hv">
              <div class="p-price">￥{{product.price}}.00</div>
              <div>
                <div>
                  <van-tag plain color="#e93b3d" round>
                    <div class="fa-icon">
                      <font-awesome-icon style="color: #e93b3d" :icon="['fa','cart-plus']"/>
                    </div>
                  </van-tag>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section id="sell-area">
      <div class="title center-h card">打折促销</div>
      <div class="product-card-list card">
        <div class="p-card" v-for="product  in discountProducts">
          <div @click="onProductClick(product.sku_id)">
            <img class="p-card-img"
                 :src="product.img[0]"
                 alt="">
            <div class="p-name"> {{product.sku_name}}</div>

          </div>
          <div>
            <div class="flex-jc-sb center-hv">
              <div class="p-price">￥{{product.price}}.00</div>
              <div>
                <div class="fa-icon" style="min-width: 40px;">
                  <font-awesome-icon style="color: #e93b3d" :icon="['fa','cart-plus']"/>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section id="recommend-area">
      <van-sticky>
        <div class="center-hv rec-title">为你精选</div>
      </van-sticky>
      <div class="product-card-list card">
        <div class="p-card" v-for="product  in recommendProducts">
          <div @click="onProductClick(product.sku_id)">
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
  import {Swipe, Sticky, SwipeItem, Button, Tabs, List} from 'vant'

  export default {
    name: 'Home',
    components: {
      [Swipe.name]: Swipe,
      [SwipeItem.name]: SwipeItem,
      [Button.name]: Button,
      [Tabs.name]: Tabs,
      [Sticky.name]: Sticky,
      [List.name]: List,
    },
    data() {
      return {
        adImages: ['http://gw.alicdn.com/imgextra/i4/163/O1CN01MMoDkD1D4h5l9bzWO_!!163-0-lubanu.jpg', 'http://gw.alicdn.com/imgextra/i4/163/O1CN01MMoDkD1D4h5l9bzWO_!!163-0-lubanu.jpg'],
        current: 0,
        hotProducts: [],
        recommendProducts: [],
        discountProducts: [],
        recOffset: 0,
      }
    },
    methods: {
      onChange: function (index) {
        this.current = index
      },
      goCategory(cid) {
        this.$router.push({'path': '/products?cid=' + cid})
      },
      getHotProducts(offset) {
        let params = {'offset': offset, 'type': 3}

        this.$api.getRecommendProducts(params).then(res => {
          this.hotProducts = res.data

        })
      }
      ,
      // async getRecProducts (offset) {
      //   let params = { 'offset': offset, 'type': 1 }
      //   let res = await getRecommendProducts(params)
      //   if (res) {
      //     this.recommendProducts = res.data
      //   } else {
      //     console.log(res)
      //   }
      // },
      getDisProducts(offset) {
        let params = {'offset': offset, 'type': 2}
        this.$api.getRecommendProducts(params).then(res => {
          this.discountProducts = res.data

        })
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
    created() {
      this.getRecProducts(0)
      this.getHotProducts(0)
      this.getDisProducts(0)

    },

  }
</script>

<style scoped lang="scss">
  .container {
    margin-bottom: 50px;
  }

  #ad-area img {
    width: 100%;
    max-height: 200px;
  }

  .custom-indicator {
    position: absolute;
    right: 5px;
    bottom: 5px;
    padding: 2px 5px;
    font-size: 1rem;
    color: white;
    background: rgba(0, 0, 0, .1);
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

  .fa-icon {
    border: 0.2px solid #e93b3d;
    border-radius: 3px;

  }

  #recommend-area {

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
