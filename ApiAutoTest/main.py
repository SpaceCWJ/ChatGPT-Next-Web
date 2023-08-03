import pytest

if __name__ == '__main__':
    pytest.main(['-vs', "--alluredir=./testreport/json", '--clean-alluredir'])
    #
    # pytest.main(['-vs', '--report=.html',
    #              '--title=曙瑞自动化测试报告',
    #              '--tester=VictorChen',
    #              '--desc=测试报告描述',
    #              '--template=2'])

