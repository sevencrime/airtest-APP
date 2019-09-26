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
class Test_employmentInfomation():

    gm = GlobalMap()
    log = Logs()

    fix_routetitle = ["就业及财务状况"]      #当fixture的参数



    fix_totalAnnual = [
        ("小于20万", []),
        ("20-50万", ['退休金', '投资回报', '租金', '其他']),
        ("50-100万", ['退休金', '投资回报', '租金', '其他']),
        ("大于100万", ['退休金', '投资回报', '租金', '其他']),
    ]

    fix_assetslist = [
        ("小于100万", []),
        ("100-300万", ["退休金", "物业投资", "车辆投资", "储蓄", "股票/债券投资", "遗产", "其他"]),
        ("300-800万", ["退休金", "物业投资", "车辆投资", "储蓄", "股票/债券投资", "遗产", "其他"]),
        ("大于800万", ["退休金", "物业投资", "车辆投资", "储蓄", "股票/债券投资", "遗产", "其他"]),
    ]

    @allure.step("用例标题: 就业情况选择: {employed}, 全年总收入选择: {totalAnnual}, 资金来源选择: {fundlist}, 资产净值选择: {customer}, 资产净值来源选择: {assetslist}")
    @pytest.mark.parametrize("employed", ["无业"])
    @pytest.mark.parametrize("totalAnnual, fundlist", fix_totalAnnual)
    @pytest.mark.parametrize("customer, assetslist", fix_assetslist)
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_unemployedandnot_02(self, poco, reloadRoute, employed, totalAnnual, fundlist, customer, assetslist):
        pubTool = publicTool(poco)
        employment = employmentInfomationPage(poco)
        with allure.step("就业情况选择无业"):
            employ = employment.click_employment(employed)
            # assert_equal(employ, "无业", "就业情况信息填写有误")

        with allure.step("全年总收入选择小于20万"):
            totalAnnual = employment.click_totalAnnualCustomerRevenueHK(totalAnnual, fundlist=fundlist)
            # assert_equal(totalAnnual, "20-50万", "全年总收入填写有误")

        with allure.step("资产净值选择小于100万"):
            customer = employment.click_customerNetAssetValueHK(customer, assetslist = assetslist)
            # assert_equal(customer, "300-800万", "资产净值填写有误")

        with allure.step("点击下一步"):
            pubTool.swipe_to_Up()
            pubTool.click_NextStepbtn()

        with allure.step("点击下一步成功, 跳转到'选择交易界面'"):
            self.log.debug("".join(self.gm.get_value("istotalAnnual")), "2222222222222222222222222222222222222222")
            assert_equal(pubTool.get_Routetitle(), "选择交易信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))

        with allure.step("点击返回按钮返回账户信息界面"):
            pubTool.backform()
            assert_equal(pubTool.get_Routetitle(), "就业及财务状况", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))



    # @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    # @allure.story("就业情况选择'无业', 全年总收入选择'小于20万', 资产净值选择'小于100万', 点击下一步")
    # def test_unemployedandnot_01(self, poco, reloadRoute):
    #     pubTool = publicTool(poco)
    #     employment = employmentInfomationPage(poco)
    #     with allure.step("就业情况选择无业"):
    #         employ = employment.click_employment("无业")
    #         # assert_equal(employ, "无业", "就业情况信息填写有误")
    #
    #     with allure.step("全年总收入选择小于20万"):
    #         totalAnnual = employment.click_totalAnnualCustomerRevenueHK("小于20万")
    #         # assert_equal(totalAnnual, "20-50万", "全年总收入填写有误")
    #
    #     with allure.step("资产净值选择小于100万"):
    #         customer = employment.click_customerNetAssetValueHK("小于100万")
    #         # assert_equal(customer, "300-800万", "资产净值填写有误")
    #
    #     with allure.step("点击下一步"):
    #         pubTool.swipe_to_Up()
    #         pubTool.click_NextStepbtn()
    #
    #     with allure.step("点击下一步成功, 跳转到'选择交易界面'"):
    #         assert_equal(pubTool.get_Routetitle(), "选择交易信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))
    #
    #     with allure.step("点击返回按钮返回账户信息界面"):
    #         pubTool.backform()
    #         assert_equal(pubTool.get_Routetitle(), "就业及财务状况", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))

    #
    # @allure.story("就业情况选择'无业', 全年总收入选择'20-50万', 资金来源选择[退休金, 投资回报, 租金, 其他], 资产净值选择'小于100万', 点击下一步")
    # @pytest.mark.run(order=3)
    # def test_unemployedandnot_02(self, poco):
    #     pubTool = publicTool(poco)
    #     employment = employmentInfomationPage(poco)
    #     with allure.step("就业情况选择无业"):
    #         employ = employment.click_employment("无业")
    #         # assert_equal(employ, "无业", "就业情况信息填写有误")
    #
    #     with allure.step("全年总收入选择小于20万"):
    #         totalAnnual = employment.click_totalAnnualCustomerRevenueHK("20-50万", fundlist=['退休金', '投资回报', '租金', '其他'])
    #         # assert_equal(totalAnnual, "20-50万", "全年总收入填写有误")
    #
    #     with allure.step("资产净值选择小于100万"):
    #         customer = employment.click_customerNetAssetValueHK("小于100万")
    #         # assert_equal(customer, "300-800万", "资产净值填写有误")
    #
    #     with allure.step("点击下一步"):
    #         pubTool.swipe_to_Up()
    #         pubTool.click_NextStepbtn()
    #
    #     with allure.step("点击下一步成功, 跳转到'选择交易界面'"):
    #         self.log.debug(self.gm.get_value("istotalAnnual"), "2222222222222222222222222222222222222222")
    #         assert_equal(pubTool.get_Routetitle(), "选择交易信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))
    #
    #     with allure.step("点击返回按钮返回账户信息界面"):
    #         pubTool.backform()
    #         assert_equal(pubTool.get_Routetitle(), "就业及财务状况", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))
    #
    #
    # @allure.story("就业情况选择'无业', 全年总收入选择'50-100万', 资金来源选择[退休金, 投资回报, 租金, 其他], 资产净值选择'小于100万', 点击下一步")
    # @pytest.mark.run(order=3)
    # def test_unemployedandnot_03(self, poco):
    #     pubTool = publicTool(poco)
    #     employment = employmentInfomationPage(poco)
    #     with allure.step("就业情况选择无业"):
    #         employ = employment.click_employment("无业")
    #         # assert_equal(employ, "无业", "就业情况信息填写有误")
    #
    #     with allure.step("全年总收入选择小于20万"):
    #         totalAnnual = employment.click_totalAnnualCustomerRevenueHK("50-100万", fundlist=['退休金', '投资回报', '租金', '其他'])
    #         # assert_equal(totalAnnual, "20-50万", "全年总收入填写有误")
    #
    #     with allure.step("资产净值选择小于100万"):
    #         customer = employment.click_customerNetAssetValueHK("小于100万")
    #         # assert_equal(customer, "300-800万", "资产净值填写有误")
    #
    #     with allure.step("点击下一步"):
    #         pubTool.swipe_to_Up()
    #         pubTool.click_NextStepbtn()
    #
    #     with allure.step("点击下一步成功, 跳转到'选择交易界面'"):
    #         assert_equal(pubTool.get_Routetitle(), "选择交易信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))
    #
    #     with allure.step("点击返回按钮返回账户信息界面"):
    #         pubTool.backform()
    #         assert_equal(pubTool.get_Routetitle(), "就业及财务状况", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))
    #
    #
    # @allure.story("就业情况选择'无业', 全年总收入选择'大于100万', 资金来源选择[退休金, 投资回报, 租金, 其他], 资产净值选择'小于100万', 点击下一步")
    # @pytest.mark.run(order=3)
    # def test_unemployedandnot_04(self, poco):
    #     pubTool = publicTool(poco)
    #     employment = employmentInfomationPage(poco)
    #     with allure.step("就业情况选择无业"):
    #         employ = employment.click_employment("无业")
    #         # assert_equal(employ, "无业", "就业情况信息填写有误")
    #
    #     with allure.step("全年总收入选择小于20万"):
    #         totalAnnual = employment.click_totalAnnualCustomerRevenueHK("大于100万", fundlist=['退休金', '投资回报', '租金', '其他'])
    #         # assert_equal(totalAnnual, "20-50万", "全年总收入填写有误")
    #
    #     with allure.step("资产净值选择小于100万"):
    #         customer = employment.click_customerNetAssetValueHK("小于100万")
    #         # assert_equal(customer, "300-800万", "资产净值填写有误")
    #
    #     with allure.step("点击下一步"):
    #         pubTool.swipe_to_Up()
    #         pubTool.click_NextStepbtn()
    #
    #     with allure.step("点击下一步成功, 跳转到'选择交易界面'"):
    #         assert_equal(pubTool.get_Routetitle(), "选择交易信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))
    #
    #     with allure.step("点击返回按钮返回账户信息界面"):
    #         pubTool.backform()
    #         assert_equal(pubTool.get_Routetitle(), "就业及财务状况", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))
    #



if __name__ == "__main__":
    pytest.main(["-s", "-v", "test_08_employmentInfomation.py::Test_employmentInfomation::test_unemployedandnot_02", '--alluredir', '../report/xml'])






