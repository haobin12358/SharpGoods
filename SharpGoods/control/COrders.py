# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
from config.response import SYSTEM_ERROR, PARAMS_MISS

class COrders():
    def get_order_list(self):
        return {
            "status":200,
            "messages":"获取订单列表成功",
            "data":[
                {
                    "OMid":"123",
                    "OMtime":"2018-05-13 10:38:22",
                    "OMstatus":"已支付/未支付/配送中/已完成/已评价",
                    "ADname":"收件人姓名",
                    "OMcointype":"$",
                    "OMtotal":4.35
                },
                {
                    "OMid": "124",
                    "OMtime": "2018-05-13 10:38:22",
                    "OMstatus": "已支付/未支付/配送中/已完成/已评价",
                    "ADname": "收件人姓名",
                    "OMcointype": "$",
                    "OMtotal": 4.35
                }
            ]
        }

    def get_order_abo(self):
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