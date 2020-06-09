from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_xpath import make_xpath_with_feature


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def clickAction(self, lop):
        self.getElement(lop).click()

    def inputText(self, lop, text):
        self.getElement(lop).send_keys(text)

    def getElement(self, loc):
        by = loc[0]
        value = loc[1]
        if by == By.XPATH:
            value = make_xpath_with_feature(loc[1])
        return WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(by, value))
