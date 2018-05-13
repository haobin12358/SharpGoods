# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from control.CProducts import CProducts

class AProducts(Resource):
    def __init__(self):
        self.control_product = CProducts()

    def post(self, product):
        print("=======================api===================")
        print("接口名称是{0}，接口方法是post".format(product))
        print("=======================api===================")

        apis = {

        }

        if product not in apis:
            from config.response import APIS_WRONG
            return APIS_WRONG
        return eval(apis[product])

    def get(self, product):
        print("=======================api===================")
        print("接口名称是{0}，接口方法是get".format(product))
        print("=======================api===================")

        apis = {
            "get_info_by_id": "self.control_product.get_info_by_id()",
            "get_all": "self.control_product.get_all()"
        }
        if product not in apis:
            from config.response import APIS_WRONG
            return APIS_WRONG
        return eval(apis[product])