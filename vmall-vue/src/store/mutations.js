import { GET_USER_INFO, RecordRefreshToken ,RecordAccessToken,RecordLoginState,RecordUserInfo} from './mutation-types'
import { getStore, setStore } from '../utils/storage'

export default {

  [RecordAccessToken] (state, accessToken) {
    state.accessToken = accessToken
    setStore('access_token',accessToken)
  },
   [RecordRefreshToken] (state, refreshToken) {
    state.refreshToken = refreshToken
    setStore('refresh_token',refreshToken)
  },
  [RecordUserInfo] (state, userInfo) {
    state.userInfo = userInfo
    setStore('user_info',userInfo)
  },

  [RecordLoginState] (state, status) {
    state.login = status
    setStore('login',status)
  },
}
