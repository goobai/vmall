import Vue from 'vue'
import Vuex from 'vuex'
import mutations from './mutations'
import actions from './actions'
import getters from './getters'
import { getStore,getStore2Obj } from '../utils/storage'

Vue.use(Vuex)

const state = {
  accessToken: getStore('access_token'),
  refreshToken: getStore('refresh_token'),
  login: getStore('login'),
  // userInfo: getStore('user_info'),//用户信息
  userInfo: getStore2Obj('user_info'),//用户信息
}

export default new Vuex.Store({
  state, getters, actions, mutations
})
