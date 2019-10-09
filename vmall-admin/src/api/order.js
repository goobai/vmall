/**
 * user模块接口列表
 */

import axios from '../utils/http' // 导入http中创建的axios实例

//订单状态状态 0:生成订单，待付款 ；1：付款完成，待发货；2：发货完成，物流中，待确认收货 ；3：确认收货，待评价 4：评价完商品，订单完成

export const getOrderList = (params) => axios.get('/admin/order/list', {
  params: {
    'page': params.page,
    'limit': params.limit,
  }
})

