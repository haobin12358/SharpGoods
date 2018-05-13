# *- coding:utf8 *-
from flask import Flask
import flask_restful
from apis.AUsers import AUsers
from apis.AProducts import AProducts
#from apis.ACarts import ACarts
#from apis.AReviews import AReviews
from apis.AOrders import AOrders
from apis.ALocations import ALocations
#from apis.ACoupons import ACoupons

sg = Flask(__name__)
api = flask_restful.Api(sg)

api.add_resource(AUsers, "/sharp/goods/users/<string:users>")
api.add_resource(AProducts, "/sharp/goods/product/<string:product>")
#api.add_resource(ACarts, "/love/breakfast/salelist/<string:cart>")
#api.add_resource(AReviews, "/love/breakfast/review/<string:review>")
api.add_resource(AOrders, "/sharp/goods/orders/<string:orders>")
api.add_resource(ALocations, "/sharp/goods/locations/<string:locations>")
#api.add_resource(ACoupons, "/love/breakfast/cardpkg/<string:card>")

'''
if __name__ == '__main__':
    bk.run('0.0.0.0', 443, debug=True, ssl_context=(
        "/etc/nginx/cert/1525609592348.pem"
    ))
'''
if __name__ == '__main__':
    sg.run('0.0.0.0', 7444, debug=True)