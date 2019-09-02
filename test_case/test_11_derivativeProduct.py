#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest

from ElementPage.derivativeProductPage import derivativeProductPage
from ElementPage.publicTool import publicTool

@allure.feature("就业信息")
class Test_derivativeProduct():

    @allure.story("填写衍生产品的认识")
    @pytest.mark.run(order=3)
    def test_derivative(self, poco):
        pubtool = publicTool(poco)
        derivative = derivativeProductPage(poco)
        with allure.step("客户是否曾接受有关衍生产品性质和风险的一般知识培训或修读相关课程"):
            derivative.click_derivativeCourse(True)

        with allure.step("您是否从现在或过去拥有过与衍生产品有关的工作经验？"):
            derivative.click_derivativeJobs(True)

        with allure.step("您是否在过去3年曾执行5次或以上有关衍生产品的交易，例如：衍生证券、牛熊市、股票期权、期货与期权、商品、结构性产品及交易所买卖基金等"):
            # import pdb; pdb.set_trace()
            derivative.click_tradingFund(True)

        with allure.step("客户是否申请开通买卖衍生权证、牛熊证及结构性等产品"):
            derivative.click_buyProduct(True)

        with allure.step("客户已明白买卖衍生权证、牛熊证及结构性产品的风险。并已详细阅读「结构性产品相关风险声明披露」"):
            derivative.click_riskStatement()

        with allure.step("点击下一步"):
            pubtool.click_NextStepbtn()


if __name__ == "__main__":
    pytest.main(["-s", "test_11_derivativeProduct.py", '--alluredir', '../report/xml'])






