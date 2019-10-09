/**
 * chat模块接口列表
 */

import axios from '../utils/http' // 导入http中创建的axios实例

export const sendMessage = (params) => axios.post('/api/chat/send', {
  'body': params.body,
  'receiver': params.receiver,

})

export const receiveMessage = (params) => axios.post('/api/chat/receive', {
  'receiver': params.receiver,
  'offset': params.offset

})

