/**
 * api接口的统一出口
 */
// 文章模块接口

import {getOrderList} from './order'
import {getProductList, addProduct, editProduct, delProduct} from './product'
import {userLogin} from './user'
import {getShopList, addShop, editShop, delShop} from './shop'
// 其他模块的接口……

// 导出接口
export default {
  getProductList, addProduct, editProduct, delProduct,
  userLogin,
  getShopList, addShop, editShop, delShop
}
