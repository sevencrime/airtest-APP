#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from airtest.core.api import *

from Commons.mongoTool import mongoTool
from ElementPage.bankCardInformationPage import bankCardInformationPage
from ElementPage.publicTool import publicTool


@allure.feature("人脸识别")
class Test_faceid():

    mongo = mongoTool('mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net')

    @allure.story("填写个人资料")
    @pytest.mark.run(order=3)
    def test_bankCard(self, poco):
        pubTool = publicTool(poco)
        with allure.step("修改数据库currentRoute"):
            # import pdb; pdb.set_trace()
            self.mongo.UpdataData(database="uat")

        with allure.step("退出开户表单"):
            pubTool.closeform()

        with allure.step("重新进入表单"):
            pass



if __name__ == "__main__":
    pytest.main(["-s", "test_06_faceid.py", '--alluredir', '../report/xml'])






