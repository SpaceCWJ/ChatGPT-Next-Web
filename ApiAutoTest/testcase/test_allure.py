import allure


@allure.feature("测试大模块feature")
class TestAllure:

    @allure.story("测试子模块01")
    def test_01(self):
        print('this is test_01')

    # @allure.story("测试子模块02")
    @allure.step("测试步骤1")
    def test_02(self):
        with allure.step("测试步骤01"):
            print('this is test_02-1')
        with allure.step("测试步骤02"):
            print('this is test_02-2')


@allure.feature("功能2")
class TestAllure2:

    @allure.story("测试子模块01")
    def test_01(self):
        print('this is test_01')

    @allure.story("测试子模块02")
    @allure.step("测试步骤1")
    @allure.link(url='https://www.baidu.com/', name="百度链接")
    @allure.testcase("https://zentao.sureemed.com/testcase-browse-46.html",name="测试case链接")
    @allure.issue("https://zentao.sureemed.com/bug-view-2812.html", name="关联bug")
    @allure.severity(severity_level=allure.severity_level.BLOCKER)
    def test_02(self):
        with allure.step("测试步骤01"):
            print('this is test_02-1')
        with allure.step("测试步骤02"):
            print('this is test_02-2')
            allure.attach('hhhhhh', attachment_type=allure.attachment_type.TEXT)
            allure.attach('<body>邮箱</body>', '汉字', attachment_type=allure.attachment_type.HTML)
            allure.attach.file('./images/test01.jpg', name='beautiful', attachment_type=allure.attachment_type.JPG)
