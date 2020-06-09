from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import sys, os
sys.path.append(os.getcwd())
from base.base_action import BaseAction


class SearchPage(BaseAction):
    search_button = By.ID, "com.android.settings:id/search"
    search_textview = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self, driver):
        self.driver = driver
        pass

    def clickSearchButton(self):
        self.clickAction(self.search_button)


    def clickBackButton(self):
        self.clickAction(self.back_button)

    def input_search(self, text):
        self.inputText(self.search_textview, text)