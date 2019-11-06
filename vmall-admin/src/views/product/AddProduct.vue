<template>

  <div class="createPost-container">
    <div class="CategorySelect">
      <span class="demonstration">分类选择</span>
      <el-cascader size="medium "
                   v-model="categoryValue"
                   :options="categoryOptions"
                   :props="{ expandTrigger: 'hover' }"
                   @change="handleChange"></el-cascader>
    </div>
    <el-form :model="productForm" :rules="rules" ref="productForm" label-width="150px" class="demo-ruleForm">

      <div><h3 style="width: 150px;text-align: right;padding: 0 12px 0 0;font-weight: 700">基础信息</h3></div>
      <hr>
      <!--      商品名-->

      <el-form-item label="商品名称" prop="name">
        <el-input v-model="productForm.name"></el-input>
      </el-form-item>
      <!--      商品标题-->

      <el-form-item label="商品标题" prop="title">
        <el-input v-model="productForm.title"></el-input>
      </el-form-item>
      <!--      商品价格-->

      <el-form-item label="商品价格" prop="title">
        <el-input v-model="productForm.price"></el-input>
      </el-form-item>
      <!--      商品规格选择-->
      <div><h3 style="width: 150px;text-align: right;padding: 0 12px 0 0;font-weight: 700">销售信息</h3></div>
      <hr>
      <div>
        <el-form-item label="颜色">
          <template>

            <el-checkbox-group @change="onCheckBoxChange"
                               v-model="checkedSpecs.prop1">
              <el-checkbox v-for="(value,index) in prop1" :label="value" :key="index">
                <el-input v-model="prop1[index]"></el-input>
              </el-checkbox>
            </el-checkbox-group>

          </template>
        </el-form-item>
      </div>
      <div>
        <el-form-item label="规格">
          <template>

            <el-checkbox-group @change="onCheckBoxChange"
                               v-model="checkedSpecs.prop2">
              <el-checkbox v-for="(value,index) in prop2" :key="index" :label="value">
                <el-input v-model="prop2[index]"></el-input>
              </el-checkbox>
            </el-checkbox-group>

          </template>
        </el-form-item>
      </div>
      <div>
        <el-form-item label="套装">
          <template>

            <el-checkbox-group @change="onCheckBoxChange"
                               v-model="checkedSpecs.prop3">
              <el-checkbox v-for="value in prop3" :key="value" :label="value">{{value}}</el-checkbox>
            </el-checkbox-group>

          </template>
        </el-form-item>
      </div>
      <!--生成sku 价格库存等信息设置-->

      <el-form-item label="商品规格">
        <template>
          <template v-if="productForm.skuList">
            <el-table
              :data="productForm.skuList"
              style="width: 100%">
              <el-table-column
                prop="prop1"
                label="颜色"
                width="180">
              </el-table-column>
              <el-table-column
                prop="prop2"
                label="规格"
                width="180">
              </el-table-column>
              <el-table-column
                prop="prop3"
                label="套装"
                width="180">
              </el-table-column>
              <el-table-column
                prop="price"
                label="价格">
                <template slot-scope="scope">
                  <el-input v-model="scope.row.price"></el-input>
                </template>
              </el-table-column>
              <el-table-column
                prop="stock"
                label="数量">
                <template slot-scope="scope">
                  <el-input v-model="scope.row.stock"></el-input>
                </template>
              </el-table-column>
            </el-table>
          </template>
          <span v-else>没有数据</span>
        </template>
      </el-form-item>


      <div><h3 style="width: 150px;text-align: right;padding: 0 12px 0 0;font-weight: 700">图文详情</h3></div>
      <hr>
      <!--商品预览图片-->

      <el-form-item label="商品预览图">
        <div class="image-uploader">
          <el-upload
            class="el-upload"
            action="/admin/image/add"
            :show-file-list="false"
            :on-success="onImgUploadSuccess"
            :before-upload="beforeImgUpload">
            <img v-if="productForm.image" :src="baseImgPath+productForm.image" class="image">
            <i v-else class="el-icon-plus image-uploader-icon"></i>
          </el-upload>
        </div>

      </el-form-item>
      <!--商品描述-->
      <el-form-item label="商品描述" prop="desc">
        <el-input type="textarea" v-model="productForm.desc"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('productForm')">立即发布</el-button>
        <el-button @click="resetForm('productForm')">重置</el-button>
      </el-form-item>


    </el-form>
  </div>
</template>

