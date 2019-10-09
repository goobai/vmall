import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [{
      path: 'dashboard',
      name: 'Dashboard',
      component: () => import('@/views/dashboard/index'),
      meta: {title: '首页', icon: 'dashboard'}
    }]
  }
  ,
  {
    path: '/shop',
    component: Layout,
    redirect: '/shop/index',
    meta: {title: '店铺管理', icon: 'shop'},
    children: [
      {
        path: 'index',
        name: 'Shop',
        component: () => import('@/views/shop/Index'),
        meta: {title: '店铺列表', icon: ''}
      },
      {
        path: 'addshop',
        name: 'AddShop',
        component: () => import('@/views/shop/AddShop'),
        meta: {title: '添加店铺', icon: ''}
      }
      ,

    ]
  },
  {
    path: '/product',
    component: Layout,
    redirect: '/product/index',
    meta: {title: '商品管理', icon: 'product'},
    children: [
      {
        path: 'index',
        name: 'Product',
        component: () => import('@/views/product/Index'),
        meta: {title: '商品列表', icon: ''}
      },
      {
        path: 'addproduct',
        name: 'AddProduct',
        component: () => import('@/views/product/AddProduct'),
        meta: {title: '添加商品', icon: ''}
      }
      ,

    ]
  },
  {
    path: '/order',
    component: Layout,
    redirect: '/order/index',
    meta: {title: '订单管理', icon: 'order'},
    children: [
      {
        path: 'index',
        name: 'Order',
        component: () => import('@/views/order/Index'),
        meta: {title: '订单列表', icon: ''}
      },

      {
        path: 'editorder',
        name: 'EditOrder',
        component: () => import('@/views/order/EditOrder'),
        meta: {title: '编辑订单', icon: ''}
      }
    ]
  },
  {
    path: '/setting',
    component: Layout,
    redirect: 'setting/index',
    name: 'Setting',
    meta: {title: '系统设置', icon: 'setting'},
    children: [
      {
        path: 'index',
        name: 'Index',
        component: () => import('@/views/setting/Index'),
        meta: {title: '首页', icon: ''}
      },
      {
        path: 'user',
        name: 'User',
        component: () => import('@/views/setting/User'),
        meta: {title: '用户管理', icon: ''}
      },
      {
        path: 'role',
        name: 'Role',
        component: () => import('@/views/setting/Role'),
        meta: {title: '角色管理', icon: ''}
      }, {
        path: 'permission',
        name: 'Permission',
        component: () => import('@/views/setting/Permission'),
        meta: {title: '权限管理', icon: ''}
      },]

  },
  {
    path: 'external-link',
    component: Layout,
    children: [
      {
        path: 'https://panjiachen.github.io/vue-element-admin-site/#/',
        meta: {title: 'External Link', icon: 'link'}
      }
    ]
  },

  // 404 page must be placed at the end !!!
  {path: '*', redirect: '/404', hidden: true}
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({y: 0}),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
