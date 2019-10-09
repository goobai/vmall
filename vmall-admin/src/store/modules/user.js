import {userLogin, getUser} from '@/api/user'
import {setStore, getStore, removeStore} from '@/utils/storage'
import {resetRouter} from '@/router'

const state = {
  access_token: getStore('access_token'),
  name: getStore('name'),
  avatar: getStore('avatar')
}

const mutations = {
  SET_ACCESS_TOKEN: (state, accessToken) => {
    setStore('access_token',accessToken)
    state.access_token = accessToken
  },
  SET_NAME: (state, name) => {
    setStore('name', name)
    state.name = name
  },
  SET_AVATAR: (state, avatar) => {
    setStore('avatar', avatar)
    state.avatar = avatar
  }
}

const actions = {
  // user login
  login({commit}, userInfo) {
    return new Promise((resolve, reject) => {
      userLogin(userInfo).then(res => {
        commit('SET_ACCESS_TOKEN', res.data.access_token)
        commit('SET_NAME', res.data.user_info.name)
        commit('SET_AVATAR', res.data.user_info.avatar)
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get user info
  getInfo({commit, state}) {
    return new Promise((resolve, reject) => {
      getUser(state.access_token).then(res => {

        if (!res) {
          reject('登陆失败，请重试.')
        }
        commit('SET_NAME', res.data.name)
        commit('SET_AVATAR', res.data.avatar)
        resolve(res.data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user logout
  logout({commit, state}) {
    return new Promise((resolve, reject) => {
      commit('SET_ACCESS_TOKEN', '')
      commit('SET_AVATAR', '')
      commit('SET_NAME', '')
      removeStore('access_token')
      removeStore('name')
      removeStore('avatar')
      resetRouter()
      resolve()
    })
  },

  resetToken({commit}) {
    return new Promise(resolve => {
      commit('SET_ACCESS_TOKEN', '')
      commit('SET_AVATAR', '')
      commit('SET_NAME', '')
      removeStore('access_token')
      removeStore('name')
      removeStore('avatar')
      resetRouter()
      resolve()
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}


