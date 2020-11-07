import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobject_wechat.pages.basepage import BasePage
from pageobject_wechat.pages.contact_page_add import ContactAddPage


class ContactsPage(BasePage):
    _baseurl = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def search_contact(self, name):
        # 判断{name}是否在联系人列表中
        # 进行联系人搜索
        self.driver.find_element(By.ID, "memberSearchInput").send_keys(name)
        # 等待搜索完成
        WebDriverWait(self.driver, 5).until_not(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".jstree.jstree-1.jstree-default")))
        # 获得搜索结果
        result = self.driver.find_elements(By.CSS_SELECTOR, "ul#search_member_list li")
        # 如果搜索结果为空，则无对应联系人
        if len(result) == 0:
            return False
        search_name = self.driver.find_elements(By.CSS_SELECTOR, "li a span.ww_searchResult_title_peopleName")[0].text
        # search_name = self.driver.find_element(By.CSS_SELECTOR, ".member_display_cover_detail_name").text
        return search_name == name

    def click_add_contact(self):
        # 找到【添加成员】按钮，并点击
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".qui_btn.ww_btn.js_add_member")))
        self.driver.find_elements(By.CSS_SELECTOR, ".qui_btn.ww_btn.js_add_member")[2].click()
        return ContactAddPage(self.driver)
