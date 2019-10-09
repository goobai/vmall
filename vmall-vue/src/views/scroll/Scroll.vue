<template>
  <div class="wrapper">
    <div class="wrapper1" ref="scroll1">
      <div>
        <div class="item" v-for=" (item,index) in items" :key="index"><span>item</span></div>
      </div>
    </div>
    <div class="wrapper2" ref="scroll2">
      <div>
        <div class="item" v-for=" (item,index) in items" :key="index"><span>item</span></div>
      </div>
    </div>
  </div>
</template>

<script>
  import BScroll from '@better-scroll/core'

  export default {
    name: 'Scroll',
    data () {
      return {
        items: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 3, 32, 412, 5, 512, 5, 255, , 65, 612]
      }
    },
    methods: {
      initScroll () {
        this.rootScroll = new BScroll(this.$refs.scroll1, {
          click: true,
          bounce:
            {
              top: true,
              bottom: false,
              left: false,
              right: false
            }
        })
        this.categoryScroll = new BScroll(this.$refs.scroll2, {
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
    mounted () {
      this.initScroll()
    }
  }
</script>

<style scoped lang="scss">
  .wrapper {
    display: flex;
    position: absolute;
    top: 50px;
    bottom: 50px;
    width: 100%;
    border-top: 0.5px #3f3f3f solid;
  }

  span {
    background-color: white;
    font-size: 14px;
    color: red;
  }

  .wrapper1 {
    background-color: #42b983;
    height: 500px;
    flex: 0 0 85px;
    overflow: hidden;
    width: 85px;

  }

  .wrapper2 {
    background-color: #42b983;
    flex: 1;
    overflow: hidden;
    width: 100%;
  }

  .item {
    height: 100px;
    margin-top: 20px;
    background-color: white;
  }

  .wrapper2 {
    background-color: #0e76a8;
    width: 100%;
    height: 500px;
  }
</style>
