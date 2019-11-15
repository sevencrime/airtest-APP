#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import allure
import pytest
from airtest.core.api import *

from Commons import CommonsTool
from Commons.CommonsTool import query_initialData
from Commons.GlobalMap import GlobalMap
from Commons.mongoTool import mongoTool
from ElementPage.accountInformationPage import accountInformationPage
from ElementPage.publicTool import publicTool
from test_case.parentBase import ParentBase


@allure.feature("账户信息")
class Test_AccountInformation():
    gm = GlobalMap()
    query_initialData()
    # mongo = mongoTool('mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net')

    @allure.story("填写账户信息")
    def test_Account(self, poco):
        mongo = mongoTool(self.gm.get_value("mongohost"))
        pubTool = publicTool(poco)
        pubTool.get_appcationNumber()
        accountinfo = accountInformationPage(poco)
        with allure.step("判断外汇账户和金业账户是否出现"):
            accountinfo.get_leverMargin()
            accountinfo.get_bullionMargin()

        with allure.step("查询数据库, 获取数据的初始值"):

            if self.gm.get_value("environment").find("aos") != -1:
                collection = "accounts"
                query = {"applyCode":self.gm.get_value("appcationNumber"),  "forLogin":True}
            elif self.gm.get_value("environment").find("uat") != -1 or self.gm.get_value("environment").find("test") != -1:
                collection = "apply"
                query = {"applySeqId":self.gm.get_value("appcationNumber")}
            else:
                self.log.deubg("数据可能有问题哦!!!")


            # 查询数据库
            result = mongo.findData(database=self.gm.get_value("environment"), collection=collection, query=query)

        with allure.step("选择账户类别"):
            accountinfo.click_securitiesCash(result)
            accountinfo.click_futuresMargin(result)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()


if __name__ == "__main__":
    pytest.main(["-s", "test_07_accountInformation.py", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()




