#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from airtest.core.api import *

from ElementPage.bankCardInformationPage import bankCardInformationPage
from ElementPage.publicTool import publicTool


@allure.feature("银行卡信息")
class Test_bankCardInformation():

    @allure.story("银行卡信息")
    @pytest.mark.run(order=3)
    def test_bankCard(self, poco):
        pubTool = publicTool(poco)
        bankcard = bankCardInformationPage(poco)
        with allure.step("输入卡号"):
            bankcard.send_bankCardNo()

        with allure.step("输入银行名称"):
            bankcard.send_bankName()

        with allure.step("输入绑定手机号"):
            bankcard.send_bankPhone()

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()



if __name__ == "__main__":
    pytest.main(["-s", "test_05_bankCardInformation.py", '--alluredir', '../report/xml'])






