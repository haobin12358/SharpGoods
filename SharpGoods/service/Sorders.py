# *- coding:utf8 *-
from SBase import SBase, close_session
from models.model import OrderMain, Orderpart

class Sorders(SBase):
    def __init__(self):
        super(Sorders, self).__init__()

    @close_session
    def get_order_part_list_by_omid(self, omid):
        return self.session.query(
            Orderpart.OPid, Orderpart.PBid, Orderpart.PRnumber).filter(Orderpart.OMid == omid).all()

    @close_session
    def get_order_main_list_by_usid(self, usid):
        return self.session.query(
            OrderMain.OMid, OrderMain.LOid, OrderMain.COid,
            OrderMain.OMabo, OrderMain.OMcointype, OrderMain.OMstatus,
            OrderMain.OMtime, OrderMain.OMprice
        ).all()