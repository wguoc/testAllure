import sys, os

from allure_commons import _allure
from allure_commons.types import Severity

sys.path.append(os.getcwd())
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from page.search_page import SearchPage
from base.base_driver import init_driver
from base.base_yml import yml_data_with_file


class TestContact:

    @_allure.step(title = '登录的测试脚本')
    def test_login(self):
        print("111")
        _allure.attach("输入用户名","输入用户名的描述")
        print("输入用户名")
        _allure.attach("输入密码", "输入密码的描述")
        print("输入密码")
        _allure.attach("点击登录", "登录的描述")
        print("点击登录")
        assert 1

    @_allure.severity(Severity.BLOCKER)
    def test_loginOut(self):
        print("222")
        assert 1


