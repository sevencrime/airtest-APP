#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView


class financialPage(BaseView):
    """
    # 香港保证金融资账户
    """

    def click_accountHolder(self, isFlag):
        """
        # 您是否是账户的最终实益拥有人?
        """
        context = "您是否是账户的最终实益拥有人?"
        self.isElementRadio(context, isFlag).click()


    def click_orderPerson(self, isFlag):
        """
        # 您是否是最终负责下单的人?
        """
        context = "您是否是最终负责下单的人?"
        self.isElementRadio(context, isFlag).click()