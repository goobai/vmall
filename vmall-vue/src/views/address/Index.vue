<template>
  <div>
    <van-address-list
      v-model="chosenAddressId"
      :list="list"
      @add="onAdd"
      @edit="onEdit"
    />
  </div>
</template>

<script>
  import {AddressList, Toast} from 'vant'

  export default {
    name: "AddressIndex",
    components: {
      [AddressList.name]: AddressList,
      [Toast.name]: Toast
    },
    data() {
      return {
        chosenAddressId: '1',
        list: []
      }

    },
    methods: {
      onAdd() {
        this.$router.push({name: "AddressEdit", params: {type: 1}})
      },

      onEdit(item, index) {
        this.$router.push({name: "AddressEdit", params: {type: 2, id: this.list[index].id}})
      }
    },
    created() {
      this.$api.getUserAddresses().then(res => {
        this.list = res.data
      })
    }
  }
</script>

<style scoped>

</style>
