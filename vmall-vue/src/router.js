import Vue from 'vue'
import Router from 'vue-router'
import Main from './views/Main'
import Home from './views/home/Home'
import ChatHome from './views/chat/Home'
import Category from './views/category/Category'
import Cart from './views/cart/Cart'
import MyCenter from './views/my/Index'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Main,
      children: [
        {
          path: '',
          redirect: Home
        },
        {
          path: 'home',
          name: 'Home',
          component: Home,
        },
        {
          path: 'chat',
          name: 'ChatHome',
          component: ChatHome
        },
        {
          path: 'category',
          name: 'Category',
          component: Category
        },
        {
          path: 'cart',
          name: 'Cart',
          component: Cart
        },
        {
          path: 'my/home',
          name: 'MyCenter',
          component: MyCenter
        }
      ]
    },
    {
      path: '/register',
      name: 'Register',
      component: () => import(/* webpackChunkName: "register" */ './views/register/Register.vue')
    },

    {
      path: '/login',
      name: 'Login',
      component: () => import(/* webpackChunkName: "login" */ './views/login/Login.vue')
    },
    {
      path: '/search',
      name: 'Search',
      component: () => import(/* webpackChunkName: "search" */ './views/search/Search.vue')
    },

    {
      path: '/product',
      name: 'Product',
      component: () => import(/* webpackChunkName: "product" */ './views/product/Product.vue')
    }
    ,
    {
      path: '/products',
      name: 'Products',
      component: () => import(/* webpackChunkName: "products" */ './views/product/Products.vue')
    },
    // { path: '*', redirect: '/' }
    {
      path: '/scroll',
      name: 'Scroll',
      component: () => import(/* webpackChunkName: "Scroll" */ './views/scroll/Scroll.vue')
    },
    {
      path: '/order/confirm',
      name: 'ConfirmOrder',
      component: () => import(/* webpackChunkName: "products" */ './views/order/ConfirmOrder.vue')
    },
    {
      path: '/order/pay',
      name: 'OrderPay',
      component: () => import(/* webpackChunkName: "products" */ './views/order/OrderPay.vue')
    },

    {
      path: '/my/order',
      name: 'MyOrder',
      component: () => import(/* webpackChunkName: "products" */ './views/my/MyOrder.vue')
    },
    {
      path: '/chat/:receiver',
      name: 'Chat',
      component: () => import(/* webpackChunkName: "products" */ './views/chat/Chat.vue')
    },

    {
      path: '/address',
      name: 'AddressIndex',
      component: () => import(/* webpackChunkName: "products" */ './views/address/Index.vue')
    },
    {
      path: '/address/edit',
      name: 'AddressEdit',
      component: () => import(/* webpackChunkName: "products" */ './views/address/Edit.vue')
    },
  ]
})
