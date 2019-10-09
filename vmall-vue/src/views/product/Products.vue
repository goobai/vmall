<template>
  <div class="wrapper">
    <div class="head">
      <van-search
        v-model="keyword"
        placeholder="请输入搜索关键词"
        show-action
        shape="round"
        @search="onSearch"
      >
        <div slot="action" @click="onSearch">搜索</div>
      </van-search>
      <van-dropdown-menu active-color="#e93b3d">
        <van-dropdown-item v-model="value1" :options="option1"/>
        <van-dropdown-item v-model="value2" :options="option2"/>
        <van-dropdown-item v-model="value3" :options="option3"/>
        <van-dropdown-item v-model="value4" :options="option4"/>
      </van-dropdown-menu>
    </div>
    <div class="pullup">

      <div class="products-wrapper" ref="scroller">
        <div class="pullup-scroller">
          <div>
            <div class="item" v-for="product in productsList">
              <div class="item-img" @click="onProductClick(product.id)">
                <img :src="product.images[0]">
              </div>
              <div class="item-main">
                <div class="p-name" @click="onProductClick(product.id)">{{product.name}}</div>
                <div class="p-tag">{{product.tag}}</div>
                <div class="p-price">￥{{product.price}}</div>
                <div class="space-between">
                  <div class="p-comment">{{product.comments}} <span>好评：99.90%</span></div>
                  <!--                  <div class="fa-icon" style="min-width: 40px;" @click="onAddCartClick(product.id)">-->
                  <!--                    <font-awesome-icon style="color: #e93b3d" :icon="['fa','cart-plus']"/>-->
                  <!--                  </div>-->
                </div>
              </div>
            </div>
      <div v-if="noMore" class="no-more">抱歉有找到相关商品！</div>

          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
  import { DropdownMenu, DropdownItem, Search, Toast } from 'vant'
  import BScroll from '@better-scroll/core'
  import Pullup from '@better-scroll/pull-up'
  import { mapState } from 'vuex'

  BScroll.use(Pullup)
  export default {
    name: 'Products',
    components: {
      [DropdownMenu.name]: DropdownMenu,
      [DropdownItem.name]: DropdownItem,
      [Search.name]: Search,
      [Toast.name]: Toast,
    },
    computed: {
      ...mapState(['accessToken'])
    },
    data () {
      return {
        keyword: '',
        searchType: '',
        noMore: false,
        offset: 0,
        value1: 0,
        value2: 'a',
        value3: 'a',
        value4: 'a',
        option1: [
          { text: '综合', value: 0 },
          { text: '新品', value: 1 },
          { text: '评论', value: 2 }
        ],
        option2: [
          { text: '销量', value: 'a' },
        ],
        option3: [
          { text: '价格', value: 'a' },
        ],
        option4: [
          { text: '筛选', value: 'a' },
        ],
        cid: 1,
        productsList: []
      }
    },
    methods: {
      onAddCartClick (id) {
        this.$api.opCartProduct(id, 0).then(res => {
          if (res.code == 1) {
            this.$toast('购物车加入成功')
          } else {
            this.$toast(res.msg)
          }
        })

      },
      onSearch () {
        this.productsList = []
        this.searchType = 'search'
        this.offset = 0
        this.noMore = false
        this.bscroll.scrollTo(0, 0)
        this.$api.getProductsList(this.searchType, this.cid, this.offset, this.keyword).then(res => {
          if (res.data.length < 1) {
            this.noMore = true
            return
          }
          this.productsList = res.data
          this.$nextTick(() => {
            this.initScroll()
          })
        })

      },
      onProductClick (id) {
        this.$router.push({ 'path': '/product?id=' + id })
      },

      getProducts () {
        this.offset = this.productsList.length
        this.$api.getProductsList(this.searchType, this.cid, this.offset, this.keyword).then(res => {
          this.productsList = res.data
          this.$nextTick(() => {
            this.initScroll()
          })
        })

      },
      initScroll () {
        this.bscroll = new BScroll(this.$refs.scroller, {
          click: true,
          scrollY: true,
          pullUpLoad: { threshold: 30 },
        })
        this.bscroll.on('pullingUp', this.pullingUpHandler)
      },
      pullingUpHandler () {
        this.offset = this.productsList.length

        this.$api.getProductsList(this.searchType, this.cid, this.offset, this.keyword).then(res => {
          if (res.data.length < 1) {
            this.noMore = true
            this.bscroll.finishPullUp()
            return
          }
          this.productsList = this.productsList.concat(res.data)
          this.bscroll.refresh() // DOM 结构发生变化后，重新初始化BScroll
          this.bscroll.finishPullUp()
        })

      },
    },
    mounted () {
      this.cid = this.$route.query.cid
      this.searchType = 'category'
      this.getProducts()
    },
    created () {
      this.cid = this.$route.query.cid
      this.category = this.$route.query.category
      this.searchType = this.$route.query.searchType
      this.keyword = this.$route.query.keyword
    }
  }
</script>

<style scoped lang="scss">
  .wrapper {
    width: 100%;
    height: 100%;
  }

  .item {
    display: flex;
    width: 100%;
    margin: 5px;

    .item-img {
      img {
        width: 100px;
        height: 100px;
      }
    }

    .item-main {
      padding: 5px 10px;
      width: 100%;

      .p-name {
        font-size: 14px;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        height: 36px;
        /*white-space: nowrap;*/
        text-align: justify;
      }

      .p-price {
        font-size: 16px;
        color: red;
        font-weight: 400;
      }

      .p-comment {
        font-size: 12px;
        color: #999;
        font-weight: 400;

        span {
          font-size: 12px;
        }
      }

      .p-shop {
        font-size: 12px;
        color: #999;
        font-weight: 400;
      }
    }
  }

  .pullup {
    position: absolute;
    top: 110px;
    bottom: 0px;
    left: 0px;
    width: 100%;
    overflow: hidden;
  }

  .products-wrapper {
    height: 100%;
  }

  .pullup-wrapper {
    padding: 20px;
    text-align: center;
    color: #999;
  }

  .fa-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    padding: 0 2px;
  }

  .space-between {
    width: 100%;
    display: flex;
    justify-content: space-between;
  }

  .no-more {
    height: 100%;
    margin-top: 50%;
  }
</style>
