import time
import random
import shelve
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def getPhone():
    """生成手机号"""

    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数字
    third = {3: random.randint(0, 9),
             4: [5, 7, 9][random.randint(0, 2)],
             5: [i for i in range(10) if i != 4][random.randint(0, 8)],
             7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
             8: random.randint(0, 9), }[second]

    # 最后八位数字
    suffix = random.randint(9999999, 100000000)

    # 拼接手机号
    phone = f"1{second}{third}{suffix}"
    return phone


class TestWechat:
    def setup_method(self):
        # 复用浏览器
        option = Options()
        option.debugger_address = "127.0.0.1:9222"

        # 未安装chromedriver插件时指定driver路径
        # self.driver = webdriver.Chrome(executable_path="./chromedriver", options=option)

        # 通过brew cask install chromedriver安装webdriver后，不再需要指定路径
        # （如果浏览器版本和chromedriver不匹配，在网上下载对应版本替换就好了）
        self.driver = webdriver.Chrome(options=option)

    def teardown_method(self):
        # self.driver.quit()
        pass

    def test_wechat(self):
        """需求：使用 cookie 登录企业微信，完成添加联系人，加上断言验证"""

        # 打开企业微信通讯录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

        # 获取cookies
        # cookies = self.driver.get_cookies()
        # print(cookies)

        # shelve 模块， python 自带的对象持久化存储
        db = shelve.open('cookies')
        # 保存当前cookie
        # db['cookie'] = cookies
        # 获取db中的cookie
        cookies = db['cookie']
        db.close()

        # cookie中的expiry可能是浮点型，为避免报错需要转换一下或者删除
        for cookie in cookies:
            if "expiry" in cookie:
                # cookie.pop('expiry')
                cookie['expiry'] = int(cookie['expiry'])
                self.driver.add_cookie(cookie)

        # 让cookie生效，刷新页面
        self.driver.refresh()

        # 找到【添加成员】按钮，并点击
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".qui_btn.ww_btn.js_add_member")))
        self.driver.find_elements(By.CSS_SELECTOR, ".qui_btn.ww_btn.js_add_member")[1].click()

        # 等待姓名输入框加载完成
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "username")))

        # 输入姓名
        cardID = str(int(time.time()))
        name = "xingxing_" + cardID
        self.driver.find_element(By.ID, "username").send_keys(name)

        # 输入帐号
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(cardID)

        # 输入手机号
        phone = getPhone()
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phone)

        # 点击保存按钮
        self.driver.find_element(By.CSS_SELECTOR, ".qui_btn.ww_btn.js_btn_save").click()

        # 判断是否保存成功
        try:
            # 如果10秒还未自动返回上一页，说明当前页报错，添加成员失败
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".qui_btn.ww_btn.js_btn_save")))
        except:
            # 自动跳转回通讯录列表页（能找到添加成员按钮），说明添加成功
            assert "成功添加成员！"
        else:
            # 获取当前页面的报错信息
            tips = self.driver.find_elements(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
            errors = []
            for tip in tips:
                if tip.text != "":
                    errors.append(tip.text)
            assert errors == []
