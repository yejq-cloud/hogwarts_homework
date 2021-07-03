"""
hogwarts 
yejq
"""
from testwork.homework5.objectpage.base_page import Base
from testwork.homework5.objectpage.main_page import MainPage
# import pytest


class TestAddMember():

    def setup(self):
        self.main = MainPage()
    def teardown(self):
        pass

    def test_add_member(self):
        result = self.main.go_to_contact().click_addmember().click_addname().edit_member().get_member()


        return True


