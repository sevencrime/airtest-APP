#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest

from ElementPage.employmentInfomationPage import employmentInfomationPage
from ElementPage.publicTool import publicTool
from airtest.core.api import *

@allure.feature("就业信息")
class Test_employmentInfomation():

    @allure.story("填写就业信息")
    @pytest.mark.run(order=3)
    def test_unemployedandnot(self, poco):
        pubTool = publicTool(poco)
        employment = employmentInfomationPage(poco)
        with allure.step("就业情况选择无业"):
            employ = employment.click_employment("无业")
            # assert_equal(employ, "无业", "就业情况信息填写有误")

        with allure.step("全年总收入选择小于20万"):
            totalAnnual = employment.click_totalAnnualCustomerRevenueHK("20-50万", funds=["退休金", "储蓄"])
            # assert_equal(totalAnnual, "20-50万", "全年总收入填写有误")

        with allure.step("资产净值选择小于100万"):
            customer = employment.click_customerNetAssetValueHK("300-800万", assets=["退休金", "储蓄"])
            # assert_equal(customer, "300-800万", "资产净值填写有误")

        with allure.step("点击下一步"):
            pubTool.swipe_to_Up()
            pubTool.click_NextStepbtn()


if __name__ == "__main__":
    pytest.main(["-s", "test_08_employmentInfomation.py", '--alluredir', '../report/xml'])






