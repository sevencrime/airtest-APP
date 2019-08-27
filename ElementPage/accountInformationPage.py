#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView


class accountInformationPage(BaseView):
    """
    账户信息

    """
    def click_securitiesCash(self):
        self.exists(self.el_securitiesCash).click()

    def click_securitiesMargin(self):
        self.exists(self.el_securitiesMargin).click()

    def click_futuresMargin(self):
        self.exists(self.el_futuresMargin).click()

