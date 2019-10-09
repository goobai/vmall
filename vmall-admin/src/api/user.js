/**
 * user模块接口列表
 */
import axios from '../utils/http' // 导入http中创建的axios实例


export const userReg = (params) => axios.post('/admin/user/reg', {
  username: params.username, password: params.password, smsCode: params.smsCode, phone: params.phone
})
export const userLogin = (params) => axios.post('/admin/user/login', {
  username: params.username, password: params.password
})


export const getUser = (params) => axios.get('/admin/user', {
  params: {
    'name': params.name,
  }
})
