import axios from '../utils/http' // 导入http中创建的axios实例

export const getRecommendProducts = (params) => axios.get('/api/recommend/products', {
  params: {
    'offset': params.offset,
    'type': params.type,
  }
})
