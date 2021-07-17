"""
hogwarts 
yejq
"""
from appium import webdriver

class TestAddMember:
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appActivity": ".launch.WwMainActivity",
            "appPackage": "com.tencent.wework",
            "noReset": True
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)
    def teardown(self):
        pass


    def test_add_member(self):

        el1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
        el1.click()
        assert True

