<template>
  <div>
    <el-table
      v-loading="listLoading"
      :data="productList"
      border
      fit
      highlight-current-row
      style="width: 100%;"
    >

      <el-table-column
        fixed
        prop="id"
        label="skuId" align="center"
        width="120">
      </el-table-column>
      <el-table-column
        prop="name"
        label="名称"
        align="center">
      </el-table-column>
      <el-table-column
        label="价格" align="center"
        width="120">
        <template slot-scope="scope">
          <span style="color: #F56C6C;font-size: 16px;font-weight: 600">
            ￥{{ scope.row.price }}</span>
        </template>
      </el-table-column>
      <el-table-column
        prop="stock"
        label="库存" align="center"
        width="120">
      </el-table-column>
      <el-table-column
        prop="comments"
        label="评论数" align="center"
        width="120">
      </el-table-column>
      <el-table-column
        prop="shop"
        label="店铺名称" align="center"
        width="120">
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
        width="120" align="center">
      </el-table-column>
      <el-table-column
        fixed="right"
        label="操作"
        width="300" align="center">
        <template slot-scope="scope">
          <el-button @click="viewProduct(scope.row)" type="primary" size="mini">查看</el-button>
          <el-button @click="editProduct(scope.row)" type="primary" size="mini">编辑</el-button>
          <el-button @click="delProduct(scope.row)" type="danger" size="mini">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog title="修改商品信息" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :model="selectedProduct" label-position="left" label-width="70px"
               style="width: 600px; margin-left:50px;">
        <el-form-item label="id" prop="id">
          {{selectedProduct.id}}
        </el-form-item>

        <el-form-item label="名称" prop="name" >
          <el-input type="textarea" v-model="selectedProduct.name"/>
        </el-form-item>
        <el-form-item label="价格" prop="price">
          <el-input v-model="selectedProduct.price"/>
        </el-form-item>
         <el-form-item label="库存" prop="stock">
          <el-input v-model="selectedProduct.stock"/>
        </el-form-item>
         <el-form-item label="评论" prop="comments">
          <el-input v-model="selectedProduct.comments"/>
        </el-form-item>
        <el-form-item label="状态">
          <el-input v-model="selectedProduct.status"/>
        </el-form-item>
        <el-form-item label="创建时间" prop="create_time">
          <el-input v-model="selectedProduct.create_time" disabled/>
        </el-form-item>
        <el-form-item label="最近更新" prop="create_time">
          <el-input v-model="selectedProduct.modify_time" disabled/>

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
      <pagination v-show="total>0" :total="total" :page.sync="productQuery.page" :limit.sync="productQuery.limit"
                  @pagination="getProductList"/>
    </div>
  </div>
</template>

<script>
    import Pagination from '@/components/Pagination'

  export default {
    name: "Index",
    components:{Pagination},
    data() {
      return {
        listLoading: false,
        dialogFormVisible: false,
        selectedProduct: 1,
        pageSize: 20,
        curPage: 1,
        perPage: [20, 30, 50, 100],
        productList: [],
        total: 0,
        productQuery: {page: 1, limit: 20}
      }
    },

    methods: {
      viewProduct(row) {
        console.log(row);
      },
      editProduct(row) {
        this.dialogFormVisible = true
        this.selectedProduct = row
      },
      delProduct(row) {
        console.log(row);

        this.$api.delProduct(row).then(res => {
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
      onEditProductConfirm() {
        this.$api.editProduct(this.selectedProduct).then(res => {
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
      getProductList() {
        this.listLoading = true
        this.$api.getProductList(this.productQuery).then(res => {
          this.productList = res.data.product_list
          this.total = res.data.total
          this.listLoading = false
        })
      }
    },

    created() {
      this.getProductList()

    }
  }
</script>

<style scoped>

</style>
