# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
from common.import_status import import_status
from config.response import SYSTEM_ERROR, PARAMS_MISS
from service.SOrders import SOrders
from service.SProduct import SProduct
from service.SLocations import SLocations
from service.
from config import conversion as cvs

from common.get_str import get_str
from common.get_model_return_list import get_model_return_list, get_model_return_dict


class COrders():
    def __init__(self):
        self.sorder = SOrders()
        self.slocation = SLocations()
        self.sproduct = SProduct()
        self.scoupons = S
        self.title = '============{0}============'

    def get_order_list(self):
        args = request.args.to_dict()
        if "token" not in args:
            return PARAMS_MISS
        order_list = get_model_return_list(self.sorder.get_order_main_list_by_usid(get_str(args, "token")))
        data = import_status("SUCCESS_MESSAGE_GET_ORDER_LIST", "OK")

        for order_main in order_list:
            order_part_list = get_model_return_list(self.sorder.get_order_part_list_by_omid(order_main.get("OMid")))
            for order_part in order_part_list:
                order_part.update(self.update_product_into_order_abo(order_part.get("PBid")))

            order_main["order_abo"] = order_part_list
            order_main["OMcointype"] = cvs.conversion_PBunit.get(order_main.get("OMcointype"), "其他币种")
            order_main["OMstatus"] = cvs.conversion_OMstatus.get(order_main.get("OMstatus"), 0)
            location = get_model_return_dict(self.slocation.get_location_by_loid(order_main.get("LOid")))
            if location.get("LOisedit") == 303:
                print(import_status("ERROR_MESSAGE_GET_LOCATION", "WORING_LOCATION"))
            order_main.update(location)
            coupon = self.
        data["data"] = order_list
        return data

    def get_order_abo(self):
        args = request.args.to_dict()
        if "token" not in args or "OMid" not in args:
            return PARAMS_MISS
        order_abo = get_model_return_dict(self.sorder.get_order_abo_by_omid(
            get_str(args, "token"), get_str(args, "OMid")))

        return {
            "status": 200,
            "messages": "获取订单列表成功",
            "data":{
                "OMid": "123",
                "OMtime": "2018-05-13 10:38:22",
                "OMstatus": "已支付/未支付/配送中/已完成/已评价",
                "ADname": "收件人姓名",
                "OMcointype": "$",
                "OMtotal": 4.35
            }

        }

    def make_order(self):
        return {
            "status":200,
            "messages":"创建订单成功",
            "data":{
                "OMid":"123"
            }
        }

    def update_order_status(self):
        return {
            "status":200,
            "messages":"更新订单状态成功"
        }

    def update_product_into_order_abo(self, pbid):
        product = get_model_return_dict(self.sproduct.get_product_by_pbid(pbid))
        product["PBunit"] = cvs.conversion_PBunit.get(product.get("PBunit", "其他币种"))
        product["PRbrand"] = cvs.conversion_PRbrand.get(product.get("PRbrand"), "其他")
        product["PRtype"] = cvs.conversion_PRtype.get(product.get("PRtype"))
        return product