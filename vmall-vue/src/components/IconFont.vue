<template>
  <svg class="iconfont" aria-hidden="true">
    <use :xlink:href="iconName"></use>
  </svg>
</template>

<script>
  import {} from '../icon/iconfont'

  export default {
    name: "IconFont",
    props: {
      iconClass: {
        type: String,
        required: true
      }
    },
    computed: {
      iconName() {
        return `#icon${this.iconClass}`
      }
    },
    data() {
      return {}
    },
    methods: {},
  }
</script>

<style scoped>
  .iconfont {
    /*font-size: 30px;*/
    /*color: #42b983;*/
    /*display: flex;*/
    /*align-items: center;*/
    /*justify-content: center;*/
    width: 1rem;
    height: 1rem;
    vertical-align: -0.15rem;
    fill: currentColor;
    overflow: hidden;
  }
</style>
