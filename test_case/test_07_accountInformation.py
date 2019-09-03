#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from airtest.core.api import *

from ElementPage.accountInformationPage import accountInformationPage
from ElementPage.bankCardInformationPage import bankCardInformationPage
from ElementPage.publicTool import publicTool


@allure.feature("账户信息")
@pytest.mark.run(order=3)
class Test_AccountInformation():

    @allure.story("填写账户信息")
    def test_Account(self, poco):
        pubTool = publicTool(poco)
        accountinfo = accountInformationPage(poco)
        with allure.step("判断外汇账户和金业账户是否出现"):
            accountinfo.get_leverMargin()
            accountinfo.get_bullionMargin()
            
        with allure.step("选择账户类别"):
            accountinfo.click_securitiesCash()
            accountinfo.click_futuresMargin()

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()


if __name__ == "__main__":
    pytest.main(["-s", "test_07_bankCardInformation.py", '--alluredir', '../report/xml'])






