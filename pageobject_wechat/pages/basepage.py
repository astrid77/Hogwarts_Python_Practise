from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BasePage:
    _baseurl = ""

    def __init__(self, driver: webdriver = None):
        # 复用浏览器
        if driver == None:
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
            # 添加一个全局的隐式等待
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

        if self._baseurl != "":
            self.driver.get(self._baseurl)
