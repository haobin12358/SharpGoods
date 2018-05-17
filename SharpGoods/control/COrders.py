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
from service.SCoupons import SCoupons
from config import conversion as cvs

from common.get_str import get_str
from common.get_model_return_list import get_model_return_list, get_model_return_dict
from common.timeformate import get_db_time_str, get_web_time_str

class COrders():
    def __init__(self):
        self.sorder = SOrders()
        self.slocation = SLocations()
        self.sproduct = SProduct()
        self.scoupons = SCoupons()
        self.title = '============{0}============'

    def get_order_list(self):
        try:
            args = request.args.to_dict()
            if "token" not in args:
                return PARAMS_MISS
            order_list = get_model_return_list(self.sorder.get_order_main_list_by_usid(get_str(args, "token")))

            data = import_status("SUCCESS_MESSAGE_GET_ORDER_LIST", "OK")

            for order_main in order_list:
                self.get_order_abo_by_order_main(order_main)

            data["data"] = order_list
            return data
        except Exception as e:
            print(self.title.format("ERROR MSG"))
            print(e.message)
            print(self.title.format("ERROR MSG"))
            return SYSTEM_ERROR

    def get_order_abo(self):
        try:
            args = request.args.to_dict()
            if "token" not in args or "OMid" not in args:
                return PARAMS_MISS

            order_main = get_model_return_dict(self.sorder.get_order_main_by_om_id(get_str(args, "OMid")))
            self.get_order_abo_by_order_main(order_main)
            data = import_status("SUCCESS_MESSAGE_GET_ORDER_ABO", "OK")
            data["data"] = order_main
            return data
        except Exception as e:
            print(self.title.format("ERROR MSG"))
            print(e.message)
            print(self.title.format("ERROR MSG"))
            return SYSTEM_ERROR

    def make_order(self):
        args = request.args.to_dict()
        if "token" not in args:
            return PARAMS_MISS

        data = json.loads(request.data)
        if "LOid" not in data:
            print("LOid is not find")
            return PARAMS_MISS
        import uuid
        omid = str(uuid.uuid4())
        order_main = {
            "OMid": omid,
            "LOid": get_str(data, "LOid"),
            "OMabo": get_str(data, "OMmessage"),
            "USid": args.get("token"),
            "OMcointype": cvs.conversion_PBunit_reverse.get(get_str(data, "OMcointype"), 402),
            "COid": get_str(data, "COid"),
            "OMprice": float(get_str(data, "OMprice")),
            "OMtime": get_db_time_str(),
            "OMstatus": cvs.conversion_OMstatus_reverse.get(get_str(data, "OMstatus"))
        }
        self.sorder.add_model("OrderMain", **order_main)

        order_part_list = data.get("order_items")
        if not order_part_list:
            print("order items not find")
            return PARAMS_MISS
        for order_part_info in order_part_list:
            try:
                order_part = {
                    "OPid": str( uuid.uuid4()),
                    "OMid": omid,
                    "PBid": get_str(order_part_info, "PBid"),
                    "PRnumber": int(get_str(order_part_info, "PRnumber"))
                }
                self.sorder.add_model("Orderpart", **order_part)
            except Exception as e:
                print(self.title.format("ERROR MSG"))
                print(e.message)
                print(self.title.format("ERROR MSG"))
                return SYSTEM_ERROR

        data = import_status("SUCCESS_MESSAGE_ADD_ORDER", "OK")
        data["data"] = {"OMid": omid}
        return data

    def update_order_status(self):
        return {
            "status":200,
            "messages":"更新订单状态成功"
        }

    def get_product_into_order_abo(self, pbid):
        product = get_model_return_dict(self.sproduct.get_product_by_pbid(pbid))
        product.update(get_model_return_dict(self.sproduct.get_product_by_prid(product.get("PRid"))))
        product.update(self.get_brinfo(product.get("BRid")))
        product["PBunit"] = cvs.conversion_PBunit.get(product.get("PBunit", "其他币种"))
        product["PRbrand"] = cvs.conversion_PRbrand.get(product.get("PRbrand"), "其他")
        product["PRtype"] = cvs.conversion_PRtype.get(product.get("PRtype"))
        return product

    def get_order_abo_by_order_main(self, order_main):
        order_part_list = get_model_return_list(self.sorder.get_order_part_list_by_omid(order_main.get("OMid")))
        for order_part in order_part_list:
            order_part.update(self.get_product_into_order_abo(order_part.get("PBid")))

        order_main["order_abo"] = order_part_list
        order_main["OMcointype"] = cvs.conversion_PBunit.get(order_main.get("OMcointype"), "其他币种")
        order_main["OMstatus"] = cvs.conversion_OMstatus.get(order_main.get("OMstatus"), 0)
        order_main["OMtime"] = get_web_time_str(order_main.get("OMtime"))
        location = get_model_return_dict(self.slocation.get_location_by_loid(order_main.get("LOid")))
        if location.get("LOisedit") == 303:
            print(import_status("ERROR_MESSAGE_GET_LOCATION", "WORING_LOCATION"))
        order_main.update(location)
        coupon = get_model_return_dict(self.scoupons.get_coupons_by_couid(order_main.get("COid")))
        order_main.update(coupon)

    def get_brinfo(self, brid):
        brinfo = {}
        while True:
            brand = get_model_return_dict(self.sproduct.get_brand_by_brid(brid))
            if not (brand.get("BRkey") and brand.get("BRvalue")):
                error = "the brand does not have BRkey or BRvalue. brand = {0}".format(brand)
                raise Exception(error)

            if brand.get("BRkey") in brinfo:
                raise Exception("the product has duplicate brand = {0}".format(brand))

            brinfo[brand.get("BRkey")] = brand.get("BRvalue")

            if brand.get("BRfromid") == "0":
                break
            brid = brand.get("BRfromid")

        return brinfo
