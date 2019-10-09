import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './config/rem'
import api from './api'
import {
  Icon,
  Tabbar,
  TabbarItem,
  Button,
  Cell,
  Field,
  Row,
  Col,
  Search,
  NavBar,
  Toast,
  CellGroup,
  Lazyload,
  Swipe,
  SwipeItem,
  Tab,
  Tabs,
  GoodsAction,
  GoodsActionIcon,
  GoodsActionButton,
  Tag,
  Sku,
  Sidebar,
  SidebarItem
} from 'vant'
import 'vant/lib/index.css'
import {library} from '@fortawesome/fontawesome-svg-core'
import {fas} from '@fortawesome/free-solid-svg-icons'
import {far, faCommentAlt} from '@fortawesome/free-regular-svg-icons'
import {fab} from '@fortawesome/free-brands-svg-icons'
import {FontAwesomeIcon, FontAwesomeLayers, FontAwesomeLayersText} from '@fortawesome/vue-fontawesome'

Vue.prototype.$api = api
library.add(fas, far, fab, faCommentAlt)

Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.component('font-awesome-layers', FontAwesomeLayers)
Vue.component('font-awesome-layers-text', FontAwesomeLayersText)
Vue.use(Button).use(Tabbar).use(TabbarItem).use(Icon).use(Cell).use(Field).use(Row).use(Col).use(Search).use(NavBar).use(Toast).use(CellGroup).use(Lazyload).use(Swipe).use(SwipeItem).use(Tab).use(Tabs).use(GoodsAction).use(GoodsActionButton).use(GoodsActionIcon).use(Tag).use(Sku).use(Sidebar).use(SidebarItem)
Vue.config.productionTip = false
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