<script>
  import {baseImgPath} from '@/utils/env'

  export default {
    name: "AddProduct",
    data() {
      return {
        categoryValue: [],
        categoryOptions: [],
        productForm: {
          name: 'Mate 30 Pro',
          title: 'Mate 30 Pro AI照亮月环',
          price: '9900',
          shop_id: '',
          cid: '',
          skuList: [],
          image: '',
          specs: ['颜色', '规格']
        },
        rules: {
          name: [
            {required: true, message: '请输入商品名称', trigger: 'blur'},
            {min: 3, max: 32, message: '长度在 3 到 64个字符', trigger: 'blur'}
          ],
          desc: [
            {required: true, message: '请填写商品描述', trigger: 'blur'}
          ]
        },
        baseImgPath: baseImgPath,
        imageUrl: '',
        checkedSpecs: {prop1: [], prop2: [], prop3: []},
        prop1: ['白色', '黑色', '银色'],
        prop2: ['6+128', '8+256'],
        prop3: ['套装1', '套装2', '套装3', '套装4'],
        skuList: []
      };
    },
    methods: {

      handleChange(value) {
        console.log(value);
      },
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            console.log(this.productForm.props)
            return
            this.$api.addProduct(this.productForm).then(res => {
              if (res.code == 1) {
                alert(res.msg)
              } else if (res.msg) {
                alert(res.msg)
              }
            })
          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      onImgUploadSuccess(res) {
        if (res.code == 1) {
          this.productForm.image = res.url;
        } else {
          this.$message.error('上传图片失败！');
        }
      },
      onCheckBoxChange(val) {
        this.productForm.skuList = []
        console.log(typeof (this.checkedSpecs.prop1))
        if (this.checkedSpecs.prop1 && this.checkedSpecs.prop1.length > 0) {
          if (this.checkedSpecs.prop2 && this.checkedSpecs.prop2.length > 0) {
            if (this.checkedSpecs.prop3 && this.checkedSpecs.prop3.length > 0) {
              for (let key1 in this.checkedSpecs.prop1) {
                for (let key2 in this.checkedSpecs.prop2) {
                  for (let key3 in this.checkedSpecs.prop3) {
                    let item = {
                      prop1: this.checkedSpecs.prop1[key1],
                      prop2: this.checkedSpecs.prop2[key2],
                      prop3: this.checkedSpecs.prop3[key3],
                      price: 1800,
                      name: this.productForm.name,
                      stock: 0
                    }
                    this.productForm.skuList.push(item)
                  }
                }
              }
            } else {
              for (let key1 in this.checkedSpecs.prop1) {
                for (let key2 in this.checkedSpecs.prop2) {
                  let item = {
                    prop1: this.checkedSpecs.prop1[key1],
                    prop2: this.checkedSpecs.prop2[key2],
                    prop3: '',
                    price: 1800,
                    name: this.productForm.name,
                    stock: 0
                  }
                  this.productForm.skuList.push(item)
                }
              }
            }
          } else {
            for (let key1 in this.checkedSpecs.prop1) {
              let item = {
                prop1: this.checkedSpecs.prop1[key1],
                prop2: '',
                prop3: '',
                price: 1800,
                name: this.productForm.name,
                stock: 0
              }
              this.productForm.skuList.push(item)
            }
          }
        } else {
          if (this.checkedSpecs.prop2 && this.checkedSpecs.prop2.length > 0
          ) if (this.checkedSpecs.prop3 && this.checkedSpecs.prop3.length > 0) {
            for (let key2 in this.checkedSpecs.prop2) {
              for (let key3 in this.checkedSpecs.prop3) {
                let item = {
                  prop1: '',
                  prop2: this.checkedSpecs.prop2[key2],
                  prop3: this.checkedSpecs.prop3[key3],
                  price: 1800,
                  name: this.productForm.name,
                  stock: 0
                }
                this.productForm.skuList.push(item)
              }
            }
          } else {
            for (let key2 in this.checkedSpecs.prop2) {
              let item = {
                prop1: '',
                prop2: this.checkedSpecs.prop2[key2],
                prop3: '',
                price: 1800,
                name: this.productForm.name,
                stock: 0
              }
              this.productForm.skuList.push(item)
            }
          }
        }

        console.log(this.productForm.skuList)
      },
      beforeImgUpload(file) {
        const isRightType = (file.type === 'image/jpeg') || (file.type === 'image/png') || (file.type === 'image/jpg');
        const isLt2M = file.size / 1024 / 1024 < 2;
        if (!isRightType) {
          this.$message.error('上传头像图片只能是 JPG 格式!');
        }
        if (!isLt2M) {
          this.$message.error('上传头像图片大小不能超过 2MB!');
        }
        return isRightType && isLt2M;
      }
      ,
      getProductCategoryList(){
        this.$api.getProductCategoryList().then(res=>{
          this.categoryOptions=res.data
        })
      }
    },
    created() {
      this.getProductCategoryList()
    }

  }
</script>

<style lang="scss" scoped>
  .createPost-container {
    margin-top: 20px;
  }

  .image-uploader {
    .el-upload {
      border: 1px dashed #d9d9d9;
      border-radius: 6px;
      cursor: pointer;
      position: relative;
      overflow: hidden;

      &:hover,
      &:focus {
        border-color: #409eff;
      }
    }

    .image-uploader-icon {
      font-size: 28px;
      color: #8c939d;
      width: 178px;
      height: 178px;
      line-height: 178px;
      text-align: center;
    }

    .image {
      width: auto;
      height: 178px;
      display: block;
    }
  }

  hr {
    height: 1px;
    border: none;
    opacity: 0.2;
    border-top: 1px solid #343a40;
  }
</style>
