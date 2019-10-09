/**
 * product模块接口列表
 */

import axios from '../utils/http' // 导入http中创建的axios实例




//获取商品列表
export const getProductList = (params) => axios.get('/admin/product/list', {
  params: {
    'page': params.page,
    'limit': params.limit,
  }
})
//新增商品
export const addProduct = (params) => axios.post('/admin/product/create', {
  'name': params.name,
  'logo': params.logo,
  'status': params.status,
})
//更新商品信息
export const editProduct = (params) => axios.post('/admin/product/update', {
  'id': params.id,
  'name': params.name,
  'price': params.price,
  'stock': params.stock,
  'status': params.status,
})
//删除商品
export const delProduct = (params) => axios.post('/admin/product/del', {
  id: params.id
})



