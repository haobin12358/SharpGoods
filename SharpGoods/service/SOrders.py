# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
import uuid
import DBSession
from models import model
from common.TransformToList import trans_params

class SOrders():
    def __init__(self):
        try:
            self.session = DBSession.db_session()
        except Exception as e:
            print(e.message)

    def get_uid_by_omid(self, omid):
        uid = None
        try:
            uid = self.session.query(model.OrderMain.USid).filter_by(OMid=omid).scalar()
        except Exception as e:
            print e.message
            self.session.rollback()
        finally:
            self.session.close()
        return uid

    def get_omstatus_by_omid(self, omid):
        uid = None
        try:
            uid = self.session.query(model.OrderMain.OMstatus).filter_by(OMid=omid).scalar()
        except Exception as e:
            print e.message
            self.session.rollback()
        finally:
            self.session.close()
        return uid

    def update_omstatus_by_omid(self, omid, order_main):
        try:
            self.session.query(model.OrderMain).filter_by(OMid=omid).update(order_main)
            self.session.commit()
            self.session.close()
            return True
        except Exception as e:
            self.session.rollback()
            self.session.close()
            print e.message
            return False