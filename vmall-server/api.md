#  接口文档
```
vmall:

```

## 目录：

* [商品](#商品)
* [用户](#用户)
* [订单](#订单)
* [购物车](#购物车)
* [售后](#售后)
* [店铺](#店铺)
* [后台管理](#后台管理)


## 接口列表：

### 接口返回格式
|参数|是否必选|类型|说明|
|:-----|:-------:|:-----|:-----|
|code     |Y       |int    | 后台处理结果码 0：失败 1：成功 |
|data     |Y       |dict   | 数据|
|msg      |Y       |string |说明 |

### 商品

#### 请求URL:

|url|方法|说明|
|:-----|:-----|:-----|
|categories |get/post| 根分类列表查询 |
|category     |get/post| 分类列表查询|
|products      |/get/post|商品列表查询 |
|/product/<int:id>/|get/post|查看商品详情 |
|/recommend/products|get/post|推荐商品 |

```javascript
```


### 用户


#### 请求URL:
|url|方法|说明|
|:-----|:-----|:-----|
|/user/reg|get/post|注册|
|/user/login|get/post|登陆|
|/user/<username>|get/post/changepwd|修改密码|
|/user/address|get/post|地址操作相关|
|/user/addresses|get/post|查询地址列表|




#### 请求方式: `post`


#### 参数类型：json

|参数|是否必选|类型|说明|
|:-----|:-------:|:-----|:-----|
|username      |Y       |string  |用户名 |
|password      |Y       |string  |登陆密码 |

#### 请求示例
``` json
curl -X POST \
  http://127.0.0.1:5000/api/users/login \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 50a24e0f-ea1d-4960-af43-4bfc069e1f38' \
  -H 'cache-control: no-cache' \
  -d '{"username":"goobai",
"password":"1"}'
```
#### 返回示例：

``` javascript
{
    "code": 1,
    "data": {
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTM3OTQ4NTQsIm5iZiI6MTU1Mzc5NDg1NCwianRpIjoiY2NkZDRlOTQtY2YxMi00OTU2LTlkZTktZjQ3ZTAxOTI5Nzc0IiwiZXhwIjoxNTUzNzk1NzU0LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIiwidXNlcl9jbGFpbXMiOnsiaWQiOjEsIm5pY2tuYW1lIjoiZ29vYmFpIiwic2V4IjoiTmEiLCJzaWduYXR1cmUiOm51bGwsImxhc3RzZWVuIjoiMjAxOS0wMy0yOFQxNzo0MDoyMVoiLCJmb2xsb3dlZCI6MCwiZm9sbG93ZXJzIjowLCJhdmF0YXJfdXJsIjoiIn19.QOe4Hyu4aD71011eV57hBPVm9a76Dpe51IKCmC5DCt8",
        "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTM3OTQ4NTQsIm5iZiI6MTU1Mzc5NDg1NCwianRpIjoiYmM3Zjg2Y2YtMDNkMS00OWYwLTgzY2EtNjg4MzdlYTVhNzZmIiwiZXhwIjoxNTU2Mzg2ODU0LCJpZGVudGl0eSI6MSwidHlwZSI6InJlZnJlc2gifQ.5iPGoYoYry2nIOrfUplJvdmdcL7dnhdCNlvEDXAofbY"
    },
    "message": "登陆成功！"
}
```


### 订单

#### 请求URL:
|url|方法|说明|
|:-----|:-----|:-----|
|/order/confirm|get/post|生成订单|
|/order/pay|get/post|支付|
|/order/confirm/products/|get/post|获取订单确认商品|
|/orders|get/post|查询订单信息|


### 购物车
#### 请求URL:
|url|方法|说明|
|:-----|:-----|:-----|
|/cart/product|get/post|修改购物车中商品数量|
|/cart/products|get/post|查询购物车中的所有商品|
|/cart/products/check|get/post|获取订单确认商品|
|/orders|get/post|修改购物车中商品的选择状态|
### 售后

#### 请求URL:
|url|方法|说明|
|:-----|:-----|:-----|
|/cart/product|get/post|修改购物车中商品数量|
|/cart/products|get/post|查询购物车中的所有商品|
|/cart/products/check|get/post|获取订单确认商品|
|/orders|get/post|修改购物车中商品的选择状态|
### 店铺

#### 请求URL:
|url|方法|说明|
|:-----|:-----|:-----|
|/shop/products|get|查询/管理店铺商品列表|
|/shop/product|get/post|添加/修改店铺商品|
|/shop/orders|get|获取店铺订单列表|
|/shop/order|get/post|查询/修改店铺订单|

###后台管理
#### 请求URL:
|url|方法|说明|
|:-----|:-----|:-----|
|/admin/system|get/post|系统状态|
|/admin/shop|get/post|店铺管理|
|/admin/user|get/post|用户管理|
|/admin/products|get/post|商品管理|
|/admin/orders|get/post|订单管理|
