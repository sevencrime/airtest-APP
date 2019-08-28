#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest

from ElementPage.employmentInfomationPage import employmentInfomationPage
from ElementPage.publicPage import publicPage


@allure.feature("就业信息")
class Test_employmentInfomation():

    @allure.story("填写就业信息")
    @pytest.mark.run(order=3)
    def test_unemployedandnot(self, poco):
        pubpage = publicPage(poco)
        employment = employmentInfomationPage(poco)
        with allure.step("就业情况选择无业"):
            employment.click_employment("无业")

        with allure.step("全年总收入选择小于20万"):
            employment.click_totalAnnualCustomerRevenueHK("小于20万")

        with allure.step("资产净值选择小于100万"):
            employment.click_customerNetAssetValueHK("小于100万")


if __name__ == "__main__":
    pytest.main(["-s", "test_employmentInfomation.py", '--alluredir', '../report/xml'])






