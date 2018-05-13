# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
from config.response import SYSTEM_ERROR, PARAMS_MISS

class CUsers():
    def register(self):
        data = request.data
        data = json.loads(data)
        if "UStelphone" not in data or "USpassword" not in data or "UScode" not in data:
            return PARAMS_MISS
        if "USinvate" in data:
            USinvate = data["USinvate"]
        return {
            "status": 200,
            "messages": "注册成功"
        }

    def login(self):
        args = request.args.to_dict()
        data = request.data
        data = json.loads(data)
        if "UStelphone" not in data or "USpassword" not in data:
            return PARAMS_MISS

        return {
            "status": 200,
            "messages": "登录成功",
            "data": {
                "token": "123"
            }
        }

    def update_info(self):
        args = request.args.to_dict()
        data = request.data
        data = json.loads(data)
        if "token" not in args or data in ["", "{}"]:
            return PARAMS_MISS
        return {
            "status": 200,
            "messages": "更新个人信息成功"
        }

    def update_pwd(self):
        args = request.args.to_dict()
        data = request.data
        data = json.loads(data)
        return {
            "status": 200,
            "messages": "更新密码成功"
        }

    def get_inforcode(self):
        data = request.data
        data = json.loads(data)
        if "UStelphone" not in data:
            return PARAMS_MISS
        return {
            "status": 200,
            "messages": "获取短信成功"
        }

    def all_info(self):
        args = request.args.to_dict()
        if "token" not in args:
            return PARAMS_MISS
        return {
            "status": 200,
            "messages": "获取信息成功",
            "data":{
                "UStelphone": "17706441101",
                "UScoin": 100.23,
                "USsex": "男",
                "USname": "测试用户",
                "USinvate": "db2312"
            }
        }