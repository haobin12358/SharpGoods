# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask import request
import json
from config.response import SYSTEM_ERROR, PARAMS_MISS

class CProducts():
    def get_info_by_id(self):
        args = request.args.to_dict()
        if "PRid" not in args:
            return PARAMS_MISS
        return {
            "status": 200,
            "messages": "获取数据成功",
            "data":{
                "PRid": "123",
                "PRname":"测试商品名称",
                "PRimage":{
                    "https://h878.cn/imgs/timg.jpg",
                    "https://h878.cn/imgs/timg.jpg"
                },
                "PRvideo":"http://123.207.97.185:7444/imgs/product.mp4",
                "PRinfo": "这里是很长很长的商品介绍",
                "PRquality":{
                    "PRcolor": {
                        "红色", "白色", "紫色"
                    },
                    "PRbrand": "美妆类",
                    "PRno": {
                        "1.0", "2.0"
                    }
                },
                "PRtype":"自营"
            }
        }

    def get_all(self):
        return {
            "status": 200,
            "messages": "获取数据成功",
            "data": [
                {
                    "PRid":"123",
                    "PRname":"测试商品名称",
                    "PRimage":{
                        "https://h878.cn/imgs/timg.jpg",
                        "https://h878.cn/imgs/timg.jpg"
                    },
                    "PRvideo":"http://123.207.97.185:7444/imgs/product.mp4",
                    "PRinfo": "这里是很长很长的商品介绍",
                    "PRquality":{
                        "PRcolor": {
                            "红色", "白色", "紫色"
                        },
                        "PRbrand": "美妆类",
                        "PRno": {
                            "1.0", "2.0"
                        }
                    },
                    "PRtype":"自营"
                },
                {
                    "PRid": "124",
                    "PRname":"测试商品名称",
                    "PRimage":{
                        "https://h878.cn/imgs/timg.jpg",
                        "https://h878.cn/imgs/timg.jpg"
                    },
                    "PRvideo":"http://123.207.97.185:7444/imgs/product.mp4",
                    "PRinfo": "这里是很长很长的商品介绍",
                    "PRquality":{
                        "PRcolor": {
                            "红色", "白色", "紫色"
                        },
                        "PRbrand": "美妆类",
                        "PRno": {
                            "1.0", "2.0"
                        }
                    },
                    "PRtype":"自营"
                }
            ]
        }
