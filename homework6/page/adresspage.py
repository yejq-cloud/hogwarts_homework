"""
hogwarts 
yejq
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from homework6.page.basepage import Base
from homework6.page.editpage import EditPage


class AdressPage(Base):
    _ADDHAND = (MobileBy.XPATH, "//* [@text='手动输入添加']")
    # def __init__(self,driver: WebDriver):
    #     #实例化一个driver,将上个页面的driver传过来。
    #     #继承Base后，这里的init方法就不需要了
    #     self.driver = driver

    def click_handadd(self):
        # self.driver.find_element(MobileBy.XPATH,"//* [@text='手动输入添加']").click()
        # 替换成封装的方法，并将需要传的数据提去出去
        self.find_and_click(*self._ADDHAND)
        return EditPage(self.driver)

    def get_toast(self):
        # result = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        # 将toast方法也封装到basepage里面
        result = self.get_toast_text()
        print(f"获取到到tost", {result})#查看查找的结果,这一步调试用
        return result