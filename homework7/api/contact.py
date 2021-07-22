"""
hogwarts 
yejq
"""
import requests
from homework7.api.base import Base


class Contact(Base):

    def create_member(self, userid, name, mobile,department=1, **kwargs):

        '''
        创建成员
        :param userid: 成员ID
        :param name: 成员名字
        :param department: 部门ID
        :param mobile: email和mobile必填一个，选择填mobile
        :param kwargs:非必填参数
        :return:
        '''
        self.log_info("create_member")
        date ={
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department,
            "kwargs": kwargs
        }
        # 把其他非必填更新到数据当中。
        r = self.send("POST", f"user/create?access_token={self.token}", json=date)
        return r

    def get_member(self, userid):
        """
        获取成员
        :return:
        """
        self.log_info("get_member")
        r = self.send("GET", f"user/get?access_token={self.token}&userid={userid}")
        return r

    def update_member(self, userid):
        """
        更新成员
        :param userid:
        :return:
        """
        self.log_info("update_member")
        date = {
            "userid": userid
        }
        r = self.send("POST", f"user/update?access_token={self.token}", json=date)
        return r

    def del_member(self, userid):
        """
        删除成员
        :param userid:
        :return:
        """
        self.log_info("del_member")
        r = self.send("GET", f"user/delete?access_token={self.token}&userid={userid}")
        return r

    def get_simple_list(self):
        """
        获取部门1的成员列表
        :return:
        """
        self.log_info("get_simple_list")
        r = self.send("GET", f"user/simplelist?access_token={self.token}&department_id=1&fetch_child=0")
        return r

