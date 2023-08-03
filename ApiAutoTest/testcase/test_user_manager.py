from config.configtest import host
from lib.request_tool import RequestsTool
import allure
import urllib3
urllib3.disable_warnings()


@allure.feature('用户管理模块')
class TestUserManager:

    @allure.story('获取职称')
    def test_get_title(self):
        url = host + '/srapi/account/gettitle'
        argument = {}
        r = RequestsTool.do_request('get', url=url, params=argument)
        assert r.status_code == 200
        assert r.json()["success"] is True
        assert r.json()["result"] is not None
        # print('获取职称')

    @allure.story('获取地区')
    def test_get_district(self):
        url = host + '/srapi/account/getdistrict'
        argument = {}
        r = RequestsTool.do_request('get', url=url, params=argument)
        assert r.status_code == 200
        assert r.json()["success"] is True
        assert r.json()["result"] is not None
        # print('获取地区')

    @allure.story('获取医院')
    def test_get_hcp(self):
        url = host + '/srapi/account/gethcp'
        argument = {"location": 110000}
        r = RequestsTool.do_request('get', url=url, params=argument)
        assert r.status_code == 200
        assert r.json()["success"] is True
        assert r.json()["result"] is not None
        # print('获取医院')

    @allure.story('获取医院 By areaname')
    def test_get_hospital_byareaname(self):
        url = host + '/srapi/account/gethospitalbyareaname'
        argument = {"areaname": '上海'}
        r = RequestsTool.do_request('get', url=url, params=argument)
        assert r.status_code == 200
        assert r.json()["success"] is True
        assert r.json()["result"] is not None
        # print('获取医院 By areaname')

    @allure.story('获取科室')
    def test_get_depart(self):
        url = host + '/srapi/account/getdepart'
        argument = {}
        r = RequestsTool.do_request('get', url=url, params=argument)
        assert r.status_code == 200
        assert r.json()["success"] is True
        assert r.json()["result"] is not None
        # print('获取科室')

    @allure.story('获取科室完整数据')
    def test_get_department(self):
        url = host + '/srapi/account/getdepartment'
        argument = {}
        r = RequestsTool.do_request('get', url=url, params=argument)
        assert r.status_code == 200
        assert r.json()["success"] is True
        assert r.json()["result"] is not None
        # print('获取科室完整数据')
        # print(r.json())

    @allure.story('获取标签列表')
    def test_get_taglist(self):
        url = host + '/srapi/account/gettaglist'
        argument = {}
        r = RequestsTool.do_request('get', url=url, params=argument)
        assert r.status_code == 200
        assert r.json()["success"] is True
        assert r.json()["result"] is not None
        # print('获取标签列表')

    @allure.story('保存标签')
    def test_save_tags(self, get_headers):
        get_tag_list_url = host + '/srapi/account/gettaglist'
        save_tags_url = host + '/srapi/account/savetags'
        res = RequestsTool.do_request('get', url=get_tag_list_url)
        tag_list = res.json()["result"]
        argument = {"list": tag_list}
        r = RequestsTool.do_request("post", url=save_tags_url, json=argument, headers=get_headers)
        assert r.json()["success"] is True
        assert r.json()["result"] is True
        print('保存标签')

    @allure.story('保存空标签')
    def test_save_no_tags(self, get_headers):
        save_tags_url = host + '/srapi/account/savetags'
        tag_list = []
        argument = {"list": tag_list}
        r = RequestsTool.do_request("post", url=save_tags_url, json=argument, headers=get_headers)
        assert r.json()["success"] is True
        assert r.json()["result"] is True
        # print('保存空标签')

    @allure.story('保存信息')
    def test_save_infor(self,get_headers):
        url = host + '/srapi/account/saveinfo'
        argument = {
            "name": "陈万军",
            "sex": "2",
            "idcard": "342423199704294973",
            "birthday": "1989-08-09",
            "diseases": "鼻腔难受",
            "diseasesImgs": [
                'https://osspub.sureemed.com/user.avatar/1687330504671952AC332-F36F-4988-B2AA-E6DCD688FC06.jpg'],
            "province": "5a719cf9fcf21e2f733f5513",
            "city": "5a719cf9fcf21e2f733f5517"
        }
        r = RequestsTool.do_request("post", url=url, json=argument, headers=get_headers)
        assert r.json()["success"] is True
        assert r.json()["result"] is True
        # print('保存信息')

    @allure.story('获取嗅觉科研个人信息')
    def test_get_smell_user_infor(self,get_headers):
        url = host + '/srapi/account/getSmellUserInfo'
        r = RequestsTool.do_request('get', url=url, headers=get_headers)
        assert r.json()['success'] is True
        assert r.json()['result']['name'] == '陈万军'
        assert r.json()['msg'] == '获取成功'
        # print('获取嗅觉科研个人信息')

    @allure.story('获取日历信息')
    def test_get_calendar_list(self,get_headers):
        url = host + '/srapi/account/getCalendarList'
        argument = {'startTime': '2022-05-01', 'endTime': '2022-05-31'}
        r = RequestsTool.do_request('get', url=url, params=argument, headers=get_headers)
        assert r.json()['success'] is True
        assert r.json()['result'] is not None
        # print('获取日历信息')

    @allure.story('获取单天日历信息')
    def test_get_calendar_infor(self,get_headers):
        url = host + '/srapi/account/getCalendarInfo'
        argument = {'dayTime': '2023-05-01'}
        r = RequestsTool.do_request('get', url=url, params=argument, headers=get_headers)
        assert r.json()['success'] is True
        assert r.json()['result'] is not None
        # print('获取单天日历信息')

    @allure.story('获取版本')
    def test_get_version(self):
        url = host + '/srapi/account/getVersion'
        r = RequestsTool.do_request('get', url=url)
        assert r.json()['success'] is True
        assert r.json()['result'] is not None
        # print('获取版本')
