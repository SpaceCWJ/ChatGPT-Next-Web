from config.configtest import host
from lib.request_tool import RequestsTool


class TestCenter:
    def test_my_favorites(self, get_headers):
        url = host + '/srapi/profile/favorites'
        argument = {'page': 1, 'pageSize': 10}
        r = RequestsTool.do_request('get', url=url, params=argument, headers=get_headers)
        assert r.json()['success'] is True
        assert r.json()['result'] is not None
