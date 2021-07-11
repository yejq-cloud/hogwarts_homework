
"""
hogwarts 
yejq
"""
from selenium.webdriver.common.by import By
from testwork.homework4.PO.basepage import BasePage
from testwork.homework4.PO.contact_page import ContactPage

#先进入主页
class MainPage(BasePage):
    _CONTACT = (By.ID, "menu_contacts")

    def click_contact(self):
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=opt)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")


        # self.driver.find_element(By.XPATH, "//*[@id= 'menu_contacts']").click()
        self.find_and_click(*self._CONTACT)
        #跳转到通讯录页面
        return ContactPage(self.driver)