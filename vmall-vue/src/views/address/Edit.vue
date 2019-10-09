<template>
  <div>
    <van-address-edit ref="address"
                      :address-info="addressInfo"
                      :area-list="areaList"
                      show-delete
                      show-set-default
                      show-search-result
                      :search-result="searchResult"
                      @save="onSave"
                      @delete="onDelete"
    />
  </div>
</template>

<script>
  import {AddressEdit} from 'vant';
  import HeaderTop from '../header/HeaderTop';
  import '../../utils/area'
  import area from "../../utils/area";
  import {mapState} from 'vuex';

  export default {
    name: "AddressIndex",
    components: {
      HeaderTop,
      [AddressEdit.name]: AddressEdit
    },
    data() {
      return {
        areaList: {},
        searchResult: [],
        addressInfo: {}
      }
    },
    methods: {
      onSave(val) {

        val.type = this.$route.params.type
        val.id = this.$route.params.id
        this.$api.editAddress(val).then(res => {
          if (res.code == 1) {
            this.$toast.success({message: res.msg, duration: 500})
            this.$router.go(-1)
          }
        })
      },
      onDelete(val) {
        val.type = 3
        val.id = this.$route.params.id
        this.$api.editAddress(val).then(res => {
          if (res.code == 1) {
            this.$toast.success({message:res.msg, duration: 500})
            this.$router.go(-1)
          }
        })
      },
      // onChangeDetail(val) {
      //   if (val) {
      //     this.searchResult = [{
      //       name: '黄龙万科中心',
      //       address: '杭州市西湖区'
      //     }];
      //   } else {
      //     this.searchResult = [];
      //   }
      // }
    },
    created() {
      this.areaList = area
      this.addressInfo.userId = this.userInfo.id
      console.log(this.$route.params)
      if (this.$route.params.type == 2) {
        this.$api.getUserAddress({id: this.$route.params.id}).then(res => {
          this.addressInfo = res.data
        })
      }

    },
    computed: {
      ...mapState(['userInfo'])
    }
  }
</script>

<style scoped>

</style>
