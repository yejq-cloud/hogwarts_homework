"""
hogwarts 
yejq
"""

import pytest
import yaml
from testwork.homework4.PO.main_page import MainPage


class TestAddParterment():

    def setup(self):
        #主页实例化
        self.main = MainPage()

    def teardown(self):# 你还在吗？？这里打字在1

        pass
    @pytest.mark.parametrize('partername', yaml.safe_load(open("../homewor/dates/dates.yaml", encoding="utf-8")).get('datas'))
    def test_add_pater(self, partername):
        #链式调用
        result= self.main.click_contact().click_add_parterment().edit_partyname(partername).get_parterment_name()
        assert partername in result
        #问题1： edit_partyname 这里才是真的调用，要传一个具体值进去
        # 问题2：yaml格式不正确。具体查下yaml格式语法。
