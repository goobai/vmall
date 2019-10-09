<template>
  <div class="hello">
    <div class="hello"><input v-model="ce"/></div>
    <div v-html="parsed"></div>
  </div>
</template>

<script>
import katex from 'katex'
import 'katex/dist/contrib/mhchem.min'
import 'katex/dist/katex.min.css'
// import './test.js'
export default {
  data () {
    return {
      ce: '\\ce{CO2 + C -> 2 CO}'
    }
  },
  computed: {
    parsed: function () {
      // console.log("wrong"+this.ce)
      try {
        return katex.renderToString(this.ce, {
          displayMode: true
        })
      } catch (e) {
        return e.message
      }
    }
  },
  created () {
    // console.log("abc"+this.ce)
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h3 {
    margin: 40px 0 0;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }

  .hello {
    margin: 0 auto;
  }
</style>
