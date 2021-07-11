
"""
hogwarts 
yejq
"""
from time import sleep

from selenium.webdriver.common.by import By

#然后通讯录页面
from testwork.homework4.PO.add_party_page import AddPartyPage
from testwork.homework4.PO.basepage import BasePage


class ContactPage(BasePage):
    _ADDPARTNAME = (By.CSS_SELECTOR, ".js_add_sub_party")
    def click_add_parterment(self):
        sleep(2)
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=opt)
        # self.driver.implicitly_wait(10)
        # self.driver.find_element(By.CSS_SELECTOR, ".js_add_sub_party").click()
        self.find_and_click(*self._ADDPARTNAME)
        #跳转到添加子部门页面
        return AddPartyPage(self.driver)

    def get_parterment_name(self):
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=opt)
        sleep(2)
        num_list = []
        # ele = self.driver.find_elements(By.CSS_SELECTOR, '.member_colLeft_bottom a:last-child')
        ele = self.finds(By.CSS_SELECTOR, '.member_colLeft_bottom a:last-child')
        for value in ele:
            num_list.append(value.get_attribute("text"))
        return num_list