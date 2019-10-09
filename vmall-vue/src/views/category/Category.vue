<template>
  <div class="wrapper">
    <div class="root-list" ref="rootWrapper">
      <ul>
        <li v-for="(root,index) in rootList" :key="index" @click="itemClick(root.id,index)"
        ><a>
          <span class="root-item" v-bind:class="{'active':activeRootIndex==index}">{{root.name}}</span></a>
        </li>
      </ul>
    </div>
    <div class="category-list" ref="categoryWrapper">
      <div>
        <div class="category-item" v-for="(category,index) in categoryList" :key="index">
          <h4 class="category-title">{{category.name}}</h4>
          <ul>
            <li @click="categoryClick(son.id)" v-for="(son,index) in category.sons" :key="index">
              <img :src="son.img" alt="" class="son-img">
              <span> {{son.name}}</span>
            </li>
          </ul>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
  import BScroll from '@better-scroll/core'

  export default {
    name: 'Category',
    data () {
      return {
        activeKey: 0,
        rootList: [],
        categoryList: [],
        activeRootIndex: 0
      }
    },
    methods: {
      initData () {
        let res = this.$api.getRootCategory().then(res => {
          this.rootList = res.data
          let id = this.rootList[0].id

          this.$api.getCategoryList(id).then(res => {
            this.categoryList = res.data
            this.activeRootIndex = 0
            this.$nextTick((() => {
              this.initScroll()
              this.initCaScroll()
            }))
          })
        })

      },
      onChange (key) {
        this.activeKey = key
      },

      itemClick (id, index) {
        this.$api.getCategoryList(id).then(res => {
          this.categoryList = res.data
          this.activeRootIndex = index
          this.$nextTick(() => {
            this.categoryScroll.scrollTo(0, 100)
            this.initCaScroll()
          })
        })

      },
      categoryClick (id) {
        this.$router.push({ 'path': '/products?type=category&cid=' + id })
      },
      initScroll () {
        this.rootScroll = new BScroll(this.$refs.rootWrapper, {
          click: true,
          bounce:
            {
              top: true,
              bottom: false,
              left: false,
              right: false
            }
        })

      },
      initCaScroll () {
        this.categoryScroll = new BScroll(this.$refs.categoryWrapper, {
          click: true,
          bounce:
            {
              top: true,
              bottom: false,
              left: false,
              right: false
            }
        })
      }
    },
    created () {
    },
    mounted () {
      this.initData()
    }
  }
</script>

<style scoped lang="less">

  .wrapper {
    display: flex;
    position: absolute;
    top: 50px;
    bottom: 50px;
    width: 100%;
    border-top: 0.5px #3f3f3f solid;

    .root-list {
      flex: 0 0 85px;
      width: 85px;
      background: #f3f5f7;
      overflow: hidden;
      padding-right: 2px;

      .root-item {
        display: block;
        width: 100%;
        height: 46px;
        line-height: 46px;
        text-decoration: none;
        font-size: 14px;
        color: #080808;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        text-align: center;

        &.active {
          display: block;
          width: 100%;
          height: 46px;
          line-height: 46px;
          text-decoration: none;
          font-size: 14px;
          background: #fff;
          color: #e93b3d;
          overflow: hidden;
          text-overflow: ellipsis;
          white-space: nowrap;
          text-align: center;
          font-weight: 600;
        }
      }
    }

    .category-list {
      flex: 1;
      overflow: hidden;
      height: 100%;

      .category-item {
        display: block;
        margin: 19px 7px 0px;

        .category-title {
          font-size: 14px;
          margin: 0;
          padding: 0;
        }

        ul {
          display: flex;
          flex-flow: row wrap;

          li {
            display: block;
            padding: 2px 10px;
            text-align: center;
            width: 3rem;

            span {
              width: 3rem;
              max-height: 100px;
              display: block;
              font-size: 12px;
              overflow: hidden;
              text-overflow: ellipsis;
              white-space: nowrap;
              text-align: center;
            }

            img {
              width: 3rem;
              height: 3rem;
              max-height: 100px;
              max-width: 100px;
              background-color: #c3c3c3;
            }

          }

        }
      }

    }

  }
</style>
