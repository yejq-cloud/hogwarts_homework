"""
hogwarts 
yejq
"""
import allure
from faker import Faker
from homework6.page.app import App


@allure.feature("通讯录")
class TestAddMember():
    def setup_class(self):
        self.fake = Faker('zh_CN')
        #self.app不能放在setup里里面，会每次新建一个新的实例
        self.app = App()
    def setup(self):
        # self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        # self.app.quit()
        # self.app.restart()
        pass


    def teardown_class(self):
        self.app.quit()


    allure.story("添加成员")
    def test_add_member(self):
        name = self.fake.name()
        phonumber = self.fake.phone_number()
        result = self.main.click_contact().click_addmember()\
            .click_handadd().edit_member(name, phonumber).get_toast()
        assert "添加成功" == result

class TestDelMember():
    def setup_class(self):
        self.fake = Faker('zh_CN')
        # self.app不能放在setup里里面，会每次新建一个新的实例
        self.app = App()

    def setup(self):
        # self.app = App()
         self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.quit()
                # self.app.restart()

    def teardown_class(self):
        self.app.quit()

    allure.story("删除成员")
    def test_del_member(self,name_member):
        self.main.click_contact().find_member()\
            .click_three().click_edit().click_delmember()\
            .click_confirm()

