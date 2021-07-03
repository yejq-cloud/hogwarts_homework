"""
hogwarts 
yejq
"""
from random import random
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy




class TestAddMember():
    def setup(self):
        # 资源准备（初始化）
        caps = {}
        caps["platformName"] = "android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["deviceName"] = "hogwarts"
        caps["noReset"] = "true"
        # 至关重要的一行，与Appium服务建立连接，并传递一个caps字典对象
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)
    def teardown(self):
        self.driver.quit()

    # @pytest.mark.parametrize('[name,phonenumber]', "[['赵云','13376871235'],['马超'，'13367545671']]")
    def test_addmember(self):
        self.driver.find_element(MobileBy.XPATH," //* [@text='通讯录']").click()
        sleep(5)
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                     'new UiScrollable(new UiSelector().scrollable(true).\
                                     instance(0)).scrollIntoView(new UiSelector().\
                                     text("添加成员").instance(0));').click()
        sleep(5)
        self.driver.find_element(MobileBy.XPATH,"//* [@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/b09").send_keys("name")
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/f7y").send_keys("13678654568")
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/ad2").click()

        toast = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        print(f"获取到到tost", {toast})
        assert '添加成功' == toast


