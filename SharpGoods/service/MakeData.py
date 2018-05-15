# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))  # 增加系统路径
from common.TransformToList import add_model
import uuid

class MakeData():
    def __init__(self):
        from service.SUsers import SUsers
        self.users = SUsers()

    def setUid(self):
        uid = str(uuid.uuid4())
        return uid

    def add_user(self, uid):
        try:
            add_model("Users",
                **{
                    "USid":uid,
                    "UStelphone":"11111111111",
                    "USpassword":"123",
                    "USname":"测试账号",
                    "USsex":101,
                    "UScoin":100.1,
                    "USinvate":"ETECH007"
                })
        except Exception as e:
            print e.message

    def set_brid(self):
        brid_list = []
        while len(brid_list) < 9:
            brid_list.append(str(uuid.uuid4()))
        return brid_list

    def add_brand(self, brid):
        try:
            add_model("Brands",
                      **{
                          "BRid":brid[0],
                          "BRfromid":"0",
                          "BRkey":"BRno",
                          "BRvalue":"1.0"
                      })
            add_model("Brands",
                      **{
                          "BRid": brid[1],
                          "BRfromid": "0",
                          "BRkey": "BRno",
                          "BRvalue": "2.0"
                      })
            add_model("Brands",
                      **{
                          "BRid": brid[2],
                          "BRfromid": brid[0],
                          "BRkey": "BRcolor",
                          "BRvalue": "红色"
                      })
            add_model("Brands",
                      **{
                          "BRid": brid[3],
                          "BRfromid": brid[0],
                          "BRkey": "BRcolor",
                          "BRvalue": "白色"
                      })
            add_model("Brands",
                      **{
                          "BRid": brid[4],
                          "BRfromid": brid[0],
                          "BRkey": "BRcolor",
                          "BRvalue": "灰色"
                      })
            add_model("Brands",
                      **{
                          "BRid": brid[5],
                          "BRfromid": brid[0],
                          "BRkey": "BRcolor",
                          "BRvalue": "紫色"
                      })
            add_model("Brands",
                      **{
                          "BRid": brid[6],
                          "BRfromid": brid[1],
                          "BRkey": "BRcolor",
                          "BRvalue": "红色"
                      })
            add_model("Brands",
                      **{
                          "BRid": brid[7],
                          "BRfromid": brid[1],
                          "BRkey": "BRcolor",
                          "BRvalue": "金色"
                      })
            add_model("Brands",
                      **{
                          "BRid": brid[8],
                          "BRfromid": brid[1],
                          "BRkey": "BRcolor",
                          "BRvalue": "蓝色"
                      })
        except Exception as e:
            print e.message

    def set_pid(self):
        pid_list = []
        pid_list.append(str(uuid.uuid4()))
        return pid_list

    def add_product(self, pid):
        try:
            add_model("Products",
                      **{
                          "PRid":pid[0],
                          "PRname":"美妆镜",
                          "PRvideo":"http://123.207.97.185:7444/imgs/product.mp4",
                          "PRinfo":"测试数据",
                          "PRtype":501,
                          "PRbrand":601
                      })
        except Exception as e:
            print e.message

    def set_pbid(self):
        pbid_list = []
        while len(pbid_list) < 7:
            pbid_list.append(str(uuid.uuid4()))
        return pbid_list

    def add_productbrand(self, pbid, pid, brid):
        try:
            add_model("ProductsBrands",
                      **{
                          "PBid": pbid[0],
                          "PRid": pid[0],
                          "BRid": brid[2],
                          "PBprice": 199.99,
                          "PBunit": 402,
                          "PBstatus": 201,
                          "PBsalesvolume": 105,
                          "PBscore": 4.9,
                          "PBimage":"https://h878.cn/imgs/timg.jpg"
                      })
            add_model("ProductsBrands",
                      **{
                          "PBid": pbid[1],
                          "PRid": pid[0],
                          "BRid": brid[3],
                          "PBprice": 199.99,
                          "PBunit": 402,
                          "PBstatus": 201,
                          "PBsalesvolume": 105,
                          "PBscore": 4.9,
                          "PBimage": "https://h878.cn/imgs/timg.jpg"
                      })
            add_model("ProductsBrands",
                      **{
                          "PBid": pbid[2],
                          "PRid": pid[0],
                          "BRid": brid[4],
                          "PBprice": 199.99,
                          "PBunit": 402,
                          "PBstatus": 201,
                          "PBsalesvolume": 105,
                          "PBscore": 4.9,
                          "PBimage": "https://h878.cn/imgs/timg.jpg"
                      })
            add_model("ProductsBrands",
                      **{
                          "PBid": pbid[3],
                          "PRid": pid[0],
                          "BRid": brid[5],
                          "PBprice": 199.99,
                          "PBunit": 402,
                          "PBstatus": 201,
                          "PBsalesvolume": 105,
                          "PBscore": 4.9,
                          "PBimage": "https://h878.cn/imgs/timg.jpg"
                      })
            add_model("ProductsBrands",
                      **{
                          "PBid": pbid[4],
                          "PRid": pid[0],
                          "BRid": brid[6],
                          "PBprice": 199.99,
                          "PBunit": 402,
                          "PBstatus": 201,
                          "PBsalesvolume": 105,
                          "PBscore": 4.9,
                          "PBimage":"https://h878.cn/imgs/timg.jpg"
                      })
            add_model("ProductsBrands",
                      **{
                          "PBid": pbid[5],
                          "PRid": pid[0],
                          "BRid": brid[7],
                          "PBprice": 199.99,
                          "PBunit": 402,
                          "PBstatus": 201,
                          "PBsalesvolume": 105,
                          "PBscore": 4.9,
                          "PBimage": "https://h878.cn/imgs/timg.jpg"
                      })
            add_model("ProductsBrands",
                      **{
                          "PBid": pbid[6],
                          "PRid": pid[0],
                          "BRid": brid[8],
                          "PBprice": 199.99,
                          "PBunit": 402,
                          "PBstatus": 201,
                          "PBsalesvolume": 105,
                          "PBscore": 4.9,
                          "PBimage": "https://h878.cn/imgs/timg.jpg"
                      })
        except Exception as e:
            print e.message

    def add_cart(self, uid, pbid):
        try:
            add_model("Cart",
                      **{
                          "CAid":str(uuid.uuid4()),
                          "USid":uid,
                          "PBid":pbid[2],
                          "CAnumber":2,
                          "CAstatus":1
                      })
            add_model("Cart",
                      **{
                          "CAid": str(uuid.uuid4()),
                          "USid": uid,
                          "PBid": pbid[3],
                          "CAnumber": 5,
                          "CAstatus": 1
                      })
            add_model("Cart",
                      **{
                          "CAid": str(uuid.uuid4()),
                          "USid": uid,
                          "PBid": pbid[0],
                          "CAnumber": 1,
                          "CAstatus": 2
                      })
        except Exception as e:
            print e.message

if __name__ == "__main__":
    makedata = MakeData()
    uid = makedata.setUid()
    pbid = makedata.set_pbid()
    pid = makedata.set_pid()
    brid = makedata.set_brid()

    makedata.add_user(uid)
    makedata.add_product(pid)
    makedata.add_cart(uid, pbid)
    makedata.add_brand(brid)
    makedata.add_productbrand(pbid,pid,brid)