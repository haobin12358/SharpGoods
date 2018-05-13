# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
from config.response import SYSTEM_ERROR, PARAMS_MISS

class CLocations():
    def get_all_location(self):
        args = request.args.to_dict()
        if "token" not in args:
            return PARAMS_MISS
        return {
            "status": 200,
            "messages": "获取信息成功",
            "data":[
                {
                    "LOid":"123456",
                    "LOno":"310000",
                    "LOname":"收件人的名字",
                    "LOtelphone":"+8617706441101",
                    "LOdetail": "详细的收货地址",
                    "LOisedit": 301
                },
                {
                    "LOid": "123457",
                    "LOno": "310000",
                    "LOname": "收件人的名字",
                    "LOtelphone": "+8617706441101",
                    "LOdetail": "详细的收货地址",
                    "LOisedit": 302
                }
            ]
        }

    def new_location(self):
        args = request.args.to_dict()
        data = request.data
        data = json.loads(data)
        if "token" not in args or "LOno" not in data or "LOname" not in data or "LOtelphone" not in data or "LOdetail" not in data:
            return PARAMS_MISS
        return {
            "status": 200,
            "messages": "创建收货地址成功"
        }

    def update_location(self):
        args = request.args.to_dict()
        data = request.data
        data = json.loads(data)
        if "token" not in args or "LOid" not in data:
            return PARAMS_MISS
        return {
            "status": 200,
            "messages": "更新收货地址成功"
        }