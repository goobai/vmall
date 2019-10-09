<template>
  <div>

    <section id="img-area">
      <van-swipe>
        <van-swipe-item v-for="(image, index) in productInfo.images" :key="index">
          <img class="img" v-lazy="image"/>
        </van-swipe-item>
      </van-swipe>
    </section>
    <section id="info-area" class="card">
      <div class="price">￥{{productInfo.price}}</div>
      <div class="title">
        <van-tag type="danger">优品</van-tag>
        {{productInfo.title}}
      </div>
      <span class="desc">{{productInfo.describe}}</span>
    </section>
    <section id="select-area" class="card">
      <van-row><span>已选择</span> <span class="selected-sku">{{id}}</span></van-row>
      <div>

      </div>
    </section>
    <section id="detail-area" class="card">
      <div class="detail">
        <van-tabs swipeable sticky>
          <van-tab title="商品详情">
            <div>
              <img class=" img" v-for="(image, index) in productInfo.detail" :key="index" v-lazy="image"/>
            </div>
          </van-tab>
          <van-tab title="商品评价">
            <div class="comment-count">评价（{{commentCount}}）</div>
            <Comment :comment="comment" v-for="comment in comments"></Comment>
          </van-tab>
        </van-tabs>
      </div>
    </section>
    <section id="bottom-area">

      <van-goods-action>

        <van-goods-action-icon
          icon="chat-o"
          text="联系客服"
          @click="onChatClick"
        />
        <van-goods-action-icon
          icon="shop-o"
          text="店铺"
        />
        <van-goods-action-icon
          icon="cart-o"
          text="购物车"
          @click="onCartClick"
        />
        <van-goods-action-button
          type="warning"
          text="加入购物车"
          @click="onAddCartClick(id)"
        />
        <van-goods-action-button
          type="danger"
          text="立即购买"
          @click="onClickButton"
        />
      </van-goods-action>
    </section>
  </div>
</template>

