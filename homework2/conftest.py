"""
hogwarts 
yejq
"""
import pytest


@pytest.fixture(scope= "module")
def login():
    print("测试资源准备")
    yield
    print("测试资源回收")

@pytest.fixture(scope="class")
def start_cases():
    print("开始计算器运算测试")
    yield
    print("结束计算器运算测试")

@pytest.fixture()
def case_run():
    print("开始执行测试用例")
    yield
    print("结束执行测试用例")


