#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView


class financialPage(BaseView):

    """
    # 香港保证金融资账户
    """

    def click_isMarginAccount(self, isFlag):
        """
        # 您的配偶是否持有艾德证券任何相关的保证金账户?
        """
        context = "您的配偶是否持有艾德证券任何相关的保证金账户?"
        self.isElementRadio(context, isFlag).click()

        # isFlag存入global
        if isFlag:
            # 输入账户持有人姓名
            self.gm.set_bool(MarginAccountName=True)
            # 输入账户号码
            self.gm.set_bool(MarginAccountNumber=True)


    def click_isDiscretion(self, isFlag):
        """
        # 您或您的配偶是否单独或共同控制艾德证券之其他保证金账户35%或以上之表决权?
        """
        context = "您或您的配偶是否单独或共同控制艾德证券之其他保证金账户35%或以上之表决权?"
        self.isElementRadio(context, isFlag).click()

        # isFlag存入global
        if isFlag:
            # 输入账户持有人姓名
            self.gm.set_bool(iscretionAccountName=True)
            # 输入账户号码
            self.gm.set_bool(iscretionAccountNumber=True)


    def click_isCompanyAccounts(self, isFlag):
        """
        # 您是否有以客户的同一集团公司旗下之公司开立保证金账户？?
        """
        context = "您是否有以客户的同一集团公司旗下之公司开立保证金账户？"
        self.isElementRadio(context, isFlag).click()

        # isFlag存入global
        if isFlag:
            # 输入账户持有人姓名
            self.gm.set_bool(CompanyAccountsAccountName=True)
            # 输入账户号码
            self.gm.set_bool(CompanyAccountsAccountNumber=True)


    def click_accountHolder(self, isFlag):
        """
        # 您是否是账户的最终实益拥有人?
        """
        context = "您是否是账户的最终实益拥有人?"
        self.isElementRadio(context, isFlag).click()

        # 触发框, 受益人名称
        if not isFlag:
            # self.gm.set_bool(beneficiaryName=True)
            self.beneficiaryName.set_text("账户的最终实益拥有人")



    def click_orderPerson(self, isFlag):
        """
        # 您是否是最终负责下单的人?
        """
        context = "您是否是最终负责下单的人?"
        self.isElementRadio(context, isFlag).click()

        # 触发框, 下单人名称
        if not isFlag:
            # self.gm.set_bool(ordersName=True)
            self.ordersName.set_text("最终负责下单的人")


    def send_AccountName(self):
        """
            # 账户持有人姓名

        """
        if self.gm.get_value("MarginAccountName"):
            self.AccountName.set_text("账户持有人姓名1")

        elif self.gm.get_value("iscretionAccountName"):
            if len(self.AccountName) == 1:
                self.AccountName.set_text("账户持有人姓名2")
            elif len(self.AccountName) != 2:
                if self.gm.get_value("MarginAccountName"):
                    self.AccountName[1].set_text("账户持有人姓名2")
                elif self.gm.get_value("ordersName"):
                    self.AccountName.set_text("账户持有人姓名2")

        elif self.gm.get_value("CompanyAccountsAccountName"):
            if len(self.AccountName) == 1:
                self.AccountName.set_text("账户持有人姓名3")
            elif len(self.AccountName) == 2 :
                self.AccountName[1].set_text("账户持有人姓名3")

            elif len(self.AccountName) == 3:
                self.AccountName[2].set_text("账户持有人姓名3")


    def send_AccountNumber(self):
        """
            # 账户号码

        """
        if self.gm.get_value("MarginAccountNumber"):
            self.AccountNumber.set_text("账户号码1")

        elif self.gm.get_value("iscretionAccountNumber"):
            if len(self.AccountNumber) == 1:
                self.AccountNumber.set_text("账户号码2")
            elif len(self.AccountNumber) != 2:
                if self.gm.get_value("MarginAccountNumber"):
                    self.AccountNumber[1].set_text("账户号码2")
                elif self.gm.get_value("orders"):
                    self.AccountNumber.set_text("账户号码2")

        elif self.gm.get_value("CompanyAccountsAccountNumber"):
            if len(self.AccountNumber) == 1:
                self.AccountNumber.set_text("账户号码3")
            elif len(self.AccountNumber) == 2 :
                self.AccountNumber[1].set_text("账户号码3")

            elif len(self.AccountNumber) == 3:
                self.AccountNumber[2].set_text("账户号码3")






