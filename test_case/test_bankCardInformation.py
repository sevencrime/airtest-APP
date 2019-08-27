#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from airtest.core.api import *

from ElementPage.bankCardInformationPage import bankCardInformationPage
from ElementPage.publicPage import publicPage


@allure.feature("银行卡信息")
class Test_bankCardInformation():

    @allure.story("填写个人资料")
    @pytest.mark.run(order=3)
    def test_bankCard(self, poco):
        pubpage = publicPage(poco)
        bankcard = bankCardInformationPage(poco)
        with allure.step("输入卡号"):
            bankcard.send_bankCardNo()

        with allure.step("输入银行名称"):
            bankcard.send_bankName()

        with allure.step("输入绑定手机号"):
            bankcard.send_bankPhone()

        with allure.step("点击下一步"):
            pubpage.click_NextStepbtn()



if __name__ == "__main__":
    pytest.main(["-s", "test_bankCardInformation.py", '--alluredir', '../report/xml'])






