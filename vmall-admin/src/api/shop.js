/**
 * shop模块接口列表
 */
import axios from '../utils/http' // 导入http中创建的axios实例

//获取商铺列表
export const getShopList = (params) => axios.get('/admin/shop/list', {
  params: {
    'page': params.page,
    'limit': params.limit,
  }
})
//新增商铺
export const addShop = (params) => axios.post('/admin/shop/create', {
  'name': params.name,
  'logo': params.logo,
  'status': params.status,
})
//更新商铺信息
export const editShop = (params) => axios.post('/admin/shop/update', {
  'id': params.id,
  'name': params.name,
  'logo': params.logo,
  'status': params.status,
})
//删除商铺
export const delShop = (params) => axios.post('/admin/shop/del', {
  id:params.id
})
