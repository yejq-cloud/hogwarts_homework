"""
hogwarts 
yejq
"""
import logging

import requests


class Base:
    CORPID = "ww61263cb87673af40"
    CORPSECRET = "zn2asJ1w_Hra5xKyNnTBMYvMPjf0dav4sqjycB4s0wg"
    BASE_URL = "https://qyapi.weixin.qq.com/cgi-bin/"

    def __init__(self):
        self.token = self.get_token()

    def log_info(self, message):
        logging.info(message)

    def get_token(self):
        self.log_info("get_token")
        url = self.BASE_URL+f"gettoken?corpid={self.CORPID}&corpsecret={self.CORPSECRET}"
        r = requests.get(url)
        return r.json().get('access_token')

    def send(self, method, url, **kwargs):
        '''
        封装发送请求
        :param method:请求方式
        :param url:路由地址
        :param kwargs:其他各参数
        :return:
        '''
        self.log_info("send")
        self.log_info(method)
        self.log_info(url)
        url = self.BASE_URL + url
        # post 和 get 底层实现，requests.get == requests.request("GET",)
        return requests.request(method, url, **kwargs)