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
        if other == "getdata":
            data = request.data
            print(data)
            import json
            data = json.loads(data)
            if "return_code" not in data:
                return PARAMS_MISS

            return {
                "return_code": "SUCCESS",
                "return_msg": "OK"
            }

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
            print("=======================api===================")
            print("接口名称是{0}，接口方法是get".format("payconfig"))
            print("=======================api===================")
            args = request.args.to_dict()
            if "code" not in args or "OMid" not in args:
                return PARAMS_MISS
            print("=======================args===================")
            print(args)
            print("=======================args===================")
            code = args["code"]
            APP_ID = "wx284751ea4c889568"
            APP_SECRET_KEY = "051c81977efa8175e43686565265bb4f"
            request_url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type={3}" \
                .format(APP_ID, APP_SECRET_KEY, code, "authorization_code")
            strResult = None
            try:
                import urllib2
                req = urllib2.Request(request_url)
                response = urllib2.urlopen(req)
                strResult = response.read()
                print strResult
            except Exception as e:
                print e.message
            if "openid" not in strResult or "session_key" not in strResult:
                return
            import json
            strResult = json.loads(strResult)
            print("=======================strResult===================")
            print(strResult)
            print("=======================strResult===================")
            openid = strResult["openid"]
            session_key = strResult["session_key"]
            OMid = args["OMid"]
            response = {}
            response["appId"] = "wx284751ea4c889568"
            response["openid"] = openid
            response["session_key"] = session_key
            import time
            response["timeStamp"] = int(time.time())
            import uuid
            response["nonceStr"] = str(uuid.uuid1()).replace("-", "")
            body = {}
            response = {}
            body["appId"] = "wx284751ea4c889568"
            body["mch_id"] = "1504082901"
            body["device_info"] = "WEB"
            body["nonce_str"] = str(uuid.uuid1()).replace("-", "")
            key_sign = "appid={0}&body={1}&device_info={2}&mch_id={3}&nonce_str={4}".format(
                body["appId"], "test", body["device_info"], body["mch_id"], body["nonce_str"]
            )
            key_sign = key_sign + "&key={0}".format("hangzhouzhenlangjinchukou")
            import hashlib
            s = hashlib.md5()
            s.update(key_sign)
            body["sign"] = s.hexdigest().upper()
            body["sign_type"] = "MD5"
            body["body"] = "美妆类-美妆镜"
            body["out_trade_no"] = OMid
            body["fee_type"] = "CNY"
            body["total_fee"] = 1
            body["spbill_create_ip"] = "120.79.182.43"
            import datetime
            body["time_start"] = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            body["time_expire"] = (datetime.datetime.now() + datetime.timedelta(hours=2)).strftime("%Y%m%d%H%M%S")
            body["notify_url"] = "https://h878.cn/sharp/goods/other/getdata"
            body["trade_type"] = "JSAPI"
            body["openid"] = openid
            strResult = None
            try:
                import urllib2
                url = "https://api.mch.weixin.qq.com/pay/unifiedorder"
                headers = {'Content-Type': 'application/json'}
                req = urllib2.Request(url, headers=headers, data=body)
                response = urllib2.urlopen(req)
                strResult = response.read()
                print strResult
            except Exception as e:
                print e.message
            if "prepay_id" not in strResult:
                return
            strResult = json.loads(strResult)
            print("=======================strResult===================")
            print(strResult)
            print("=======================strResult===================")
            prepay_id = strResult["prepay_id"]
            response["package"] = "prepay_id=" + prepay_id
            response["signType"] = "MD5"
            key_sign = "appId={0}&nonceStr={1}&package={2}&signType={3}&timeStamp={4}&key={5}".format(
                response["appId"], response["nonceStr"], response["package"], response["signType"], response["timeStamp"], "hangzhouzhenlangjinchukou"
            )
            s = hashlib.md5()
            s.update(key_sign)
            response["paySign"] = s.hexdigest().upper()
            return response

        if other == "prepayconfig":
            args = request.args.to_dict()
            if "OMid" not in args:
                return PARAMS_MISS
            OMid = args["OMid"]
            package = "prepay_id=" + OMid.replace("-", "")
            import time
            timeStamp = int(time.time())
            response = {}
            response["appId"] = "wx284751ea4c889568"
            response["mch_id"] = "1504082901"
            response["device_info"] = "WEB"
            import uuid
            response["nonce_str"] = str(uuid.uuid1()).replace("-", "")
            key_sign = "appId={0}&nonceStr={1}&package={2}&signType={3}&timeStamp={4}&key={5}".format(
                response["appId"], response["nonce_str"], package, "MD5",
                timeStamp, "hangzhouzhenlangjinchukou"
            )
            import hashlib
            s = hashlib.md5()
            s.update(key_sign)
            response["sign"] = s.hexdigest().upper()
            response["sign_type"] = "MD5"
            response["body"] = "美妆类-美妆镜"
            response["out_trade_no"] = OMid
            response["fee_type"] = "CNY"
            response["total_fee"] = 1
            response["spbill_create_ip"] = "120.79.182.43"
            import datetime
            response["time_start"] = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            response["time_expire"] = (datetime.datetime.now() + datetime.timedelta(hours=2)).strftime("%Y%m%d%H%M%S")
            response["notify_url"] = "https://h878.cn/sharp/goods/other/getdata"
            response["trade_type"] = "JSAPI"
            return response

        if other == "openid":
            args = request.args.to_dict()
            print args
            if "code" not in args:
                return PARAMS_MISS
            code = args["code"]
            APP_ID = "wx284751ea4c889568"
            APP_SECRET_KEY = "051c81977efa8175e43686565265bb4f"
            request_url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type={3}"\
                .format(APP_ID, APP_SECRET_KEY, code, "authorization_code")
            conn = None
            bye = None
            try:
                import pycurl
                import io
                conn = pycurl.Curl()
                bye = io.BytesIO()
                conn.setopt(pycurl.WRITEFUNCTION, bye.write)
                conn.setopt(conn.url, request_url)
                conn.setopt(pycurl.SSL_VERIFYPEER, 1)
                conn.setopt(pycurl.SSL_VERIFYHOST, 2)
                conn.perform()
                response = bye.getvalue().decode("utf-8")
                #res = response.read()
                #print res
                print response
                if "openid" in response:
                    import json
                    res = json.loads(response)
                    return res["openid"]
            except BaseException as e:
                print e.message
            finally:
                conn.close()
                bye.close()


