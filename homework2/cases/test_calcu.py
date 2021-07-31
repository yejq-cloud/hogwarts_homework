"""
hogwarts 
yejq
"""
import allure
import pytest
import yaml
from homework2.calcu_code.calculator import Calculator


def get_cacldate():
    with open("./dates/calcudates.yaml")as f:
        totals = yaml.safe_load(f)
        return [totals["dates"], totals["ids"]]

@allure.feature("加法测试用例")
class TestAdd():
    @allure.story("加法测试")
    @pytest.mark.parametrize("a, b, c", get_cacldate()[0]["add_dates"], ids = get_cacldate()[1])
    def test_add(self,a, b, c, login, start_cases, case_run):
        calc = Calculator()
        assert c  == calc.add(a, b)

@allure.feature("减法测试用例")
class TestMinus():
    @allure.story("减法测试")
    @pytest.mark.parametrize("a, b, c", get_cacldate()[0]["munis_dates"], ids = get_cacldate()[1])
    def test_minus(self, a, b, c, login, start_cases, case_run):
        calc = Calculator()
        assert c == calc.minus(a, b)

@allure.feature("乘法测试用例")
class TestMcl():
    @allure.story("乘法测试")
    @pytest.mark.parametrize("a, b ,c", get_cacldate()[0]["mcl_dates"], ids = get_cacldate()[1])
    def test_mcl_int(self, a, b, c, login, start_cases, case_run):
        calc = Calculator()
        assert c == round(calc.mcl(a, b), 4)

@allure.feature("除法测试用例")
class TestDiv():
    @allure.story("除法测试")
    @pytest.mark.parametrize("a, b, c", get_cacldate()[0]["div_dates"], ids = get_cacldate()[1])
    def test_div(self, a, b, c, login, start_cases, case_run):
        calc = Calculator()
        try:
            assert c == calc.div(a, b)
        except ZeroDivisionError:
            print("除数不能为0")




