# *- coding:utf8 *-
# *- coding:utf8 *-
import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from flask_restful import Resource,request
from config.response import PARAMS_MISS
from common.import_status import import_status
from config.response import SYSTEM_ERROR

class AOther(Resource):
    def __init__(self):
        from service.SOrders import SOrders
        self.sorders = SOrders()
        self.title = '============{0}============'

    def get(self, other):
        if other == "getdata":
            print("=======================api===================")
            print("接口名称是{0}，接口方法是get".format("getdata"))
            print("=======================api===================")
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
            print("=======================request_url===================")
            print str(request_url)
            print("=======================request_url===================")
            strResult = None
            try:
                import urllib2
                req = urllib2.Request(request_url)
                response = urllib2.urlopen(req)
                strResult = response.read()
                response.close()
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
            OMid = args["OMid"]
            response = {}
            response["appid"] = "wx284751ea4c889568"
            response["openid"] = openid
            import time
            response["timeStamp"] = int(time.time())
            import uuid
            response["nonceStr"] = str(uuid.uuid1()).replace("-", "")
            data = {}
            body = {}
            body["appid"] = "wx284751ea4c889568"
            body["mch_id"] = "1504082901"
            body["device_info"] = "WEB"
            body["nonce_str"] = str(uuid.uuid1()).replace("-", "")
            body["body"] = "Beauty mirror"
            body["out_trade_no"] = OMid.replace("-", "")
            OMprice = self.sorders.get_omprice_by_omid(OMid)
            print("============OMprice=========")
            print OMprice
            print("============OMprice=========")
            body["total_fee"] = int(OMprice * 100)
            body["spbill_create_ip"] = "120.79.182.43"
            import datetime
            body["time_start"] = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            body["time_expire"] = (datetime.datetime.now() + datetime.timedelta(hours=2)).strftime("%Y%m%d%H%M%S")
            body["notify_url"] = "https://h878.cn/sharp/goods/other/getdata"
            body["trade_type"] = "JSAPI"
            body["openid"] = openid
            key_sign = "appid={0}&body={1}&device_info={2}&mch_id={3}&nonce_str={4}&notify_url={5}&openid={6}" \
                       "&out_trade_no={7}&time_expire={8}&time_start={9}&total_fee={10}&trade_type={11}".format(
                body["appid"], "Beauty mirror", body["device_info"], body["mch_id"], body["nonce_str"],
                body["notify_url"], body["openid"], body["out_trade_no"], body["time_expire"], body["time_start"],
                body["total_fee"], body["trade_type"]
            )
            key_sign = key_sign + "&key={0}".format("HangZhouZhenLangHangZhouZhenLang")

            import hashlib
            s = hashlib.md5()
            s.update(key_sign)
            body["sign"] = s.hexdigest().upper()
            xml_body = """<xml>\n\t
                            <appid><![CDATA[{0}]]></appid>\n\t
                            <body><![CDATA[{1}]]></body>\n\t
                            <device_info><![CDATA[{2}]]></device_info>\n\t
                            <mch_id><![CDATA[{3}]]></mch_id>\n\t
                            <nonce_str><![CDATA[{4}]]></nonce_str>\n\t
                            <notify_url><![CDATA[{5}]]></notify_url>\n\t
                            <openid><![CDATA[{6}]]></openid>\n\t
                            <out_trade_no><![CDATA[{7}]]></out_trade_no>\n\t
                            <time_expire><![CDATA[{8}]]></time_expire>\n\t
                            <time_start><![CDATA[{9}]]></time_start>\n\t
                            <total_fee><![CDATA[{10}]]></total_fee>\n\t
                            <trade_type><![CDATA[{11}]]></trade_type>\n\t
                            <sign>{12}</sign>\n
                            </xml>\n""".format(body["appid"], "Beauty mirror", body["device_info"], body["mch_id"],
                                               body["nonce_str"],
                                               body["notify_url"], body["openid"], body["out_trade_no"],
                                               body["time_expire"], body["time_start"],
                                               body["total_fee"], body["trade_type"], body["sign"])
            print("=======================body===================")
            print(body)
            print("=======================body===================")
            data["xml"] = body
            strResult = None
            try:
                import urllib2
                url = "https://api.mch.weixin.qq.com/pay/unifiedorder"
                headers = {'Content-Type': 'application/xml'}
                # import xmltodict
                # xml_body = xmltodict.unparse(data)
                print("=======================xml_body===================")
                print xml_body
                print("=======================xml_body===================")
                req = urllib2.Request(url, headers=headers, data=xml_body)
                url_response = urllib2.urlopen(req)
                strResult = url_response.read()
                print 1
            except Exception as e:
                print e.message
            print("=======================strResult===================")
            print(str(strResult))
            print("=======================strResult===================")
            if not strResult:
                return
            import xmltodict
            json_strResult = xmltodict.parse(strResult)
            import json
            json_strResult = json.loads(json.dumps(json_strResult))

            json_result = json_strResult["xml"]
            print("=======================json_result===================")
            print(str(json_result))
            print("=======================json_result===================")
            if not json_strResult:
                return
            if "prepay_id" not in json_result:
                return

            prepay_id = json_result["prepay_id"]
            print("=======================prepay_id===================")
            print(str(prepay_id))
            print("=======================prepay_id===================")
            response["package"] = "prepay_id=" + str(prepay_id)
            response["signType"] = "MD5"
            key_sign = "appId={0}&nonceStr={1}&package={2}&signType={3}&timeStamp={4}&key={5}".format(
                response["appid"], response["nonceStr"], response["package"], response["signType"],
                response["timeStamp"], "HangZhouZhenLangHangZhouZhenLang"
            )
            s = hashlib.md5()
            s.update(key_sign)
            response["paySign"] = s.hexdigest().upper()
            order = {"OMstatus": 14}
            print(self.title.format("order"))
            print(order)
            print(self.title.format("order"))
            try:
                self.sorders.update_omstatus_by_omid(OMid, order)
            except Exception as e:
                print(self.title.format("update order error"))
                print(e.message)
                print(self.title.format("update order error"))
                return SYSTEM_ERROR
            return response

        if other == "prepayconfig":
            print("=======================api===================")
            print("接口名称是{0}，接口方法是get".format("prepayconfig"))
            print("=======================api===================")
            args = request.args.to_dict()
            if "openid" not in args or "OMid" not in args:
                return PARAMS_MISS
            print("=======================args===================")
            print(args)
            print("=======================args===================")
            openid = args["openid"]
            OMid = args["OMid"]
            response = {}
            response["appid"] = "wx284751ea4c889568"
            response["openid"] = openid
            import time
            response["timeStamp"] = int(time.time())
            import uuid
            response["nonceStr"] = str(uuid.uuid1()).replace("-", "")
            data = {}
            body = {}
            body["appid"] = "wx284751ea4c889568"
            body["mch_id"] = "1504082901"
            body["device_info"] = "WEB"
            body["nonce_str"] = str(uuid.uuid1()).replace("-", "")
            body["body"] = "Beauty mirror"
            body["out_trade_no"] = OMid.replace("-", "")
            body["total_fee"] = 1
            body["spbill_create_ip"] = "120.79.182.43"
            import datetime
            body["time_start"] = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            body["time_expire"] = (datetime.datetime.now() + datetime.timedelta(hours=2)).strftime("%Y%m%d%H%M%S")
            body["notify_url"] = "https://h878.cn/sharp/goods/other/getdata"
            body["trade_type"] = "JSAPI"
            body["openid"] = openid
            key_sign = "appid={0}&body={1}&device_info={2}&mch_id={3}&nonce_str={4}&notify_url={5}&openid={6}" \
                       "&out_trade_no={7}&time_expire={8}&time_start={9}&total_fee={10}&trade_type={11}".format(
                body["appid"], "Beauty mirror", body["device_info"], body["mch_id"], body["nonce_str"],
                body["notify_url"], body["openid"], body["out_trade_no"], body["time_expire"], body["time_start"],
                body["total_fee"], body["trade_type"]
            )
            key_sign = key_sign + "&key={0}".format("HangZhouZhenLangHangZhouZhenLang")

            import hashlib
            s = hashlib.md5()
            s.update(key_sign)
            body["sign"] = s.hexdigest().upper()
            xml_body = """<xml>\n\t
                <appid><![CDATA[{0}]]></appid>\n\t
                <body><![CDATA[{1}]]></body>\n\t
                <device_info><![CDATA[{2}]]></device_info>\n\t
                <mch_id><![CDATA[{3}]]></mch_id>\n\t
                <nonce_str><![CDATA[{4}]]></nonce_str>\n\t
                <notify_url><![CDATA[{5}]]></notify_url>\n\t
                <openid><![CDATA[{6}]]></openid>\n\t
                <out_trade_no><![CDATA[{7}]]></out_trade_no>\n\t
                <time_expire><![CDATA[{8}]]></time_expire>\n\t
                <time_start><![CDATA[{9}]]></time_start>\n\t
                <total_fee><![CDATA[{10}]]></total_fee>\n\t
                <trade_type><![CDATA[{11}]]></trade_type>\n\t
                <sign>{12}</sign>\n
                </xml>\n""".format(body["appid"], "Beauty mirror", body["device_info"], body["mch_id"], body["nonce_str"],
                    body["notify_url"], body["openid"], body["out_trade_no"], body["time_expire"], body["time_start"],
                    body["total_fee"], body["trade_type"], body["sign"])
            print("=======================body===================")
            print(body)
            print("=======================body===================")
            data["xml"] = body
            strResult = None
            try:
                import urllib2
                url = "https://api.mch.weixin.qq.com/pay/unifiedorder"
                headers = {'Content-Type': 'application/xml'}
                #import xmltodict
                #xml_body = xmltodict.unparse(data)
                print("=======================xml_body===================")
                print xml_body
                print("=======================xml_body===================")
                req = urllib2.Request(url, headers=headers, data=xml_body)
                url_response = urllib2.urlopen(req)
                strResult = url_response.read()
                print 1
            except Exception as e:
                print e.message
            print("=======================strResult===================")
            print(str(strResult))
            print("=======================strResult===================")
            if not strResult:
                return
            import xmltodict
            json_strResult = xmltodict.parse(strResult)
            import json
            json_strResult = json.loads(json.dumps(json_strResult))

            json_result = json_strResult["xml"]
            print("=======================json_result===================")
            print(str(json_result))
            print("=======================json_result===================")
            if not json_strResult:
                return
            if "prepay_id" not in json_result:
                return

            prepay_id = json_result["prepay_id"]
            print("=======================prepay_id===================")
            print(str(prepay_id))
            print("=======================prepay_id===================")
            response["package"] = "prepay_id=" + str(prepay_id)
            response["signType"] = "MD5"
            key_sign = "appId={0}&nonceStr={1}&package={2}&signType={3}&timeStamp={4}&key={5}".format(
                response["appid"], response["nonceStr"], response["package"], response["signType"],
                response["timeStamp"], "HangZhouZhenLangHangZhouZhenLang"
            )
            s = hashlib.md5()
            s.update(key_sign)
            response["paySign"] = s.hexdigest().upper()
            return response

    def post(self, other):
        if other == "getdata":
            print("=======================api===================")
            print("接口名称是{0}，接口方法是get".format("getdata"))
            print("=======================api===================")
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
