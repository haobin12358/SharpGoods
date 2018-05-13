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
                "PRname":"测试商品名称",
                "PRpicture":"https://h878.cn/imgs/timg.jpg",
                "PRvideo":"http://123.207.97.185:7444/imgs/product.mp4",
                "PRprice": 192.35,
                "PRunit": "$",
                "PRstatus": "在售",
                "PRinfo": "这里是很长很长的商品介绍",
                "PRsalesvolume": 398,
                "PRscore": 2.6,
                "PRno":"1.0",
                "PRcolor":{
                    "红色","白色","紫色"
                },
                "PRtype":"自营",
                "PRbrand":"美妆类"
            }
        }

    def get_all(self):
        return {
            "status": 200,
            "messages": "获取数据成功",
            "data": [
                {
                    "PRid": "123456",
                    "PRname": "测试商品名称",
                    "PRpicture": "https://h878.cn/imgs/timg.jpg",
                    "PRvideo": "http://123.207.97.185:7444/imgs/product.mp4",
                    "PRprice": 192.35,
                    "PRunit": "$",
                    "PRstatus": "在售",
                    "PRinfo": "这里是很长很长的商品介绍",
                    "PRsalesvolume": 398,
                    "PRscore": 2.6,
                    "PRno":"1.0",
                    "PRcolor":"红色",
                    "PRtype":"自营",
                    "PRbrand":"美妆类"
                },
                {
                    "PRid": "123457",
                    "PRname": "测试商品名称2",
                    "PRpicture": "https://h878.cn/imgs/timg.jpg",
                    "PRvideo": "http://123.207.97.185:7444/imgs/product.mp4",
                    "PRprice": 125.35,
                    "PRunit": "￥",
                    "PRstatus": "已下架",
                    "PRinfo": "这里是很长很长的商品介绍",
                    "PRsalesvolume": 100,
                    "PRscore": 0.7,
                    "PRno":"1.0",
                    "PRcolor":"白色",
                    "PRtype":"非自营",
                    "PRbrand":"美妆类"
                }
            ]
        }
