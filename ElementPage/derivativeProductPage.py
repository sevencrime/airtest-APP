#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView


class derivativeProductPage(BaseView):
    """
    # 衍生产品的认识
    """

    def click_derivativeCourse(self, isFlag):
        # 客户是否曾接受有关衍生产品性质和风险的一般知识培训或修读相关课程
        context = "您是否曾接受有关衍生产品性质和风险的一般知识培训或修读相关课程？"
        self.isElementRadio(context, isFlag).click()

    def click_derivativeJobs(self, isFlag):
        # 客户是否从现时或过去拥有与衍生产品有关的工作经验?
        context = "您是否从现在或过去拥有过与衍生产品有关的工作经验？"
        self.isElementRadio(context, isFlag).click()

    def click_tradingFund(self, isFlag):
        # 您是否在过去3年曾执行5次或以上有关衍生产品的交易，例如：衍生证券、牛熊市、股票期权、期货与期权、商品、结构性产品及交易所买卖基金等
        context="您是否在过去3年曾执行5次或以上有关衍生产品的交易，例如：衍生证券、牛熊市、股票期权、期货与期权、商品、结构性产品及交易所买卖基金等？"
        self.isElementRadio(context, isFlag).click()

    def click_buyProduct(self, isFlag):
        # 客户是否申请开通买卖衍生权证、牛熊证及结构性等产品
        context = "客户是否申请开通买卖衍生权证、牛熊证及结构性等产品？"
        self.isElementRadio(context, isFlag).click()

    def click_riskStatement(self):
        # 客户是否已明白买卖衍生权证，牛熊证及结构性产品的风险。并已详细阅读「结构性产品相关风险声明披露」
        context = "客户已明白买卖衍生权证、牛熊证及结构性产品的风险。并已详细阅读「结构性产品相关风险声明披露」"
        if not self.gm.get_value("knowRisk"):
            self.isElementCheck(context).click()
            self.gm.set_bool(knowRisk=True)

