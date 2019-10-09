<template>
  <div id="header">
    <van-nav-bar
      :title="title"
      left-text="返回"
      left-arrow
      @click-left="$router.go(-1)"
    />
  </div>
</template>

<script>
export default {
  name: 'HeaderTop',
  methods: {},
  props: {
    title: String
  },
  methods: {
    onClickLeft: function () {
      this.$router.go(-1)
    }
  }
}
</script>

<style scoped>
  #header {
    position: -webkit-sticky;
    position: sticky;
    top: 0;
    z-index: 1020;
  }
</style>
