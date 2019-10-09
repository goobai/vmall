import {setStore, removeStore, getStore} from '@/utils/storage'

const TokenKey = 'access_token'

export function getToken() {
  return getStore(TokenKey)
}

export function setToken(token) {
  return setStore(TokenKey, token)
}

export function removeToken() {
  return removeStore(TokenKey)
}

