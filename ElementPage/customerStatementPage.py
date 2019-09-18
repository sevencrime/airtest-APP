#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView


class customerStatementPage(BaseView):
    """
    # 客户声明
    """

    def click_CustomerStatement01(self):
        # 本人已详细阅读、确认、同意、接受及明白《共同汇报标准声明》
        context = "本人已详细阅读、确认、同意、接受及明白《共同汇报标准声明》"
        self.isElementCheck(context).click()


    def click_CustomerStatement02(self):
        # 本人已详细阅读、确认、同意、接受及明白《客户声明》
        context = "本人已详细阅读、确认、同意、接受及明白《客户声明》"
        self.isElementCheck(context).click()

    def click_CustomerStatement03(self):
        # 本人已详细阅读、确认、同意、接受及明白《私隐政策声明》
        context = "本人已详细阅读、确认、同意、接受及明白《私隐政策声明》"
        self.isElementCheck(context).click()

    def click_CustomerStatement04(self):
        # 本人已详细阅读、确认、同意、接受及明白《风险披露声明》
        context = "本人已详细阅读、确认、同意、接受及明白《风险披露声明》"
        self.isElementCheck(context).click()

    def click_CustomerStatement05(self):
        # 本人已详细阅读、确认、同意、接受及明白《常设授权》
        context = "本人已详细阅读、确认、同意、接受及明白《常设授权》"
        self.isElementCheck(context).click()

    def click_CustomerStatement06(self):
        # 本人已详细阅读、确认、同意、接受及明白开立交易账户之《业务条款及细则》
        context = "本人已详细阅读、确认、同意、接受及明白开立交易账户之《业务条款及细则》"
        self.isElementCheck(context).click()



