#!/usr/bin/env python
# -*- coding: utf-8 -*-
from poco.exceptions import PocoNoSuchNodeException

from Commons.BaseView import BaseView
from Commons.GlobalMap import GlobalMap


class accountInformationPage(BaseView):
    """
    账户信息

    """
    gm = GlobalMap()

    def get_leverMargin(self):
        try:
            self.poco(text="杠杆式外汇账户(保证金)").get_text()
        except PocoNoSuchNodeException:
            self.gm.set_value(isLeveraged=False)
        else:
            self.gm.set_value(isLeveraged=True)   	

    def get_bullionMargin(self):
        try:
            self.poco(text="艾德金业现货黄金账户(保证金)").get_text()
        except PocoNoSuchNodeException:
            self.gm.set_value(isbullion=False)
        else:
            self.gm.set_value(isbullion=True)

    def click_securitiesCash(self):
        self.exists(self.el_securitiesCash).click()

    def click_securitiesMargin(self):
        self.exists(self.el_securitiesMargin).click()

    def click_futuresMargin(self):
        self.exists(self.el_futuresMargin).click()

