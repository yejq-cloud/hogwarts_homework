"""
hogwarts 
yejq
"""
from selenium import webdriver
import yaml
from selenium.webdriver.common.by import By
import time



#复用浏览器，获取cookie
def test_getcookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address="127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    driver.find_element_by_id("menu_apps").click()
    cookie_dates = driver.get_cookies()
    with open("date,yaml", "w", encoding="utf-8") as f:
        yaml.dump(cookie_dates,f)

def test_load_cookie():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/")
    with open("date,yaml", encoding="utf-8") as f:
        yaml_date = yaml.safe_load(f)   #yaml反序列化
    for cookie in yaml_date:
        driver.add_cookie(cookie)

    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    driver.find_element_by_id("menu_contacts").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(1) > a.qui_btn.ww_btn.js_add_member").click()

    # driver.find_element(By.CSS_SELECTOR,"div.ww_inputWithTips_tips").send_keys("测试员1")
    time.sleep(3)
    driver.find_element(By.XPATH,'//*[@id = "username"]').send_keys("测开学员1")
    driver.find_element_by_id("memberAdd_english_name").send_keys("基哥")
    driver.find_element_by_xpath('//*[@id = "memberAdd_acctid"]').send_keys("4253462")
    driver.find_element(By.ID,"memberAdd_phone").send_keys("13789892222")
    driver.find_element(By.CSS_SELECTOR,"a.qui_btn.ww_btn.js_btn_save").click()
    time.sleep(3)
