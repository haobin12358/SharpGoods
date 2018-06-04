# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource
from control.CCarts import CCarts

class ACarts(Resource):
    def __init__(self):
        self.ccarts = CCarts()

    def post(self, cart):
        print("=======================api===================")
        print("接口名称是{0}，接口方法是post".format(cart))
        print("=======================api===================")
        apis = {
            "delete_product": "self.ccarts.del_cart()",
            "update": "self.ccarts.add_or_update_cart()"
        }

        if cart not in apis:
            from config.response import APIS_WRONG
            return APIS_WRONG
        return eval(apis[cart])

    def get(self, cart):
        print("=======================api===================")
        print("接口名称是{0}，接口方法是get".format(cart))
        print("=======================api===================")
        apis = {
            "get_all": "self.ccarts.get_carts_by_uid()"
        }

        if cart not in apis:
            from config.response import APIS_WRONG
            return APIS_WRONG
        return eval(apis[cart])