import pytest
from testcase.test_login import TestLogin
res = TestLogin.test_login_by_true_code()
token = 'Bearer ' + res["result"]["accessToken"]
headers = [{"Authorization": token}]


@pytest.fixture(scope='package', params=headers)
def get_headers(request):
    print("执行yield前面的代码")
    yield request.param
    print("执行yield后面的代码")


