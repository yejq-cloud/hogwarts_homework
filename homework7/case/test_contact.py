"""
hogwarts 
yejq
"""
import json

import allure
import requests
from faker import Faker
from homework7.api.contact import Contact

fake = Faker("zh_CN")

@allure.feature("成员增删改查接口测试")
class TestContact():

    USERID = fake.bban()
    NAME = fake.name()
    MOBILE = fake.phone_number()

    def setup_class(self):
        self.contact = Contact()

    @allure.story('创建成员接口用例')
    def test_create(self):
        with allure.step('创建成员步骤'):
            r = self.contact.create_member(self.USERID, self.NAME,self.MOBILE)
        with allure.step('判断成功创建成员'):
            assert r.json().get("errcode") == 0

    @allure.story('更新成员接口用例')
    def test_update(self):
        with allure.step('添加新成员'):
            self.contact.create_member(self.USERID, self.NAME,self.MOBILE)
        with allure.step('判断成功更新成员'):
            assert self.contact.update_member(self.USERID).json().get("errcode") == 0

    @allure.story('获取成员接口用例')
    def test_get(self):
        with allure.step('添加新成员'):
            self.contact.create_member(self.USERID, self.NAME,self.MOBILE)
        with allure.step('判断成功获取成员'):
            assert self.contact.get_member(self.USERID).json().get("errcode") == 0

    @allure.story('删除成员接口用例')
    def test_delete(self):
        with allure.step('添加新成员'):
            self.contact.create_member(self.USERID, self.NAME,self.MOBILE)
        with allure.step('判断成功删除成员'):
            assert self.contact.del_member(self.USERID).json().get("errcode") == 0

    @allure.story('获取部门成员接口用例')
    def test_simple_list(self):
        with allure.step('判断成功获取部门列表'):
            assert self.contact.get_simple_list().json().get("errcode") == 0

