/**
 * product模块接口列表
 */

import axios from '../utils/http' // 导入http中创建的axios实例

export const getRootCategory = () => axios.get('/api/categories ')
export const getCategoryList = (id) => axios.get('/api/category?id=' + id)

export const getProductInfo = (id) => axios.post('/api/product/' + id + '/')

export const getProductsList = (type, cid, offset, keyword) => axios.get('/api/products', {
  params: {
    type: type,
    cid: cid,
    keyword: keyword,
    offset: offset
  }
})



