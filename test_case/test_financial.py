#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest

from ElementPage.financialPage import financialPage
from ElementPage.publicPage import publicPage

@allure.feature("相关保证金融资账户")
class Test_financial():

    @allure.story("相关保证金融资账户")
    @pytest.mark.run(order=3)
    def test_derivative(self, poco):
        pubpage = publicPage(poco)
        financial = financialPage(poco)
        with allure.step("您是否是账户的最终实益拥有人? "):
            financial.click_accountHolder(True)

        with allure.step("您是否是最终负责下单的人?? "):
            financial.click_orderPerson(True)

        with allure.step("点击下一步"):
            pubpage.click_NextStepbtn()


if __name__ == "__main__":
    pytest.main(["-s", "test_financial.py", '--alluredir', '../report/xml'])






