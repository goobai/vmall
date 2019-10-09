<template>
  <div>
    <el-table
      v-loading="listLoading"
      :data="shopList"
      border
      fit
      highlight-current-row
      style="width: 100%;"
    >

      <el-table-column
        fixed
        prop="id"
        label="店铺id" align="center"
        width="120">
      </el-table-column>
      <el-table-column
        prop="name"
        label="店铺名称"
        align="center">
      </el-table-column>
      <el-table-column
        prop="logo"
        label="logo" align="center"
        width="300">
      </el-table-column>
      <el-table-column
        prop="create_time"
        label="创建时间" align="center"
        width="200">
      </el-table-column>
      <el-table-column
        prop="modify_time"
        label="更新时间" align="center"
        width="200">
      </el-table-column>
      <el-table-column
        prop="status"
        label="状态"
        width="100" align="center">
      </el-table-column>
      <el-table-column
        fixed="right"
        label="操作"
        width="300" align="center">
        <template slot-scope="scope">
          <el-button @click="viewShop(scope.row)" type="primary" size="mini">查看</el-button>
          <el-button @click="editShop(scope.row)" type="primary" size="mini">编辑</el-button>
          <el-button @click="delShop(scope.row)" type="danger" size="mini">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog title="修改店铺信息" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :model="selectedShop" label-position="left" label-width="70px"
               style="width: 400px; margin-left:50px;">
        <el-form-item label="id" prop="id">
          {{selectedShop.id}}
        </el-form-item>

        <el-form-item label="店铺名称" prop="name">
          <el-input v-model="selectedShop.name"/>
        </el-form-item>
        <el-form-item label="logo" prop="logo">
          <el-input v-model="selectedShop.logo"/>
        </el-form-item>
        <el-form-item label="状态">
          <el-input v-model="selectedShop.status"/>
        </el-form-item>
        <el-form-item label="创建时间" prop="create_time">
          <el-input v-model="selectedShop.create_time" disabled/>
        </el-form-item>
        <el-form-item label="最近更新" prop="create_time">
          <el-input v-model="selectedShop.modify_time" disabled/>

        </el-form-item>

      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          取消
        </el-button>
        <el-button type="primary" @click="onConfirm">
          确定
        </el-button>
      </div>
    </el-dialog>

    <div class="block">
      <pagination v-show="total>0" :total="total" :page.sync="shopQuery.page" :limit.sync="shopQuery.limit"
                  @pagination="getShopList"/>
    </div>
  </div>
</template>

<script>
  import Pagination from '@/components/Pagination'

  export default {
    name: "Index",
    components: {Pagination},
    data() {
      return {
        listLoading: false,
        dialogFormVisible: false,
        selectedShop: 1,
        pageSize: 20,
        curPage: 1,
        perPage: [20, 30, 50, 100],
        shopList: [],
        total: 0,
        shopQuery: {page: 1, limit: 20}
      }
    },
    methods: {
      viewShop(row) {
        console.log(row);
      },
      editShop(row) {
        this.dialogFormVisible = true
        this.selectedShop = row
      },
      delShop(row) {
        console.log(row);

        this.$api.delShop(row).then(res => {
            if (res.code == 1) {
              this.$notify({
                title: '成功',
                message: res.msg,
                type: 'success'
              });
            }
          }
        )
      },
      onConfirm() {
        this.$api.editShop(this.selectedShop).then(res => {
          console.log(this.selectedShop)
          if (res.code == 1) {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: res.msg,
              type: 'success'
            });
          } else {
            this.$notify.error({
              title: '失败',
              message: res.msg,
            });
          }
        }).catch(err => {
          this.$notify.error({
            title: '失败',
            message: err,
          });
        })
      }
      ,
      getShopList() {
        this.listLoading = true
        this.$api.getShopList(this.shopQuery).then(res => {
          this.shopList = res.data.shop_list
          this.total = res.data.total
          this.listLoading = false
        })
      }
    },

    created() {
      this.getShopList()

    }
  }
</script>

<style scoped>

</style>
