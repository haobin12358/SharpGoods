# *- coding:utf8 *-
import urllib2
import json
HTTP_HOST = "h878.cn"
HTTP_SERVER = "https"
HTTP_HEADER = {'Content-Type': 'application/json'}
ERROR_CODE = 0
title = "======={0}======="
def test_user_login():
    try:
        api_login = "/sharp/goods/users/login"
        url_login = "{0}://{1}{2}".format(HTTP_SERVER, HTTP_HOST, api_login)
        data = "{\n\t\"UStelphone\":\"17706441101\",\n\t\"USpassword\":\"123\"\n}"
        req = urllib2.Request(url_login, headers=HTTP_HEADER, data=data)
        response = urllib2.urlopen(req)
        strResult = response.read()
        jsonResult = json.loads(strResult)
        if "status" not in jsonResult:
            return False
        status = jsonResult["status"]
        if status != 200:
            return False
        return True
    except Exception as e:
        print(title.format("message"))
        print(e.message)
        print(title.format("message"))
        return False

if __name__ == '__main__':
    if not test_user_login():
        ERROR_CODE = ERROR_CODE + 1
    print(ERROR_CODE)
