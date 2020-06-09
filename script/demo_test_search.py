import sys, os
sys.path.append(os.getcwd())
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from page.search_page import SearchPage
from base.base_driver import init_driver
from base.base_yml import yml_data_with_file


class TestSearch:


    def get_search(key):
        data = yml_data_with_file("search_data")[key]
        print(data)
        return data

    def setup(self):
        #打开driver
        self.driver = init_driver()
        self.searchPage = SearchPage(self.driver)


    @pytest.mark.parametrize("keys", get_search("test_search"))
    def test_search(self, keys):
        #打开search界面
        self.searchPage.clickSearchButton()
        #点击search搜索框输入搜索内容
        self.searchPage.input_search(keys)
        #按返回键退出
        self.searchPage.clickBackButton()
        pass

if __name__ == '__main__':
    TestSearch.get_search("test_search")