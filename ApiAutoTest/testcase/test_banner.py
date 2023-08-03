import allure

from config.configtest import host
from lib.request_tool import RequestsTool


@allure.feature('Banner模块')
class TestBanner:

    @allure.story('获取轮播图')
    def test_get_banner_list(self):
        url = host + '/srapi/banner/list'
        r = RequestsTool.do_request('get', url=url)
        assert r.json()['success'] is True
        assert r.json()['result'] is not None

    @allure.story('轮播列表详情')
    def test_banner_detail(self):
        url = host + '/srapi/banner/detail'
        argument = {'detailId': '611e2d69337f821facedb8f0'}
        r = RequestsTool.do_request('get', url=url, params=argument)
        assert r.json()['success'] is True
        assert r.json()['result'] is not None
