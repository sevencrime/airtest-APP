#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from Commons.BaseView import BaseView


class accountInformationPage(BaseView):
    """
    账户信息

    """
    # gm = GlobalMap()

    def get_leverMargin(self):
        # try:
        #     self.poco(text="杠杆式外汇账户(保证金)").get_text()
        #     # assert acctext.strip() == "杠杆式外汇账户(保证金)"
        # # except AssertionError:
        # #     raise AssertionError
        # except PocoNoSuchNodeException:
        #     self.gm.set_value(isLeveraged=False)
        # else:
        #     self.gm.set_value(isLeveraged=True)   	

        start = time.time()
        while not self.poco(text="杠杆式外汇账户(保证金)").exists():
            self.poco(text="杠杆式外汇账户(保证金)").invalidate()
            if time.time() - start > 3:
                self.gm.set_value(isLeveraged=False)
                break
        else:
            self.gm.set_value(isLeveraged=True)  


    def get_bullionMargin(self):
        # try:
        #     self.poco(text="艾德金业现货黄金账户(保证金)").get_text()
        # except PocoNoSuchNodeException:
        #     self.gm.set_value(isbullion=False)
        # else:
        #     self.gm.set_value(isbullion=True)

        start = time.time()
        while not self.poco(text="艾德金业现货黄金账户(保证金)").exists():
            self.poco(text="艾德金业现货黄金账户(保证金)").invalidate()
            if time.time() - start > 3:
                self.gm.set_value(isLeveraged=False)
                break
        else:
            self.gm.set_value(isLeveraged=True)  


    # 证券现金
    def click_securitiesCash(self):
        # 查询数据库, 通过值判断是否勾选
        if "securitiesCash" not in self.gm.get_value("accountType"):
            self.exists(self.el_securitiesCash).click()


    # 证券保证金
    def click_securitiesMargin(self):
        if "securitiesMargin" not in self.gm.get_value("accountType"):
            self.exists(self.el_securitiesMargin).click()

    # 期货
    def click_futuresMargin(self):
        if "futuresMargin" not in self.gm.get_value("accountType"):
            self.exists(self.el_futuresMargin).click()

