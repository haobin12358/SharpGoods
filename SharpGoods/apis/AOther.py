# *- coding:utf8 *-
# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource,request
from config.response import PARAMS_MISS

class AOther(Resource):
    def __init__(self):
        pass

    def get(self, other):
        if other == "disclaimer":
            return """欢迎您使用网上订餐服务。请您务必先仔细阅读本用户协议（包括隐私权条款及法律条款），我们将按以下的方式和条件为您提供我们的服务。如果您使用我们的服务，即表示您完全同意并接受本用户协议。 
              
              一、我们的服务和义务
              
              1. 权利声明
              
              本网站出现的商标、服务标志、设计及本网站中述及的任何其他知识产权，均属公司所有、或已取得所有人的正式授权，在未取得公司的正式书面授权之前，任何人不得擅自使用，包括但不限于复制、复印、修改、出版、公布、传送、分发本网站上所载的文本、图象、影音、镜像等内容，违者将被依法追究民事乃至刑事责任。 
              
              2. 责任限制
              
              本程序将努力提供准确和及时的信息和内容，但这些信息和内容仅限于其现有状况，对其准确性和及时性，本网站不给予任何明示或默示的保证。本网站不承担因您进入或使用本网站而导致的任何直接的、间接的、意外的、因果性的损害责任。请小心使用您的软件和设备。 
              
              3．信息提交
              
              您传送至本网站的任何其他通讯或材料，包括但不限于意见、客户反馈、喜好、建议、支持、请求、问题等内容，将被当作非保密资料和非专有资料处理；而当您将这些资料传送至本网站并被接收时，即被视为您同意这些资料用作本网站的调查、统计或作内部整体无偿使用。 我们将有权将提交内容用于任何商业的或其他目的而无需对您或其他提交人予以补偿。您承认，您对所提交资料负责，并且对信息承担全部责任，包括其合法性、可靠性、适当性、独创性及著作权。
              
              4．适用法律
              
                  本使用条款及隐私权政策受中国的法律管辖。如果本网站条款或隐私权政策的任何部分失效，将不影响其余条款的有效性和可执行性。 """
        if other == "payconfig":
            args = request.args.to_dict()
            if "OMid" not in args:
                return PARAMS_MISS
            OMid = args["OMid"]
            response = {}
            response["appId"] = "wx284751ea4c889568"
            import time
            response["timeStamp"] = int(time.time())
            import uuid
            response["nonceStr"] = str(uuid.uuid1()).replace("-", "")
            response["package"] = "prepay_id=" + OMid.replace("-", "")
            response["signType"] = "MD5"
            key_sign = "appId={0}&nonceStr={1}&package={2}&signType={3}&timeStamp={4}&key={5}".format(
                response["appId"], response["nonceStr"], response["package"], response["signType"], response["timeStamp"], "hangzhouzhenlangjinchukou"
            )
            print key_sign
            print type(key_sign)
            import hashlib
            s = hashlib.md5()
            print s
            s.update(key_sign)
            print s
            response["paySign"] = s.hexdigest().upper()
            return response
