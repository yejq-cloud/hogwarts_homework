from testwork.calculator_code.calculator import Calculator
import pytest
import yaml
#获取数据函数
def get_calcadd_dates():
    with open("./dates/calcu_add.yaml") as f:
        totals1 = yaml.safe_load(f)
        return [totals1['dates1'],totals1['ids1']]

def setup_module():
    print("资源准备：setup_medule")

def teardown_module():
    print("资源回收：teardown_module")

# 加法测试用例
class TestAdd():
    def setup_class():
        print("开始测试加法用例")

    def teardown_class():
        print("结束测试加法用例")

    def setup(self):
        print("开始执行测试用例")

    def teardown(self):
        print("结束执行测试用例")

    @pytest.mark.parametrize("a,b,expect", get_calcadd_dates()[0], ids = get_calcadd_dates()[1])
    def test_add1(self,a,b,expect):
        calc = Calculator()
        assert expect == calc.add(a, b)

def get_calcdiv_dates():
    with open("./dates/calcu_div.yaml") as g:
        totals2 = yaml.safe_load(g)
        return [totals2['dates2'],totals2['ids2']]

# #除法测试用例
class TestDiv():
    def setup_class(self):
        calc = Calculator()
        print("开始除法测试：setup_class")

    def teardown_class(self):
        print("结束除法测试：teardown_class")

    def setup(self):
        print("开始执行测试用例：setup")

    def teardown(self):
        print("结束执行测试用例：teardown")
    @pytest.mark.parametrize("a,b,expect", get_calcdiv_dates()[0], ids = get_calcdiv_dates()[1])
    def test_div1(self,a,b,expect):

        try:
            cacl = Calculator()
            round(cacl.div(a,b))  #四舍五入取整
            assert expect == cacl.div(a, b)
        except ZeroDivisionError:
            print("b不能为0")