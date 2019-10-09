<template>
  <div>
    <van-row type="flex" justify="center">
      <van-col span="20" >
        <van-search
        v-model="keyword"
        placeholder="请输入搜索关键词"
        show-action
        shape="round"
        @search="onSearch"
      >
        <div slot="action" @click="onSearch">搜索</div>
      </van-search>
      </van-col>
    </van-row>
  </div>
</template>

<script>
// import { regUser, info } from '../../api/api'

export default {
  name: 'search',
  data () {
    return {
      keyword: '',
      userId: 1
    }
  },
  methods: {
    // getUerInfo: function (userid) {
    //   this.userInfo = info(this.userId).data.signature
    // },
    onSearch: function (keyword) {

    }
  },

}
</script>

<style scoped>

</style>
