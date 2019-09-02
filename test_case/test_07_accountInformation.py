#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from airtest.core.api import *

from ElementPage.accountInformationPage import accountInformationPage
from ElementPage.bankCardInformationPage import bankCardInformationPage
from ElementPage.publicTool import publicTool


@allure.feature("账户信息")
class Test_AccountInformation():

    @allure.story("填写账户信息")
    @pytest.mark.run(order=3)
    def test_Account(self, poco):
        pubtool = publicTool(poco)
        accountinfo = accountInformationPage(poco)
        with allure.step("选择账户类别"):
            accountinfo.click_securitiesCash()
            accountinfo.click_futuresMargin()

        with allure.step("点击下一步"):
            pubtool.click_NextStepbtn()


if __name__ == "__main__":
    pytest.main(["-s", "test_05_bankCardInformation.py", '--alluredir', '../report/xml'])






