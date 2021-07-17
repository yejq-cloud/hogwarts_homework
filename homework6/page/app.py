"""
hogwarts 
yejq
"""
from appium import webdriver
from homework6.page.basepage import Base
from homework6.page.mainpage import MainPage


class App(Base):  #做了复用后，也需要继承Base.
    def start(self):
        #启动应用
        if self.driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["deviceName"] = "hogwarts"
            caps["noReset"] = "true"

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(15)
        else:
            # launch_app() 可以直接启动caps里面的应用。
            #start_activity 可以帮我们传递任何包，只需要指定app_package,app_activity
            # self.driver.start_activity()
            self.driver.launch_app()

        return self

    #由于每次启动消耗时间，driver复用，让应用热启动。

    def restart(self):
        self.driver.close()
        self.driver.launch_app()

    def quit(self):
        self.driver.quit()

    def goto_main(self):
        # 传递driver,实际是实例化了一个类。在实例化创建driver，用__init__方法。
        return MainPage(self.driver)
