#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import sys

import allure
import pytest

from Commons import CommonsTool
from Commons.GlobalMap import GlobalMap
from Commons.Logging import Logs
from ElementPage.employmentInfomationPage import employmentInfomationPage
from ElementPage.publicTool import publicTool
from airtest.core.api import *

@pytest.mark.usefixtures('query_initialData')
@allure.feature("就业及财务状况")
class Test_employmentInfomation():

    gm = GlobalMap()
    log = Logs()

    fix_routetitle = ["就业及财务状况"]      #当fixture的参数


    # 无业--全年总收入
    Unemployed_totalAnnual = [
        ("小于20万", []),
        ("20-50万", ['退休金', '投资回报', '租金', '其他']),
        ("50-100万", ['退休金', '投资回报', '租金', '其他']),
        ("大于100万", ['退休金', '投资回报', '租金', '其他']),
    ]

    # 无业--资产净值
    Unemployed_assetslist = [
        ("小于100万", []),
        ("100-300万", ["退休金", "物业投资", "车辆投资", "储蓄", "股票/债券投资", "遗产", "其他"]),
        ("300-800万", ["退休金", "物业投资", "车辆投资", "储蓄", "股票/债券投资", "遗产", "其他"]),
        ("大于800万", ["退休金", "物业投资", "车辆投资", "储蓄", "股票/债券投资", "遗产", "其他"]),
    ]

    # 就业--全年总收入
    Employed_totalAnnual = [
        ("小于20万", []),
        ("20-50万", []),
        ("50-100万", []),
        ("大于100万", ['薪金', '投资回报', '租金', '佣金', '其他']),
    ]

    # 就业--资产净值
    Employed_assetslist = [
        ("小于100万", []),
        ("100-300万", []),
        ("300-800万", ["薪金", "物业投资", "车辆投资", "储蓄", "股票/债券投资", "遗产", "其他"]),
        ("大于800万", ["薪金", "物业投资", "车辆投资", "储蓄", "股票/债券投资", "遗产", "其他"]),
    ]


    # 自雇--全年总收入
    selfEmployed_totalAnnual = [
        ("小于20万", []),
        ("20-50万", ["自营业务收益", "投资回报", "租金", "其他"]),
        ("50-100万", ["自营业务收益", "投资回报", "租金", "其他"]),
        ("大于100万", ["自营业务收益", "投资回报", "租金", "其他"]),
    ]

    # 自雇--资产净值
    selfEmployed_assetslist = [
        ("小于100万", []),
        ("100-300万", ["薪金", "自营业务收益", "物业投资", "储蓄", "股票/债券投资", "车辆投资", "遗产", "其他"]),
        ("300-800万", ["薪金", "自营业务收益", "物业投资", "储蓄", "股票/债券投资", "车辆投资", "遗产", "其他"]),
        ("大于800万", ["薪金", "自营业务收益", "物业投资", "储蓄", "股票/债券投资", "车辆投资", "遗产", "其他"]),
    ]

    # @CommonsTool.retry()
    @allure.step("用例标题: 不选择就业情况, 直接选择全年总收入和资产净值")
    @allure.title("全年总收入选择: {totalAnnual}, 资产净值全栈: {customer}")
    @pytest.mark.parametrize('totalAnnual', ['小于20万', '20-50万', '50-100万', '大于100万'])
    @pytest.mark.parametrize('customer', ['小于100万', '100-300万', '300-800万', '大于800万'])
    @pytest.mark.skipif(gm.get_value("Routetitle") == "选择交易信息", reason= "就业情况已有值, 跳过该用例")
    @pytest.mark.usefixtures('reloadRoute')
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_nullemploy(self, poco, totalAnnual, customer):
        self.log.debug("正在执行用例 {} ".format(sys._getframe().f_code.co_name, ))
        pubTool = publicTool(poco)
        employment = employmentInfomationPage(poco)
        with allure.step("选择全年总收入选择 {}".format(totalAnnual)):
            employment.click_totalAnnualCustomerRevenueHK(totalAnnual)

        with allure.step("资产净值选择 {}".format(customer)):
            employment.click_customerNetAssetValueHK(customer)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()
            assert_equal(pubTool.get_Routetitle(), "就业及财务状况", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))



    @allure.step("用例标题: 就业情况选择: {employed}, 全年总收入选择: {totalAnnual}, 资金来源选择: {fundlist}, 资产净值选择: {customer}, 资产净值来源选择: {assetslist}")
    @pytest.mark.parametrize("employed", ["无业"])
    @pytest.mark.parametrize("totalAnnual, fundlist", Unemployed_totalAnnual)
    @pytest.mark.parametrize("customer, assetslist", Unemployed_assetslist)
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_unemployedandnot(self, poco, reloadRoute, employed, totalAnnual, fundlist, customer, assetslist):
        self.log.debug("正在执行用例 {} ".format(sys._getframe().f_code.co_name, ))
        pubTool = publicTool(poco)
        employment = employmentInfomationPage(poco)
        with allure.step("就业情况选择无业"):
            employ = employment.click_employment(employed)

        with allure.step("全年总收入选择{}".format(totalAnnual)):
            totalAnnual = employment.click_totalAnnualCustomerRevenueHK(totalAnnual, fundlist=fundlist)

        with allure.step("资产净值选择{}".format(customer)):
            customer = employment.click_customerNetAssetValueHK(customer, assetslist = assetslist)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("点击下一步成功, 跳转到'选择交易界面'"):
            self.log.debug("{}".format(self.gm.get_value("istotalAnnual"), ))
            assert_equal(pubTool.get_Routetitle(), "选择交易信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))

        with allure.step("点击返回按钮返回账户信息界面"):
            pubTool.backform()
            assert_equal(pubTool.get_Routetitle(), "就业及财务状况", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))


    @allure.step("用例标题: 就业情况选择: {employed}, 全年总收入选择: {totalAnnual}, 资金来源选择: {fundlist}, 资产净值选择: {customer}, 资产净值来源选择: {assetslist}")
    @pytest.mark.parametrize("employed", ["就业"])
    @pytest.mark.parametrize("totalAnnual, fundlist", Employed_totalAnnual)
    @pytest.mark.parametrize("customer, assetslist", Employed_assetslist)
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_Employed(self, poco, reloadRoute, employed, totalAnnual, fundlist, customer, assetslist):
        self.log.debug("正在执行用例 {} ".format(sys._getframe().f_code.co_name, ))
        pubTool = publicTool(poco)
        employment = employmentInfomationPage(poco)
        with allure.step("就业情况选择就业"):
            employ = employment.click_employment(employed)

        with allure.step("输入办公室地址"):
            employaddr = employment.send_officeAddr()

        with allure.step("全年总收入选择{}".format(totalAnnual)):
            totalAnnual = employment.click_totalAnnualCustomerRevenueHK(totalAnnual, fundlist=fundlist)

        with allure.step("资产净值选择{}".format(customer)):
            customer = employment.click_customerNetAssetValueHK(customer, assetslist = assetslist)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("校验就业地址弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "请确认您的办公室地址", "办公室地址弹框标题有误")
            assert_equal(boxcontent, employaddr, "办公室地址弹框内容与填写的地址不一致")

        with allure.step("确认地址弹框--点击确定"):
            pubTool.click_boxconfirm()

        with allure.step("点击下一步成功, 跳转到'选择交易界面'"):
            self.log.debug("{}".format(self.gm.get_value("istotalAnnual"), ))
            assert_equal(pubTool.get_Routetitle(), "选择交易信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))

        with allure.step("点击返回按钮返回账户信息界面"):
            pubTool.backform()
            assert_equal(pubTool.get_Routetitle(), "就业及财务状况", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))



    @allure.step("用例标题: 就业情况选择: {employed}, 全年总收入选择: {totalAnnual}, 资金来源选择: {fundlist}, 资产净值选择: {customer}, 资产净值来源选择: {assetslist}")
    @pytest.mark.parametrize("employed", ["自雇"])
    @pytest.mark.parametrize("totalAnnual, fundlist", selfEmployed_totalAnnual)
    @pytest.mark.parametrize("customer, assetslist", selfEmployed_assetslist)
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_selfEmployed(self, poco, reloadRoute, employed, totalAnnual, fundlist, customer, assetslist):
        self.log.debug("正在执行用例 {} ".format(sys._getframe().f_code.co_name, ))
        pubTool = publicTool(poco)
        employment = employmentInfomationPage(poco)
        with allure.step("就业情况选择自雇"):
            employ = employment.click_employment(employed)

        with allure.step("输入办公室地址"):
            employaddr = employment.send_officeAddr()

        with allure.step("全年总收入选择{}".format(totalAnnual)):
            totalAnnual = employment.click_totalAnnualCustomerRevenueHK(totalAnnual, fundlist=fundlist)

        with allure.step("资产净值选择{}".format(customer)):
            customer = employment.click_customerNetAssetValueHK(customer, assetslist = assetslist)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("校验就业地址弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "请确认您的办公室地址", "办公室地址弹框标题有误")
            assert_equal(boxcontent, employaddr, "办公室地址弹框内容与填写的地址不一致")

        with allure.step("确认地址弹框--点击确定"):
            pubTool.click_boxconfirm()

        with allure.step("点击下一步成功, 跳转到'选择交易界面'"):
            self.log.debug("{}".format(self.gm.get_value("istotalAnnual"), ))
            assert_equal(pubTool.get_Routetitle(), "选择交易信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))

        with allure.step("点击返回按钮返回账户信息界面"):
            pubTool.backform()
            assert_equal(pubTool.get_Routetitle(), "就业及财务状况", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))




if __name__ == "__main__":
    pytest.main(["-s", "-v",  "test_08_employmentInfomation.py::Test_employmentInfomation", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()





