import time
import allure
from config.configtest import host, phone
from lib import djs_tool
from lib.request_tool import RequestsTool
import urllib3
urllib3.disable_warnings()


@allure.feature('登录模块')
class TestLogin:
    @staticmethod
    def get_phone_code():
        get_code_url = host + "/srapi/verifyphone/sendcode"
        get_code_argument = {"phone": phone}
        r = RequestsTool().do_request(method="post", url=get_code_url, json=get_code_argument)
        return r

    @classmethod
    @allure.story('正确验证码登录')
    def test_login_by_true_code(cls):
        r = TestLogin.get_phone_code()
        if r.status_code == 201:
            login_url = host + "/srapi/auth/verifyAccount"
            login_argument = {"phone": phone, "code": r.json()["code"]}
            res = RequestsTool().do_request("post", url=login_url, json=login_argument)
            assert res.json()['success'] is True
            assert res.json()['msg'] == '登录成功'
            return res.json()
        else:
            while r.status_code == 405:
                print("一分钟之前已发过验证码，60秒后自动重新尝试发送验证码")
                djs_tool.djs(60)
                r = TestLogin.get_phone_code()
                login_url = host + "/srapi/auth/verifyAccount"
                login_argument = {"phone": phone, "code": r.json()["code"]}
                res = RequestsTool().do_request("post", url=login_url, json=login_argument)
                assert res.json()['success'] is True
                assert res.json()['msg'] == '登录成功'
                return res.json()
            else:
                print("登录失败")
