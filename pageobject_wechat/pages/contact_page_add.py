from selenium.webdriver.common.by import By

from pageobject_wechat.pages.basepage import BasePage


class ContactAddPage(BasePage):
    def add_contact(self, name, cardID, phone):
        # 输入姓名
        self.driver.find_element(By.ID, "username").send_keys(name)

        # 输入帐号
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(cardID)

        # 输入手机号
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phone)

        # 点击保存按钮
        self.driver.find_element(By.CSS_SELECTOR, ".qui_btn.ww_btn.js_btn_save").click()
