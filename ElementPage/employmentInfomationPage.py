#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView


class employmentInfomationPage(BaseView):
    """
    # 就业情况
    """
    def click_employment(self, employ):
        """
        # 选择就业情况信息

        args:
            employ:下拉框的值(string)  可选值['就业', '自雇', '无业]
        """
        employment = self.exists(self.el_employ)
        # 判断employ是否与当前选中的一致
        if employ != employment.get_text():
            # 点击就业情况下拉框
            employment.click()
            # 下拉框选值:employ
            self.poco(employ).click()

        return employment.get_text()


    def click_totalAnnualCustomerRevenueHK(self, price, funds=None):
        """
        # 全年总收入

        args:
            price: 资金区间(string)
            funds:  list类型, 资金来源需要勾选的字段
        """
        totalAnnual = self.exists(self.totalAnnualCustomerRevenueHK)
        # 判断employ是否与当前选中的一致
        if price != totalAnnual.get_text():
            totalAnnual.click()
            self.poco(text=price).click()

        # 判断 "请注明资金来源(可多选)" 复选框是否触发
        if self.exists(self.sourcesfunds):
            # 遍历需要点击的选项
            for fund in funds:
                sources = self.exists(self.poco(text=fund))
                # 判断资金来源和资产净值是否同时出现
                if len(sources) == 1:
                    sources.click()
                elif len(sources) > 1:
                    sources[0].click()
                else:
                    print("出现了不止2个, 需要查看问题哦")
                    pass

        return totalAnnual.get_text()


    def click_customerNetAssetValueHK(self, price, assets=None):
        """
        # 资产净值

        args:
            price: 资金区间(string)
            assets:  list类型, 资产净值需要勾选的字段
        """
        customer = self.exists(self.customerNetAssetValueHK)
        # 判断employ是否与当前选中的一致
        if price != customer.get_text():
            customer.click()
            self.poco(text=price).click()

        # 判断 "请注明资金来源(可多选)" 复选框是否触发
        if self.exists(self.assetsvalue):
            # 遍历需要点击的选项
            for asset in assets:
                sources = self.exists(self.poco(text=asset))
                # 判断资金来源和资产净值是否同时出现
                if len(sources) == 1:
                    sources.click()
                elif len(sources) > 1:
                    sources[1].click()
                else:
                    print("出现了不止2个, 需要查看问题哦")
                    pass

        return customer.get_text()



