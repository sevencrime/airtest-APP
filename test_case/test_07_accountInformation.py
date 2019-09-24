#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from airtest.core.api import *

from Commons.GlobalMap import GlobalMap
from Commons.mongoTool import mongoTool
from ElementPage.accountInformationPage import accountInformationPage
from ElementPage.bankCardInformationPage import bankCardInformationPage
from ElementPage.publicTool import publicTool


@allure.feature("账户信息")
@pytest.mark.run(order=3)
class Test_AccountInformation():
    gm = GlobalMap()
    # mongo = mongoTool('mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net')
    mongo = mongoTool(gm.get_value("mongohost"))

    @allure.story("填写账户信息")
    def test_Account(self, poco):
        pubTool = publicTool(poco)
        pubTool.customersource()
        accountinfo = accountInformationPage(poco)
        with allure.step("判断外汇账户和金业账户是否出现"):
            accountinfo.get_leverMargin()
            accountinfo.get_bullionMargin()
        with allure.step("查询数据库"):
            if self.gm.get_value("source") == "aos" or self.gm.get_value("source") == "aos-uat":
                collection = "accounts"
                query = {"phone":"15089514626",  "forLogin":True}

            # import pdb; pdb.set_trace()
            result = self.mongo.findData(database=self.gm.get_value("environment"), collection=collection, query=query)

        with allure.step("选择账户类别"):
            accountinfo.click_securitiesCash(result)
            accountinfo.click_futuresMargin(result)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()


if __name__ == "__main__":
    pytest.main(["-s", "test_07_accountInformation.py", '--alluredir', '../report/xml'])






