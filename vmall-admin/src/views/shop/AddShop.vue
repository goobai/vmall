<template>
  <div class="createPost-container">
    <el-form :model="shopForm" :rules="rules" ref="shopForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="商铺名称" prop="name">
        <el-input v-model="shopForm.name"></el-input>
      </el-form-item>
      <el-form-item label="商铺logo" prop="logo">
        <div class="image-uploader">
          <el-upload
            class="el-upload"
            :action=" '/admin/image/add'"
            :show-file-list="false"
            :on-success="onImgUploadSuccess"
            :before-upload="beforeImgUpload">
            <img v-if="shopForm.logo" :src="baseImgPath+shopForm.logo" class="image">
            <i v-else class="el-icon-plus image-uploader-icon"></i>
          </el-upload>
        </div>
      </el-form-item>
      <el-form-item label="商铺status" prop="status">
        <el-select v-model="shopForm.status" placeholder="请选择状态">
          <el-option label="非正常" value="0"></el-option>
          <el-option label="正常" value="1"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="商铺描述" prop="desc">
        <el-input type="textarea" v-model="shopForm.desc"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('shopForm')">立即创建</el-button>
        <el-button @click="resetForm('shopForm')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  import {baseImgPath} from '@/utils/env'

  export default {
    name: "AddShop",
    data() {
      return {
        shopForm: {
          name: 'vmall国际化旗舰店',
          image: '',
          logo: '',
          desc: 'vmall国际化旗舰店 dec'
        },
        rules: {
          name: [
            {required: true, message: '请输入店铺名称', trigger: 'blur'},
            {min: 3, max: 32, message: '长度在 3 到 64个字符', trigger: 'blur'}
          ],
          desc: [
            {required: true, message: '请填写店铺描述', trigger: 'blur'}
          ]
        },
        baseImgPath: baseImgPath
      };
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.$api.addShop(this.shopForm).then(res => {
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
      onImgUploadSuccess(res, file) {
        if (res.code == 1) {
          this.shopForm.logo = res.url;
        } else {
          this.$message.error('上传图片失败！');
        }
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
    }
  }
</script>

<style lang="scss" scoped>
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
</style>
