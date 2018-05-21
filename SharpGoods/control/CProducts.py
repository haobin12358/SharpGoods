# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
from config.response import SYSTEM_ERROR, PARAMS_MISS
from common.import_status import import_status

class CProducts():
    def __init__(self):
        from service.SProduct import SProduct
        self.sproduct = SProduct()

    def get_info_by_id(self):
        args = request.args.to_dict()
        print "=================args================="
        print args
        print "=================args================="
        if "PRid" not in args:
            return PARAMS_MISS
        PRid = args["PRid"]
        product = self.sproduct.get_product_by_prid(PRid)
        print "=================product================="
        print product
        print "=================product================="
        if not product:
            return SYSTEM_ERROR
        product_price = [9999999,-1]
        product_volue = 0
        product_price_list = self.sproduct.get_pbprice_by_prid(PRid)
        print "=================product_price_list================="
        print product_price_list
        print "=================product_price_list================="
        if not product_price_list:
            return SYSTEM_ERROR
        for row in product_price_list:
            if row < product_price[0]:
                product_price[0] = row
            if row > product_price[1]:
                product_price[1] = row
        product_volue_list = self.sproduct.get_pbvolume_by_prid(PRid)
        print "=================product_volue_list================="
        print product_volue_list
        print "=================product_volue_list================="
        if not product_volue_list:
            return SYSTEM_ERROR
        for row in product_volue_list:
            product_volue = product_volue + row
        product_info = {}
        product_info["PRid"] = PRid
        product_info["PRprice"] = str(product_price[0]) +  "-" + str(product_price[1])
        product_info["PRsalevolume"] = product_volue
        product_info["PRname"] = product.PRname
        product_info["PRvideo"] = product.PRvideo
        product_info["PRinfo"] = product.PRinfo
        product_info["PRimage"] = product.PRimage
        product_info["PRaboimage"] = product.PRaboimage
        PRbrand = product.PRbrand
        PRtype = product.PRtype
        if PRbrand == 601:
            product_info["PRbrand"] = "美妆类"
        elif PRbrand == 602:
            product_info["PRbrand"] = "3C类"
        else:
            product_info["PRbrand"] = "其他"
        if PRtype == 501:
            product_info["PRtype"] = "自营"
        elif PRtype == 502:
            product_info["PRtype"] = "非自营"
        else:
            product_info["PRtype"] = "未知商品"
        PBimage = self.sproduct.get_pbimg_by_prid(PRid)
        print "=================PBimage================="
        print PBimage
        print "=================PBimage================="
        product_info["PBimage"] = []
        for img in PBimage:
            product_info["PBimage"].append(img)
        product_info["PRquality"] = {}
        BRid = self.sproduct.get_brid_by_prid(PRid)
        print "=================BRid================="
        print BRid
        print "=================BRid================="
        for brid in BRid:
            while brid != "0":
                brand = self.sproduct.get_brand_by_brid(brid)
                print "=================brand================="
                print brand
                print "=================brand================="
                brid, BRkey, BRvalue = brand.BRfromid, brand.BRkey, brand.BRvalue
                if BRkey in product_info["PRquality"].keys():
                    if BRvalue not in product_info["PRquality"][BRkey]["choice"]:
                        product_info["PRquality"][BRkey]["choice"].append(BRvalue)
                else:
                    product_info["PRquality"].keys().append(BRkey)
                    product_info["PRquality"][BRkey] = {}
                    product_info["PRquality"][BRkey]["name"] = self.choose_key(BRkey)
                    product_info["PRquality"][BRkey]["choice"] = []
                    product_info["PRquality"][BRkey]["choice"].append(BRvalue)
        response_of_product = import_status("SUCCESS_MESSAGE_GET_PRODUCT", "OK")
        response_of_product["data"] = product_info
        return response_of_product

    def get_all(self):
        PRid_list = self.sproduct.get_all_prid()
        print "=================PRid_list================="
        print PRid_list
        print "=================PRid_list================="
        product_infos = []
        for PRid in PRid_list:
            product = self.sproduct.get_product_by_prid(PRid)
            print "=================product================="
            print product
            print "=================product================="
            if not product:
                return SYSTEM_ERROR
            product_price = [9999999, -1]
            product_volue = 0
            product_price_list = self.sproduct.get_pbprice_by_prid(PRid)
            print "=================product_price_list================="
            print product_price_list
            print "=================product_price_list================="
            if not product_price_list:
                return SYSTEM_ERROR
            for row in product_price_list:
                if row < product_price[0]:
                    product_price[0] = row
                if row > product_price[1]:
                    product_price[1] = row
            product_volue_list = self.sproduct.get_pbvolume_by_prid(PRid)
            print "=================product_volue_list================="
            print product_volue_list
            print "=================product_volue_list================="
            if not product_volue_list:
                return SYSTEM_ERROR
            for row in product_volue_list:
                product_volue = product_volue + row
            product_info = {}
            product_info["PRid"] = PRid
            if product_price[0] == product_price[1]:
                product_info["PRprice"] = product_price[0]
            else:
                product_info["PRprice"] = str(product_price[0]) + "-" + str(product_price[1])
            product_info["PRsalevolume"] = product_volue
            product_info["PRname"] = product.PRname
            product_info["PRvideo"] = product.PRvideo
            product_info["PRinfo"] = product.PRinfo
            product_info["PRimage"] = product.PRimage
            product_info["PRaboimage"] = product.PRaboimage
            PRbrand = product.PRbrand
            PRtype = product.PRtype
            if PRbrand == 601:
                product_info["PRbrand"] = "美妆类"
            elif PRbrand == 602:
                product_info["PRbrand"] = "3C类"
            else:
                product_info["PRbrand"] = "其他"
            if PRtype == 501:
                product_info["PRtype"] = "自营"
            elif PRtype == 502:
                product_info["PRtype"] = "非自营"
            else:
                product_info["PRtype"] = "未知商品"
            PBimage = self.sproduct.get_pbimg_by_prid(PRid)
            print "=================PBimage================="
            print PBimage
            print "=================PBimage================="
            product_info["PBimage"] = []
            for img in PBimage:
                product_info["PBimage"].append(img)
            product_info["PRquality"] = {}
            BRid = self.sproduct.get_brid_by_prid(PRid)
            print "=================BRid================="
            print BRid
            print "=================BRid================="
            for brid in BRid:
                while brid != "0":
                    brand = self.sproduct.get_brand_by_brid(brid)
                    print "=================brand================="
                    print brand
                    print "=================brand================="
                    brid, BRkey, BRvalue = brand.BRfromid, brand.BRkey, brand.BRvalue
                    if BRkey in product_info["PRquality"].keys():
                        if BRvalue not in product_info["PRquality"][BRkey]["choice"]:
                            product_info["PRquality"][BRkey]["choice"].append(BRvalue)
                    else:
                        product_info["PRquality"].keys().append(BRkey)
                        product_info["PRquality"][BRkey] = {}
                        product_info["PRquality"][BRkey]["name"] = self.choose_key(BRkey)
                        product_info["PRquality"][BRkey]["choice"] = []
                        product_info["PRquality"][BRkey]["choice"].append(BRvalue)
            product_infos.append(product_info)
        response_of_product = import_status("SUCCESS_MESSAGE_GET_INFO", "OK")
        response_of_product["data"] = product_infos
        return response_of_product

    def get_control_brand_by_prid(self):
        args = request.args.to_dict()
        print "=================args================="
        print args
        print "=================args================="
        data = request.data
        data = json.loads(data)
        print "=================data================="
        print data
        print "=================data================="
        if "token" not in args or "PRid" not in args:
            return PARAMS_MISS
        if data == {}:
            return PARAMS_MISS
        BRid = self.sproduct.get_brid_by_prid(args["PRid"])
        print "=================BRid================="
        print BRid
        print "=================BRid================="
        if not BRid:
            return SYSTEM_ERROR
        key_list = []
        brid = BRid[0]
        while brid != "0":
            Brand = self.sproduct.get_brand_by_brid(brid)
            brid, BRkey, BRvalue = Brand.BRfromid, Brand.BRkey, Brand.BRvalue
            key_list.append(BRkey)
        print "=================key_list================="
        print key_list
        print "=================key_list================="
        # 根据高层的key去找低层的所有id
        if key_list[0] in data.keys():
            BRid_list = self.sproduct.get_brid_by_key_value(key_list[0], data[key_list[0]])
        else:
            BRid_list = self.sproduct.get_brid_by_prid(args["PRid"])
        print "=================BRid_list================="
        print BRid_list
        print "=================BRid_list================="
        i = len(BRid_list)
        while i > 0:
            raw = BRid_list[i - 1]
            row = BRid_list[i - 1]
            print "=================raw================="
            print raw
            print "=================raw================="
            while row != "0":
                brand = self.sproduct.get_brand_by_brid(row)
                print "=================brand================="
                print brand
                print "=================brand================="
                row, BRkey, BRvalue = brand.BRfromid, brand.BRkey, brand.BRvalue
                if BRkey in data.keys() and data[BRkey] != BRvalue:
                    BRid_list.remove(raw)
                    print "=================BRid_list_remove================="
                    print BRid_list
                    print "=================BRid_list_remove================="
            i = i - 1
        print "=================BRid_list================="
        print BRid_list
        print "=================BRid_list================="
        data = {}
        for key in key_list:
            data.keys().append(key)
            data[key] = []
            for BRid in BRid_list:
                brand = self.sproduct.get_brand_by_brid(BRid)
                BRkey, BRvalue = brand.BRkey, brand.BRvalue
                if BRkey == key and BRvalue not in data[key]:
                    data[key].append(BRvalue)
                else:
                    while BRid != "0":
                        brand_parent = self.sproduct.get_brand_by_brid(BRid)
                        BRid, BRkey, BRvalue = brand_parent.BRfromid, brand_parent.BRkey, brand_parent.BRvalue
                        if BRvalue not in data[key] and BRkey == key:
                            data[key].append(BRvalue)

        response = import_status("SUCCESS_MESSAGE_GET_INFO", "OK")
        response["data"] = data
        return response

    def get_pbid_by_all_brand(self):
        args = request.args.to_dict()
        print "=================args================="
        print args
        print "=================args================="
        data = request.data
        data = json.loads(data)
        print "=================data================="
        print data
        print "=================data================="
        if "token" not in args or "PRid" not in args:
            return PARAMS_MISS
        if data == {}:
            return PARAMS_MISS
        BRid = self.sproduct.get_brid_by_prid(args["PRid"])
        print "=================BRid================="
        print BRid
        print "=================BRid================="
        if not BRid:
            return SYSTEM_ERROR
        key_list = []
        brid = BRid[0]
        while brid != "0":
            Brand = self.sproduct.get_brand_by_brid(brid)
            brid, BRkey, BRvalue = Brand.BRfromid, Brand.BRkey, Brand.BRvalue
            key_list.append(BRkey)
        print "=================key_list================="
        print key_list
        print "=================key_list================="
        BRid_list = self.sproduct.get_brid_by_key_value(key_list[0], data[key_list[0]])
        print "=================BRid_list================="
        print BRid_list
        print "=================BRid_list================="
        i = len(BRid_list)
        while i > 0:
            row = BRid_list[i - 1]
            raw = row
            while row != "0":
                brand = self.sproduct.get_brand_by_brid(row)
                print "=================brand================="
                print brand
                print "=================brand================="
                row, BRkey, BRvalue = brand.BRfromid, brand.BRkey, brand.BRvalue
                if data[BRkey] != BRvalue:
                    BRid_list.remove(raw)
            i = i - 1

        print "=================BRid_list================="
        print BRid_list
        print "=================BRid_list================="
        if len(BRid_list) != 1:
            return SYSTEM_ERROR
        BRid = BRid_list[0]
        pball = self.sproduct.get_pball_by_brid(BRid)
        print "=================pball================="
        print pball
        print "=================pball================="
        data = {}
        data["PBid"] = pball.PBid
        data["PBimage"] = pball.PBimage
        PBunit = pball.PBunit
        if PBunit == 401:
            data["PBunit"] = "$"
        elif PBunit == 402:
            data["PBunit"] = "￥"
        elif PBunit == 403:
            data["PBunit"] = "欧元"
        elif PBunit == 404:
            data["PBunit"] = "英镑"
        else:
            data["PBunit"] = "其他币种"
        data["PBprice"] = pball.PBprice
        data["PBsalesvolume"] = pball.PBsalesvolume
        data["PBscore"] = pball.PBscore

        response = import_status("SUCCESS_MESSAGE_GET_INFO", "OK")
        response["data"] = data
        return response

    def choose_key(self, BRkey):
        if BRkey == "BRno":
            return "版本选择"
        elif BRkey == "BRcolor":
            return "颜色选择"
        else:
            return "未知类目"