# *- coding:utf8 *-
from flask import Flask
import flask_restful
import threading
from apis.AUsers import AUsers
from apis.AProducts import AProducts
from apis.ACarts import ACarts
from apis.AReviews import AReviews
from apis.AOrders import AOrders
from apis.ALocations import ALocations
from apis.ACoupons import ACoupons
from apis.AOther import AOther
from celery.GetOrdermain import GetOrdermain

sg = Flask(__name__)
api = flask_restful.Api(sg)

api.add_resource(AUsers, "/sharp/goods/users/<string:users>")
api.add_resource(AProducts, "/sharp/goods/product/<string:product>")
api.add_resource(ACarts, "/sharp/goods/cart/<string:cart>")
api.add_resource(AReviews, "/sharp/goods/review/<string:review>")
api.add_resource(AOrders, "/sharp/goods/orders/<string:orders>")
api.add_resource(ALocations, "/sharp/goods/locations/<string:locations>")
api.add_resource(ACoupons, "/sharp/goods/card/<string:card>")
api.add_resource(AOther, "/sharp/goods/other/<string:other>")
# '''
if __name__ == '__main__':
    th = threading.Thread(target=GetOrdermain().timer())
    th.start()
    sg.run('0.0.0.0', 443, debug=False, ssl_context=(
        "/etc/nginx/cert/1525609592348.pem"
    ))
    
'''
if __name__ == '__main__':
    th = threading.Thread(target=GetOrdermain().timer)
    th.start()
    sg.run('0.0.0.0', 7444, debug=False)
'''