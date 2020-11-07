import time
from pageobject_wechat.methods.get_phone import get_phone
from pageobject_wechat.pages.contacts_page import ContactsPage


class TestContact:
    def test_add_contact(self):
        # 帐号
        cardID = str(int(time.time()))
        # 姓名
        name = "cs" + cardID
        # 手机号
        phone = get_phone()

        # 实例化页面对象
        self.contact_page = ContactsPage()
        # 添加联系人
        self.contact_page.click_add_contact().add_contact(name=name, cardID=cardID, phone=phone)
        # 通过搜索判断联系人是否创建成功
        assert self.contact_page.search_contact(name=name)
