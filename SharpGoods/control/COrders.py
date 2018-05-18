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
        self.order_main_params = ["OMstatus", "OMprice", "LOid", "OMabo", "COid", "OMcointype", "order_item"]
        self.order_part_param = ["PBid", "PRnumber"]

    def get_order_list(self):
        try:
            args = request.args.to_dict()
            if "token" not in args:
                return PARAMS_MISS
            order_list = get_model_return_list(self.sorder.get_order_main_list_by_usid(get_str(args, "token")))

            data = import_status("SUCCESS_MESSAGE_GET_INFO", "OK")

            for order_main in order_list:
                self._get_order_abo_by_order_main(order_main)

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
            self._get_order_abo_by_order_main(order_main)
            data = import_status("SUCCESS_MESSAGE_GET_INFO", "OK")
            data["data"] = order_main
            return data
        except Exception as e:
            print(self.title.format("ERROR MSG"))
            print(e.message)
            print(self.title.format("ERROR MSG"))
            return SYSTEM_ERROR

    def make_order(self):
        args = request.args.to_dict()
        print(self.title.format("arge"))
        print(args)
        print(self.title.format("arge"))

        if "token" not in args:
            return PARAMS_MISS

        data = json.loads(request.data)
        print(self.title.format("data"))
        print(data)
        print(self.title.format("data"))

        if "LOid" not in data:
            print("LOid is not find")
            return PARAMS_MISS
        loid = get_str(data, "Loid")

        try:
            self.slocation.update_locations_by_loid(loid, {"LOisedit": 302})
            print(self.title.format("update location success"))
            import uuid
            omid = str(uuid.uuid4())
            order_main = {
                "OMid": omid,
                "LOid": loid,
                "OMabo": get_str(data, "OMmessage"),
                "USid": args.get("token"),
                "OMcointype": cvs.conversion_PBunit_reverse.get(get_str(data, "OMcointype"), 402),
                "COid": get_str(data, "COid"),
                "OMprice": float(get_str(data, "OMprice")),
                "OMtime": get_db_time_str(),
                "OMstatus": cvs.conversion_OMstatus_reverse.get(get_str(data, "OMstatus"))
            }
            self.sorder.add_model("OrderMain", **order_main)
        except Exception as e:
            print(self.title.format("system error"))
            print(e.message)
            print(self.title.format("system error"))
            return SYSTEM_ERROR

        order_part_list = data.get("orderitems")
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
        args = request.args.to_dict()
        print(self.title.format("arge"))
        print(args)
        print(self.title.format("arge"))

        if "token" not in args:
            return PARAMS_MISS

        data = json.loads(request.data)
        print(self.title.format("data"))
        print(data)
        print(self.title.format("data"))
        if "OMid" not in data or "OMstatus" not in data:
            return PARAMS_MISS
        order = {"OMstatus": cvs.conversion_OMstatus_reverse.get(get_str(data, "OMstatus"))}
        print(self.title.format("order"))
        print(order)
        print(self.title.format("order"))
        try:
            self.sorder.update_omstatus_by_omid(get_str(data, "OMid"), order)
            return import_status("SUCCESS_MESSAGE_UPDATE_ORDER", "OK")
        except Exception as e:
            print(self.title.format("update order error"))
            print(e.message)
            print(self.title.format("update order error"))
            return SYSTEM_ERROR

    def _get_product_into_order_abo(self, pbid):
        print(self.title.format("get PBid"))
        print(pbid)
        print(self.title.format("get PBid"))
        product = get_model_return_dict(self.sproduct.get_product_by_pbid(pbid))
        if not product:
            raise Exception("SYSTEM ERROR NO FIDN PBID")
        product.update(get_model_return_dict(self.sproduct.get_product_by_prid(product.get("PRid"))))
        product.update(self._get_brinfo(product.get("BRid")))
        product["PBunit"] = cvs.conversion_PBunit.get(product.get("PBunit", "其他币种"))
        product["PRbrand"] = cvs.conversion_PRbrand.get(product.get("PRbrand"), "其他")
        product["PRtype"] = cvs.conversion_PRtype.get(product.get("PRtype"))
        return product

    def _get_order_abo_by_order_main(self, order_main):
        order_part_list = get_model_return_list(self.sorder.get_order_part_list_by_omid(order_main.get("OMid")))
        for order_part in order_part_list:
            order_part.update(self._get_product_into_order_abo(order_part.get("PBid")))

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

    def _get_brinfo(self, brid):
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

    def get_order_price(self):
        args = request.args.to_dict()
        print(self.title.format("arge"))
        print(args)
        print(self.title.format("arge"))

        data = json.loads(request.data)
        print(self.title.format("data"))
        print(data)
        print(self.title.format("data"))
        products_list = data.get("productlist")
        OMcointype = "￥"
        order_list = []
        OMprice = 0
        try:
            for product in products_list:
                prnumber = product.get("PRnumber")
                product = self._get_product_into_order_abo(product.get("PBid"))
                if product.get("PBunit") != OMcointype:
                    #TODO 增加换算过程
                    pass
                OMprice += (product.get("PBprice") * prnumber)
                order_list.append(product)

            if "COid" in data and get_str(data, "COid"):
                coupon = self.scoupons.get_coupons_by_couid(get_str(data, "Coid"))
                OMprice = self.compute_om_price_by_coupons(coupon, OMprice)
                if not isinstance(OMprice, float):
                    return OMprice

            print(self.title.format("OMprice"))
            print(OMprice)
            print(self.title.format("OMprice"))

            data = import_status("SUCCESS_MESSAGE_GET_INFO", "OK")
            data["data"] = {"OMprice": OMprice, "OMcointype": OMcointype, "productlist": order_list}
            return data
        except Exception as e:
            print(self.title.format("get order error"))
            print(e.message)
            print(self.title.format("get order error"))

    def compute_om_price_by_coupons(self, coupon, omprice):
        time_now = get_db_time_str()
        if time_now > coupon.get("COend"):
            return import_status("ERROR_MESSAGE_COUPONS_TIMEEND", "SHARPGOODS_ERROR", "ERROR_TIMR")

        if time_now < coupon.get("COstart"):
            return import_status("ERROR_MESSAGE_COUPONS_TIMESTART", "SHARPGOODS_ERROR", "ERROR_TIMR")

        if 801 == coupon.get("COtype"):
            if omprice > coupon.get("COfilter"):
                omprice = omprice - coupon.get("COamount")

        elif 802 == coupon.get("COtype"):
            if omprice > coupon.get("COfilter"):
                omprice = omprice * coupon.get("COdiscount")
        elif 803 == coupon.get("COtype"):
            #TODO 增加商品类型的筛选判断逻辑
            pass
        elif 804 == coupon.get("COtype"):
            if coupon.get("COamount"):
                omprice = omprice - coupon.get("COamount")
            elif coupon.get("COdiscount"):
                omprice = omprice * coupon.get("COdiscount")
            else:
                raise Exception("DBERROR")
        elif 805 == coupon.get("COtype"):
            #TODO 增加用户类型的的筛选判断逻辑
            pass

        return omprice if omprice >= 0 else 0
