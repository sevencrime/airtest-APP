#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest

from Commons.GlobalMap import GlobalMap
from Commons.Logging import Logs
from ElementPage.employmentInfomationPage import employmentInfomationPage
from ElementPage.publicTool import publicTool
from airtest.core.api import *

@allure.feature("就业及财务状况")
@pytest.mark.usefixtures('get_totalAnnual_AND_customerNetAssetValue')
# @pytest.mark.usefixtures('reloadRoute')
class Test_employmentInfomation():

    gm = GlobalMap()
    log = Logs()

    @publicTool.reloadRoute("就业及财务状况")
    @allure.story("就业情况选择'无业', 全年总收入选择'小于20万', 资产净值选择'小于100万', 点击下一步")
    def test_unemployedandnot_01(self, poco):
        pubTool = publicTool(poco)
        employment = employmentInfomationPage(poco)
        with allure.step("就业情况选择无业"):
            employ = employment.click_employment("无业")
            # assert_equal(employ, "无业", "就业情况信息填写有误")

        with allure.step("全年总收入选择小于20万"):
            totalAnnual = employment.click_totalAnnualCustomerRevenueHK("小于20万")
            # assert_equal(totalAnnual, "20-50万", "全年总收入填写有误")

        with allure.step("资产净值选择小于100万"):
            customer = employment.click_customerNetAssetValueHK("小于100万")
            # assert_equal(customer, "300-800万", "资产净值填写有误")

        with allure.step("点击下一步"):
            pubTool.swipe_to_Up()
            pubTool.click_NextStepbtn()

        with allure.step("点击下一步成功, 跳转到'选择交易界面'"):
            assert_equal(pubTool.get_Routetitle(), "选择交易信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))

        with allure.step("点击返回按钮返回账户信息界面"):
            pubTool.backform()
            assert_equal(pubTool.get_Routetitle(), "就业及财务状况", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))


    @allure.story("就业情况选择'无业', 全年总收入选择'20-50万', 资金来源选择[退休金, 投资回报, 租金, 其他], 资产净值选择'小于100万', 点击下一步")
    @pytest.mark.run(order=3)
    def test_unemployedandnot_02(self, poco):
        pubTool = publicTool(poco)
        employment = employmentInfomationPage(poco)
        with allure.step("就业情况选择无业"):
            employ = employment.click_employment("无业")
            # assert_equal(employ, "无业", "就业情况信息填写有误")

        with allure.step("全年总收入选择小于20万"):
            totalAnnual = employment.click_totalAnnualCustomerRevenueHK("20-50万", fundlist=['退休金', '投资回报', '租金', '其他'])
            # assert_equal(totalAnnual, "20-50万", "全年总收入填写有误")

        with allure.step("资产净值选择小于100万"):
            customer = employment.click_customerNetAssetValueHK("小于100万")
            # assert_equal(customer, "300-800万", "资产净值填写有误")

        with allure.step("点击下一步"):
            pubTool.swipe_to_Up()
            pubTool.click_NextStepbtn()

        with allure.step("点击下一步成功, 跳转到'选择交易界面'"):
            self.log.debug(self.gm.get_value("istotalAnnual"), "2222222222222222222222222222222222222222")
            assert_equal(pubTool.get_Routetitle(), "选择交易信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))

        with allure.step("点击返回按钮返回账户信息界面"):
            pubTool.backform()
            assert_equal(pubTool.get_Routetitle(), "就业及财务状况", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))


    @allure.story("就业情况选择'无业', 全年总收入选择'50-100万', 资金来源选择[退休金, 投资回报, 租金, 其他], 资产净值选择'小于100万', 点击下一步")
    @pytest.mark.run(order=3)
    def test_unemployedandnot_03(self, poco):
        pubTool = publicTool(poco)
        employment = employmentInfomationPage(poco)
        with allure.step("就业情况选择无业"):
            employ = employment.click_employment("无业")
            # assert_equal(employ, "无业", "就业情况信息填写有误")

        with allure.step("全年总收入选择小于20万"):
            totalAnnual = employment.click_totalAnnualCustomerRevenueHK("50-100万", fundlist=['退休金', '投资回报', '租金', '其他'])
            # assert_equal(totalAnnual, "20-50万", "全年总收入填写有误")

        with allure.step("资产净值选择小于100万"):
            customer = employment.click_customerNetAssetValueHK("小于100万")
            # assert_equal(customer, "300-800万", "资产净值填写有误")

        with allure.step("点击下一步"):
            pubTool.swipe_to_Up()
            pubTool.click_NextStepbtn()

        with allure.step("点击下一步成功, 跳转到'选择交易界面'"):
            assert_equal(pubTool.get_Routetitle(), "选择交易信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))

        with allure.step("点击返回按钮返回账户信息界面"):
            pubTool.backform()
            assert_equal(pubTool.get_Routetitle(), "就业及财务状况", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))


    @allure.story("就业情况选择'无业', 全年总收入选择'大于100万', 资金来源选择[退休金, 投资回报, 租金, 其他], 资产净值选择'小于100万', 点击下一步")
    @pytest.mark.run(order=3)
    def test_unemployedandnot_04(self, poco):
        pubTool = publicTool(poco)
        employment = employmentInfomationPage(poco)
        with allure.step("就业情况选择无业"):
            employ = employment.click_employment("无业")
            # assert_equal(employ, "无业", "就业情况信息填写有误")

        with allure.step("全年总收入选择小于20万"):
            totalAnnual = employment.click_totalAnnualCustomerRevenueHK("大于100万", fundlist=['退休金', '投资回报', '租金', '其他'])
            # assert_equal(totalAnnual, "20-50万", "全年总收入填写有误")

        with allure.step("资产净值选择小于100万"):
            customer = employment.click_customerNetAssetValueHK("小于100万")
            # assert_equal(customer, "300-800万", "资产净值填写有误")

        with allure.step("点击下一步"):
            pubTool.swipe_to_Up()
            pubTool.click_NextStepbtn()

        with allure.step("点击下一步成功, 跳转到'选择交易界面'"):
            assert_equal(pubTool.get_Routetitle(), "选择交易信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))

        with allure.step("点击返回按钮返回账户信息界面"):
            pubTool.backform()
            assert_equal(pubTool.get_Routetitle(), "就业及财务状况", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))



if __name__ == "__main__":
    pytest.main(["-s", "-v", "--pdb", "test_08_employmentInfomation.py::Test_employmentInfomation::test_unemployedandnot_01", '--alluredir', '../report/xml'])