<script>
  // import Comment from '/src/views/comment/Comment'
  import Comment from '../comment/Comment'
  import {mapState} from 'vuex'

  export default {
    name: 'Product',
    components: {Comment},
    data() {
      return {
        productInfo: {},
        id: 0,
        shopId: 0,
        showBase: false,
        showCustom: false,
        showStepper: false,
        showSoldout: false,
        closeOnClickOverlay: true,
        initialSku: {
          s1: '30349',
          s2: '1193',
          selectedNum: 3
        },
        comments: [{
          score: 4.5,
          userName: 'feng子怡',
          userImg: 'https://huyaimg.msstatic.com/avatar/1094/9c/9bd826292dbe3a174fc81b5a6e781f_180_135.jpg?1559034850',
          content: '首先来说一下外观外观来说，没有给人一种很惊艳的感觉，嗯，比较适合女生用吧，特别是低配版的，感觉中规中矩，手感也比较圆润，感觉手感不错，系统方面没什么可讲的，还可以不是重度使用，用户用着完全没有问题，特别是电池方面，非常给力，充电也会特别快摄像的话也比较清晰，可玩性比较高，总体事项，低配的还可以',
          commentTime: '2019-06-02',
          like: '56',
          dislike: '3',
          commentCount: '90'
        }, {
          score: 4.5,
          userName: 'feng子怡',
          userImg: 'https://huyaimg.msstatic.com/avatar/1094/9c/9bd826292dbe3a174fc81b5a6e781f_180_135.jpg?1559034850',
          content: '首先来说一下外观外观来说，没有给人一种很惊艳的感觉，嗯，比较适合女生用吧，特别是低配版的，感觉中规中矩，手感也比较圆润，感觉手感不错，系统方面没什么可讲的，还可以不是重度使用，用户用着完全没有问题，特别是电池方面，非常给力，充电也会特别快摄像的话也比较清晰，可玩性比较高，总体事项，低配的还可以',
          commentTime: '2019-06-02',
          like: '56',
          dislike: '3',
          commentCount: '90'
        }, {
          score: 4.5,
          userName: 'feng子怡',
          userImg: '//storage.360buyimg.com/i.imageUpload/3130353932333230332d32323536343731343636343030303332373336_sma.jpg',
          content: '首先来说一下外观外观来说，没有给人一种很惊艳的感觉，嗯，比较适合女生用吧，特别是低配版的，感觉中规中矩，手感也比较圆润，感觉手感不错，系统方面没什么可讲的，还可以不是重度使用，用户用着完全没有问题，特别是电池方面，非常给力，充电也会特别快摄像的话也比较清晰，可玩性比较高，总体事项，低配的还可以',
          commentTime: '2019-06-02',
          like: '56',
          dislike: '3',
          commentCount: '90'
        }, {
          score: 4.5,
          userName: 'feng子怡',
          userImg: 'https://huyaimg.msstatic.com/avatar/1094/9c/9bd826292dbe3a174fc81b5a6e781f_180_135.jpg?1559034850',
          content: '首先来说一下外观外观来说，没有给人一种很惊艳的感觉，嗯，比较适合女生用吧，特别是低配版的，感觉中规中矩，手感也比较圆润，感觉手感不错，系统方面没什么可讲的，还可以不是重度使用，用户用着完全没有问题，特别是电池方面，非常给力，充电也会特别快摄像的话也比较清晰，可玩性比较高，总体事项，低配的还可以',
          commentTime: '2019-06-02',
          like: '56',
          dislike: '3',
          commentCount: '90'
        }, {
          score: 4.5,
          userName: 'feng子怡',
          userImg: '//storage.360buyimg.com/i.imageUpload/3130353932333230332d32323536343731343636343030303332373336_sma.jpg',
          content: '首先来说一下外观外观来说，没有给人一种很惊艳的感觉，嗯，比较适合女生用吧，特别是低配版的，感觉中规中矩，手感也比较圆润，感觉手感不错，系统方面没什么可讲的，还可以不是重度使用，用户用着完全没有问题，特别是电池方面，非常给力，充电也会特别快摄像的话也比较清晰，可玩性比较高，总体事项，低配的还可以',
          commentTime: '2019-06-02',
          like: '56',
          dislike: '3',
          commentCount: '90'
        }, {
          score: 4.5,
          userName: 'feng子怡',
          userImg: '//storage.360buyimg.com/i.imageUpload/3130353932333230332d32323536343731343636343030303332373336_sma.jpg',
          content: '首先来说一下外观外观来说，没有给人一种很惊艳的感觉，嗯，比较适合女生用吧，特别是低配版的，感觉中规中矩，手感也比较圆润，感觉手感不错，系统方面没什么可讲的，还可以不是重度使用，用户用着完全没有问题，特别是电池方面，非常给力，充电也会特别快摄像的话也比较清晰，可玩性比较高，总体事项，低配的还可以',
          commentTime: '2019-06-02',
          like: '56',
          dislike: '3',
          commentCount: '90'
        }, {
          score: 4.5,
          userName: 'feng子怡',
          userImg: '//storage.360buyimg.com/i.imageUpload/3130353932333230332d32323536343731343636343030303332373336_sma.jpg',
          content: '首先来说一下外观外观来说，没有给人一种很惊艳的感觉，嗯，比较适合女生用吧，特别是低配版的，感觉中规中矩，手感也比较圆润，感觉手感不错，系统方面没什么可讲的，还可以不是重度使用，用户用着完全没有问题，特别是电池方面，非常给力，充电也会特别快摄像的话也比较清晰，可玩性比较高，总体事项，低配的还可以',
          commentTime: '2019-06-02',
          like: '56',
          dislike: '3',
          commentCount: '90'
        }],
        commentCount: '90'
      }

    },
    methods: {
      getDetail() {
        this.$api.getProductInfo(this.id).then(res => {
          this.productInfo = res.data

        })
      },
      getComments() {
        this.$api.getComments(this.id).then(res => {
          this.comments = res.data

        })
      },
      onChatClick() {
        this.$router.push('chat')
      },
      onClickIcon() {
        this.$toast('点击图标')
      },
      onClickButton() {
        this.$toast('点击按钮')
      },
      onCartClick() {
        this.$router.push('cart')
      },
      onAddCartClick(id) {
        if (this.login) {
          this.$api.opCartProduct(id).then(res => {
            if (res.code == 1) {
              console.log(this.$router.currentRoute.fullPath)
              this.$toast('购物车加入成功')
            } else {
              this.$toast(res.msg)
            }
          })

        } else {
          this.$router.push({
            name: "Login", query: {
              redirect: this.$router.currentRoute.fullPath
            }
          })
          this.$toast('请登录！')
        }

      }
    },
    mounted() {
      this.id = this.$route.query.id
      this.getDetail()
    },
    computed: {
      ...mapState(['accessToken', 'refreshToken', 'login'])
    }
  }
</script>

<style scoped lang="scss">
  .img {
    width: 100%
  }

  .detail {
    margin-bottom: 60px;
  }

  .detail img {
    border: 0px;
    display: inline;
    max-width: none !important;
    vertical-align: top;
  }

  #bottom-area {
    position: fixed;
    bottom: 0px;
    left: 0px;
  }

  #info-area {
    padding: 2px 4px;
    text-align: start;
    font-family: PingFang SC, Helvetica Neue, Arial, sans-serif;

    .price {
      font-size: 20px;
      color: red;
      font-weight: bold;
    }

    .title {
      font-size: 16px;
      font-weight: 700;
    }

    .desc {
      font-size: 0.8rem;
      color: #c3c3c3;
    }

  }

  .comment-count {
    color: #666;
    margin: 10px;
    font-weight: 700;
  }
</style>
