/**
 * api接口的统一出口
 */
// 文章模块接口
import {
  opCartProduct,
  getCartProducts,
  modifyCartProductsChecked,
  postOrderProducts,
  getOrderConfirmData
} from '../api/cart'
import {sendMessage, receiveMessage,} from './chat'
import {getMyOrder} from './order'
import {getRootCategory, getProductInfo, getCategoryList, getProductsList,} from './product'
import {getRecommendProducts} from '../api/recommend'
import {getUserAddress, getUserCard, userLogin, userReg, getUserAddresses, editAddress} from '../api/user'

// 其他模块的接口……

// 导出接口
export default {

  opCartProduct, getCartProducts, modifyCartProductsChecked, postOrderProducts, getOrderConfirmData,
  sendMessage, receiveMessage,
  getMyOrder,
  getRootCategory, getProductInfo, getCategoryList, getProductsList, getRecommendProducts,
  getUserCard, userLogin, userReg, getUserAddresses, getUserAddress, editAddress

}
