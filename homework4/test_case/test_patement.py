
"""
hogwarts 
yejq
"""
from selenium import webdriver
import yaml
from selenium.webdriver.common.by import By
from time import sleep


#复用浏览器，获取cookie

def test_getcookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address="127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    cookie_dates =  driver.get_cookies()
    with open("yaml.dates","w",encoding="utf-8") as f:
        yaml.dump(cookie_dates,f)

def test_load_cookie():

    # driver = webdriver.Chrome()
    # driver.get("https://work.weixin.qq.com/")
    # with open("yaml.dates",encoding="utf-8") as f:
    #     cookie_dates = yaml.safe_load(f)
    # for cookie in cookie_dates:
    #     driver.add_cookie(cookie)
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #进首页，开始进行测试步骤
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    sleep(2)
    driver.find_element(By.XPATH, "//*[@id= 'menu_contacts']").click()
    driver.find_element(By.CSS_SELECTOR,".js_add_sub_party").click()
    driver.find_element(By.CSS_SELECTOR,".qui_inputText.ww_inputText:nth-child(2)").send_keys("投资部")
    driver.find_element(By.CSS_SELECTOR,"div.qui_dialog_foot.ww_dialog_foot > a").click()
    #断言添加部门成功

    # ele = driver.find_elements(By.CSS_SELECTOR,'.member_colLeft_bottom a:last-child')
    # for i in ele:
    #     if i.get_attribute("text") == "投资部":
    #         return True

    num_list = []
    ele = driver.find_elements(By.CSS_SELECTOR,'.member_colLeft_bottom a:last-child')
    for value in ele:
        num_list.append(value.get_attribute("text"))
        return num_list

    assert "投资部" in num_list
    #定义一个列表---查找元素--遍历元素值--将值append到列表中---返回列表---判断新增的元素标签
