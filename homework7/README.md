
-企业微信实战
 -第一步：get获取token
  1.我的企业--企业信息：获取corpid
  2.管理工具--通讯录同步--设置权限--查看secret：获取corpsecret

 -第二步：获取token,用json().get()方法，不要用方括号，如果不存在，会有报错。
 mO_LNtmlZsLuc7QK3iAwIJIRXAof1pW0CyeRPtiWxfl3z9kBnaFSz6RHDVGQqAw7rEoxs5_3b0Kx9kwrhBRDmrb2w1RaFC6tl6WM0ENJZh0cwx5E0tV2kJsuXxUW5FEB8-uIdkPVRS0wns8vRy_fGWcQFJBtIptzTDPuEWBYG2KUgf8EPAsFv_-tX-0cnTmaWMmTAHWPzRJrGMCRLdcjDg

 -第三步：利用获取的token，做其他接口的测试

-作业：
 -老师代码地址：https://gitlab.stuq.ceshiren.com/ck/ck19/hogwartssdet19/-/tree/master/test_pytest
 -作业要求：
  -用通讯录的增删改查，实现接口的api封装和测试用例编写