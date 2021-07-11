
"""
hogwarts 
yejq
"""


from selenium.webdriver.common.by import By
from testwork.homework4.PO.basepage import BasePage


#添加部门页面,填写信息，然后跳转到通讯录界面
from testwork.homework4.PO.contact_page import ContactPage


class AddPartyPage(BasePage):
    _CLICK = (By.CSS_SELECTOR, "div.qui_dialog_foot.ww_dialog_foot > a")
    _EDITE = (By.CSS_SELECTOR, ".qui_inputText.ww_inputText:nth-child(2)")
    #填写要添加的部门
    def edit_partyname(self,partername): # 你这个是形参，不是实参。调用的时候要传值。
        #局部导入解决循环导入问题
        # opt = webdriver.ChromeOptions()
        # opt.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=opt)
        self.driver.find_element(*self._EDITE).send_keys(partername)
        # self.driver.find_element(By.CSS_SELECTOR, "div.qui_dialog_foot.ww_dialog_foot > a").click()
        self.find_and_click(*self._CLICK)

        return ContactPage(self.driver)
