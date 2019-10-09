/**
 * cart模块接口列表
 */

import axios from '../utils/http'

//向购物车添加 修改 删除商品
//id:商品sku id
//type:0 ：添加商品, 1：从购物车删除商品 ,2:修改购物车商品数量
//count:将要把商品数量修改为count值
export const opCartProduct = (id, type = 0, count = 1) => axios.post('/api/cart/product', {
    id: id,
    type: type,
    count: count,
  }
)

//查询购物车商品所有商品
export const getCartProducts = () => axios.get('/api/cart/products')
// # 修改购物车商品check状态
// # 修改类型 m_type 0：所有商品 1：店铺 2：单个商品
// # 修改check状态 c_type 0：unchecked 1:checked,
// # pid :商品 sku id
// # shop_id :店铺id
export const modifyCartProductsChecked = (m_type, c_type, pid = 0, shop_id = 0) => axios.post('/api/cart/products/check', {
  m_type: m_type,
  c_type: c_type,
  pid: pid,
  shop_id: shop_id
})

//生成订单 订单生成成功后将商品从购物车移除
export const postOrderProducts = (products, address_id) => axios.post('/api/order/confirm', {
  products: products,
  address_id: address_id,

})

//"""获取订单确认商品"""
export const getOrderConfirmData = () => axios.post('/api/order/confirm/products/')

