import {
    wxRequest
} from '../utils/wxRequest';

// const api2api = 'https://h878.cn/love/breakfast'
// const api2 = 'http://120.79.182.43:7444/sharp'
const api2 = 'https://h878.cn/sharp'

//登录 注册
const getValidate = (params) => wxRequest(params, api2+'/goods/users/get_inforcode')
const getText = () => wxRequest('', api2+'/goods/other/disclaimer')
const login = (params) => wxRequest(params, api2+'/goods/users/login')
const register = (params) => wxRequest(params, api2+'/goods/users/register')

//首页
const getProductAll = () => wxRequest('',api2+'/goods/product/get_all')

//商品详情
const getProductInfo = (params) => wxRequest(params, api2+'/goods/product/get_info_by_id')
const getLeft = (params) => wxRequest(params, api2 + '/goods/product/get_control_brand?PRid='+params.PRid+ '&token=' + params.token)
const getPBid = (params) => wxRequest(params, api2+'/goods/product/get_pbid_by_all_brand?PRid='+params.PRid+ '&token=' +params.token)

//个人
const getUserInfo = (params) => wxRequest(params, api2+'/goods/users/all_info')
const updateUserInfo = (params) => wxRequest(params, api2+'/goods/users/update_info?token=' + params.token)
const updatePass = (params) => wxRequest(params, api2+ '/goods/users/update_pwd')

//
// http://120.79.182.43:7444/sharp/goods/product/get_all?
//地址
const getAddress = (params) => wxRequest(params, api2+'/goods/locations/get_all_location')
const editAddress = (params) => wxRequest(params, api2+ '/goods/locations/update_location?token='+ params.token)
const saveAddress = (params) => wxRequest(params, api2+ '/goods/locations/new_location?token='+ params.token)
const deleteAddress = (params) => wxRequest(params, api2+'/goods/locations/del_location')

//支付
const getAllPrice = (params) => wxRequest(params, api2+'/goods/orders/order_price?token='+params.token)
const makeOrder = (params) => wxRequest(params, api2+'/goods/orders/make_main_order?token='+ params.token);
const getOpenID = (params) => wxRequest(params, pai2+'/goods/other/openid')
const getPayParam = (params) => wxRequest(params, api2+'/goods/other/payconfig')

//订单
const getSelectProduct = (params,token) => wxRequest(params,api2 + '/goods/cart/get_select_product?token=' + token);//获取已选中商品
const getOrderList = (params) => wxRequest(params, api2+'/goods/orders/get_order_list')
const getOrderInfo = (params) => wxRequest(params, api2+'/goods/orders/get_order_abo?token='+params.token+'&OMid='+params.OMid)
const updateOrderStatus = (params) => wxRequest(params, api2+ '/goods/orders/update_order_status?token=' + params.token)
// const getGoodInfo = (params) => wxRequest(params, api2+'/orders/get_order_abo')
const getComment = (params) => wxRequest(params, api2+'/goods/review/get_review')
const makeComment = (params) => wxRequest(params, api2+'/goods/review/create_review?token=' + params.token + '&OMid=' + params.OMid);
const logistics = (params) => wxRequest(params,api2 + '/goods/other/logistics');

//购物车 4a72a9ac-4118-4358-8eeb-5ccd155674df
const getCartList = (params) => wxRequest(params, api2+'/goods/cart/get_all')
const operateCart = (params) => wxRequest(params, api2+'/goods/cart/update?token='+params.token)
// const deleteCart = (params) => wxRequest(params, api2+'/delete_product?token='+params.token)

//优惠券
const getTicketAll = (params) => wxRequest(params, api2+ '/goods/card/get_cardpkg')

//评价
module.exports = {
    getValidate, register, login, getUserInfo,getPBid,
    getProductInfo,getAddress,editAddress,getText,getLeft,
    getOrderList, getOrderInfo, getCartList, operateCart,
    // getGoodInfo,
    getSelectProduct,logistics,
    getProductAll,getTicketAll,makeOrder,saveAddress,getAllPrice,
    getPayParam,getOpenID,getComment,makeComment,deleteAddress,
    updateUserInfo, updatePass,updateOrderStatus

}
