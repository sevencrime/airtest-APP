#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import allure
import pytest

from Commons import CommonsTool
from ElementPage.derivativeProductPage import derivativeProductPage
from ElementPage.publicTool import publicTool
from airtest.core.api import *
from Commons.GlobalMap import GlobalMap


@allure.feature("衍生产品的认识")
@pytest.mark.usefixtures('query_initialData')
class Test_derivativeProduct():

    gm = GlobalMap()
    fix_routetitle = ["衍生品产品认识"]
    radiovalue = [True, False]

    @allure.story("衍生品产品认识 >> 直接勾选最后一个")
    @pytest.mark.parametrize("buyProduct", radiovalue)
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    @pytest.mark.usefixtures('query_initialData')
    @pytest.mark.skipif(gm.get_value("derivative") == True, reason="衍生产品选项已经勾选")
    def test_derivative_Reversed(self, poco, reloadRoute, buyProduct):
        pubTool = publicTool(poco)
        derivative = derivativeProductPage(poco)

        with allure.step("客户是否申请开通买卖衍生权证、牛熊证及结构性等产品"):
            derivative.click_buyProduct(buyProduct)

        if buyProduct:
            with allure.step("客户已明白买卖衍生权证、牛熊证及结构性产品的风险。并已详细阅读「结构性产品相关风险声明披露」"):
                derivative.click_riskStatement()

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()
            assert_equal(pubTool.get_Routetitle(), "衍生品产品认识", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))


    @allure.story("衍生品产品认识 >> 结构性产品相关风险声明披露不勾选")
    @pytest.mark.parametrize("derivativeCourse", radiovalue)
    @pytest.mark.parametrize("derivativeJobs", radiovalue)
    @pytest.mark.parametrize("tradingFund", radiovalue)
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_derivative_nullriskStatement(self, poco, reloadRoute, derivativeCourse, derivativeJobs, tradingFund):
        pubTool = publicTool(poco)
        derivative = derivativeProductPage(poco)
        with allure.step("客户是否曾接受有关衍生产品性质和风险的一般知识培训或修读相关课程"):
            derivative.click_derivativeCourse(derivativeCourse)

        with allure.step("您是否从现在或过去拥有过与衍生产品有关的工作经验？"):
            derivative.click_derivativeJobs(derivativeJobs)

        with allure.step("您是否在过去3年曾执行5次或以上有关衍生产品的交易，例如：衍生证券、牛熊市、股票期权、期货与期权、商品、结构性产品及交易所买卖基金等"):
            derivative.click_tradingFund(tradingFund)

        with allure.step("客户是否申请开通买卖衍生权证、牛熊证及结构性等产品"):
            derivative.click_buyProduct(True)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()
            assert_equal(pubTool.get_Routetitle(), "衍生品产品认识", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))

    @allure.story("衍生品产品认识 >> 组合勾选")
    @allure.title("derivativeCourse: {derivativeCourse}, derivativeJobs: {derivativeJobs}, tradingFund : {tradingFund}, buyProduct : {buyProduct}")
    @pytest.mark.parametrize("derivativeCourse", radiovalue)
    @pytest.mark.parametrize("derivativeJobs", radiovalue)
    @pytest.mark.parametrize("tradingFund", radiovalue)
    @pytest.mark.parametrize("buyProduct", radiovalue)
    @pytest.mark.usefixtures('query_initialData')
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_derivative(self, poco, reloadRoute, derivativeCourse, derivativeJobs, tradingFund, buyProduct):
        pubTool = publicTool(poco)
        derivative = derivativeProductPage(poco)
        with allure.step("客户是否曾接受有关衍生产品性质和风险的一般知识培训或修读相关课程"):
            derivative.click_derivativeCourse(derivativeCourse)

        with allure.step("您是否从现在或过去拥有过与衍生产品有关的工作经验？"):
            derivative.click_derivativeJobs(derivativeJobs)

        with allure.step("您是否在过去3年曾执行5次或以上有关衍生产品的交易，例如：衍生证券、牛熊市、股票期权、期货与期权、商品、结构性产品及交易所买卖基金等"):
            derivative.click_tradingFund(tradingFund)

        with allure.step("客户是否申请开通买卖衍生权证、牛熊证及结构性等产品"):
            derivative.click_buyProduct(buyProduct)

        # 当"开通衍生权证"时, 触发隐藏框
        if buyProduct:
            with allure.step("客户已明白买卖衍生权证、牛熊证及结构性产品的风险。并已详细阅读「结构性产品相关风险声明披露」"):
                derivative.click_riskStatement()
        else:
            self.gm.set_bool(knowRisk=False)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()
            assert_equal(pubTool.get_Routetitle(), "相关保证金融资账户", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))




if __name__ == "__main__":
    pytest.main(["-s", "-v", "test_11_derivativeProduct.py::Test_derivativeProduct::test_demo", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()





