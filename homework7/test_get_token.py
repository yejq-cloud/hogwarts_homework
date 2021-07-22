"""
hogwarts 
yejq
"""
import requests


def test_requests():
    #获取企业微信token.
    corpid = "ww61263cb87673af40"
    corpsecret = "zn2asJ1w_Hra5xKyNnTBMYvMPjf0dav4sqjycB4s0wg"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    r = requests.get(url)
    token = r.json().get('access_token')

    r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={token}&id=ID")
    print(r.json())