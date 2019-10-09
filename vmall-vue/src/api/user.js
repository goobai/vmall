/**
 * user模块接口列表
 */
import axios from '../utils/http' // 导入http中创建的axios实例


export const userReg = (username, password, phone, smsCode) => axios.post('/api/user/reg', {
  username: username, password: password, smsCode: smsCode, phone: phone
})
export const userLogin = (username, password) => axios.post('/api/user/login', {
  username: username, password: password
})
export const getUserCard = (params) => axios.get('/api/user/' + params.name + '/card')

export const getUserAddresses = () => axios.get('/api/user/addresses')
export const getUserAddress = (params) => {
  if (params.id) {
    return axios.get('/api/user/address?id=' + params.id)
  } else {
    return axios.get('/api/user/address')
  }
}

export const editAddress = (params) => axios.post('/api/user/address', params)




