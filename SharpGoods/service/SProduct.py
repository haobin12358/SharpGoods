# *- coding:utf8 *-
# 兼容linux系统
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))  # 增加系统路径
# 引用项目类
from models import model
import DBSession
from common.TransformToList import trans_params


# 操作user表的相关方法
class SProduct():
    def __init__(self):
        """
        self.session 数据库连接会话
        self.status 判断数据库是否连接无异常
        """
        self.session, self.status = DBSession.get_session()

    def get_product_by_pbid(self, pbid):
        product = None
        try:
            product = self.session.query(model.ProductsBrands.PRid, model.ProductsBrands.BRid,
                                         model.ProductsBrands.PBunit, model.ProductsBrands.PBprice,
                                         model.ProductsBrands.PBsalesvolume, model.ProductsBrands.PBscore,
                                         model.ProductsBrands.PBimage)\
                .filter_by(PBstatus=201).filter_by(PBid=pbid).first()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return product

    def get_all_brand_by_brid_last(self, brid):
        brand_list = {}
        try:
            while brid == "0":
                brand = self.session.query(model.Brands.BRfromid, model.Brands.BRkey,
                                           model.Brands.BRvalue).filter_by(BRid=brid).first()
                brid, brkey, brvalue = brand.BRfromid, brand.BRkey, brand.BRvalue
                brand_list.keys().append(brkey)
                brand_list[brkey] = brvalue
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return brand_list

    def get_product_by_prid(self, prid):
        product = None
        try:
            product = self.session.query(model.Products.PRname, model.Products.PRbrand, model.Products.PRinfo,
                                         model.Products.PRvideo, model.Products.PRtype).filter_by(PRid=prid).first()
        except Exception as e:
            print e.message
            self.session.rollback()
            return False
        finally:
            self.session.close()
        return product
