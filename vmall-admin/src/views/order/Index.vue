<template>
  <div>
    <el-row>
      <el-form :inline="true" :model="formKeys">
        <el-form-item label="订单号">
          <el-input v-model="formKeys.order_id" placeholder="订单号"></el-input>
        </el-form-item>
        <el-form-item label="关键字">
          <el-input v-model="formKeys.key_word" placeholder=""></el-input>
        </el-form-item>
        <el-form-item label="订单状态">
          <el-select v-model="formKeys.order_status">
            <el-option label="全部" value=""></el-option>
            <el-option label="待付款" value="0"></el-option>
            <el-option label="待发货" value="1"></el-option>
            <el-option label="待收货" value="2"></el-option>
            <el-option label="待评价" value="3"></el-option>
            <el-option label="已完成" value="4"></el-option>
            <el-option label="已取消" value="5"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="searchOrder">查询</el-button>
        </el-form-item>
      </el-form>
    </el-row>
    <el-table
      v-loading="listLoading"
      :data="orderList"
      border
      fit
      highlight-current-row
      style="width: 100%;"
    >

      <el-table-column
        fixed
        prop="order_id"
        label="订单号" align="center"
        width="120">
      </el-table-column>

      <el-table-column
        label="实付金额" align="center"
        width="120">
        <template slot-scope="scope">
          <span style="color: #F56C6C;font-size: 16px;font-weight: 600">
            ￥{{ scope.row.total_price }}</span>
        </template>
      </el-table-column>

      <el-table-column
        prop="create_time"
        label="下单时间" align="center"
        width="200">
      </el-table-column>

      <el-table-column
        prop="order_status"
        label="状态"
        width="120" align="center">
      </el-table-column>
      <el-table-column
        fixed="right"
        label="操作"
        align="center">
        <template slot-scope="scope">
          <el-button @click="viewDetail(scope.row)" type="primary" size="mini">查看详情</el-button>
          <el-button @click="delProduct(scope.row)" type="danger" size="mini">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog title="订单详情" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :model="selectedOrder" label-position="left" label-width="70px"
               style="width: 600px; margin-left:50px;">
        <el-form-item label="id" prop="id">
          {{selectedOrder.id}}
        </el-form-item>


        <el-form-item label="状态">
          <el-input v-model="selectedOrder.order_status" disabled/>
        </el-form-item>
        <el-form-item label="创建时间" prop="create_time">
          <el-input v-model="selectedOrder.create_time" disabled/>
        </el-form-item>


      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          取消
        </el-button>
        <el-button type="primary" @click="onEditProductConfirm">
          确定
        </el-button>
      </div>
    </el-dialog>

    <div class="block">
      <pagination v-show="total>0" :total="total" :page.sync="orderQuery.page" :limit.sync="orderQuery.limit"
                  @pagination="searchOrder"/>
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
        formKeys: {order_id: '', order_status: '', key_word: ''},
        listLoading: false,
        dialogFormVisible: false,
        selectedOrder: 1,
        pageSize: 20,
        curPage: 1,
        perPage: [20, 30, 50, 100],
        orderList: [],
        total: 0,
        orderQuery: {page: 1, limit: 20}
      }
    },

    methods: {
      viewDetail(row) {
        this.dialogFormVisible = true
        this.selectedOrder = row
        console.log(this.formKeys.order_status)
      },

      onEditProductConfirm() {
        this.$api.editOrder(this.selectedOrder).then(res => {
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
      getOrderList() {
        this.listLoading = true
        this.$api.getOrderList(this.orderQuery).then(res => {
          this.orderList = res.data.order_list
          this.total = res.data.total
          this.listLoading = false
        })
      },
      searchOrder() {
        this.listLoading = true
        if (this.formKeys.key_word || this.formKeys.order_status || this.formKeys.order_id) {
          this.orderQuery.formKeys = this.formKeys
          this.$api.searchOrder(this.orderQuery).then(res => {
            this.orderList = res.data.order_list
            this.total = res.data.total
            this.listLoading = false
          })
        } else {
          this.getOrderList()
        }

      }
    },

    created() {
      this.getOrderList()
    }
  }
</script>

<style scoped>

</style>
