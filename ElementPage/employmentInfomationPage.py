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

        # 获取就业情况栏位的值
        try:
            employtext = employment.get_text()
        except:
            employtext = None

        # 判断employ是否与当前选中的一致
        if employ != employtext:
            # 点击就业情况下拉框
            employment.click()
            # 下拉框选值:employ
            self.poco(text=employ).click()

        # 判断就业情况是否输入就业或自雇
        if employ == "就业" or employ == "自雇":
            # 输入职位信息
            self.position.set_text("工程师")
            # 输入业务性质
            self.BusinessNature.set_text("互联网行业")
            # 公司名称
            self.companyName.set_text("艾德网络科技")

        return self.el_employ.get_text()


    def click_totalAnnualCustomerRevenueHK(self, price, fundlist=[]):
        """
        # 全年总收入

        args:
            price: 资金区间(string)
            fundlist:  list类型, 资金来源需要勾选的字段

        # gm.get_value("istotalAnnual") : 全年总收入来源已勾选的值
        """
        # import pdb; pdb.set_trace()

        funds = set(self.gm.get_value("istotalAnnual")).symmetric_difference(fundlist)
        self.log.debug("需要点击的选项有: {}".format(','.join(funds)))
        totalAnnual = self.exists(self.totalAnnualCustomerRevenueHK)

        try:
            totalAnnualtext = totalAnnual.get_text()
        except:
            totalAnnualtext = None

        # 判断employ是否与当前选中的一致
        if price != totalAnnualtext:
            totalAnnual.click()
            self.poco(text=price).click()

        # 判断 "请注明资金来源(可多选)" 复选框是否触发
        if self.sourcesfunds:
            # 遍历需要点击的选项
            for fund in funds:
                sources = self.exists(self.poco(text=fund))
                # 判断资金来源和资产净值是否同时出现
                if len(sources) == 1:
                    sources.click()
                    if fund == '其他':
                        self.otherfunds.set_text("其他资金来源")

                elif len(sources) > 1:
                    sources[0].click()
                    if fund == '其他':
                        self.otherfunds.set_text("其他资金来源")

                else:
                    print("出现了不止2个, 需要查看问题哦")
                    pass

        # 重新给istotalAnnual赋值, 值为当前勾选的字段
        self.gm.set_List('istotalAnnual', fundlist)
        return self.totalAnnualCustomerRevenueHK.get_text()


    def click_customerNetAssetValueHK(self, price, assetslist=[]):
        """
        # 资产净值

        args:
            price: 资金区间(string)
            assetslist:  list类型, 资产净值需要勾选的字段
        """

        assets = set(self.gm.get_value("customerNetAssetValue")).symmetric_difference(assetslist)
        customer = self.exists(self.customerNetAssetValueHK)

        try:
            customertext = customer.get_text()
        except:
            customertext = None

        # 判断employ是否与当前选中的一致
        if price != customertext:
            customer.click()
            self.poco(text=price).click()

        # 判断 "请注明资金来源(可多选)" 复选框是否触发
        if self.assetsvalue:
            # 遍历需要点击的选项
            for asset in assets:
                sources = self.exists(self.poco(text=asset))
                # 判断资金来源和资产净值是否同时出现
                if len(sources) == 1:
                    sources.click()
                    if asset == '其他':
                        self.otherfunds.set_text("其他资产净值")

                elif len(sources) > 1:
                    sources[1].click()
                    if asset == '其他':
                        self.otherfunds.set_text("其他资产净值")
                else:
                    print("出现了不止2个, 需要查看问题哦")
                    pass

        # 重新给istotalAnnual赋值, 值为当前勾选的字段
        self.gm.set_List('customerNetAssetValue', assetslist)
        return self.customerNetAssetValueHK.get_text()



