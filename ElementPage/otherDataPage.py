#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView


class otherDataPage(BaseView):
    """
    # 其他资料
    """

    def click_bankrupt(self, isFlag):
        """
        # 您是否曾经宣告破产或被申请破产
        """
        content = "您是否曾经宣告破产或被申请破产"
        self.disExists_swipe(self.isElementRadio(content, isFlag)).click()

    def click_customerRelatives(self, isFlag):
        """
        # 客户是否艾德证券及/或艾德金业的雇员或任何其客户的亲属?
        """
        # content = "您是否艾德证券期货及/或艾德金业的雇员或任何其雇员的亲属"
        if self.gm.get_value("isbullion"):
            content = "您是否艾德证券期货及/或艾德金业的雇员或任何其雇员的亲属"
        else:
            content = "您是否艾德证券期货的雇员或任何其雇员的亲属"
        self.disExists_swipe(self.isElementRadio(content, isFlag)).click()


    def click_associatedcustomer(self, isFlag):
        """
        # 3.客户是否与任何艾德证券及/或艾德金业客户有关连?
        """
        if self.gm.get_value("isbullion"):
            content = "您是否与任何艾德证券期货及/或艾德金业客户有关连"
        else:
            content = "您是否与任何艾德证券期货客户有关连"

        self.disExists_swipe(self.isElementRadio(content, isFlag)).click()


    def click_director(self, isFlag):
        """
        # 4.客户是否香港交易所之交易所参与者或证监会之持牌人或注册人之董事、雇员或认可人士?
        """
        content = "您是否香港交易所之交易所参与者或证监会之持牌人或注册人之董事、雇员或认可人士"
        self.disExists_swipe(self.isElementRadio(content, isFlag)).click()

    def click_citizenOfUSA(self, isFlag):
        """
        # 5.客户是否拥有美国公民或美国合法永久居民身份?
        """
        content = "您是否拥有美国公民或美国合法永久居民身份"
        self.disExists_swipe(self.isElementRadio(content, isFlag)).click()

    def click_americanResident(self, isFlag):
        """
        # 6.就税务而言，您是否美国居民?
        """
        content = "就税务而言，您是否是美国居民"
        self.disExists_swipe(self.isElementRadio(content, isFlag)).click()

    def click_PEP_People(self, isFlag):
        """
        # 7.客户是否香港法律定义下的“政治公众人物（PEP）”或与政治公众人物有密切联系？
        """
        content = "您是否香港法律定义下的“政治公众人物（PEP）”或与政治公众人物有密切联系"
        self.disExists_swipe(self.isElementRadio(content, isFlag)).click()

    def click_investmentTarget(self, investments):
        """
        # 您的投资目标是:
        """
        if self.investmentTarget:
            # 遍历需要点击的选项
            for investment in investments:
                invest = self.exists(self.poco(text=investment))
                invest.click()

    def click_riskTolerance(self, grade):
        """
        # 您的风险承受能力是
        """

        riskTolerance = self.poco(text="您的风险承受能力是").sibling("android.view.ViewGroup").child("android.widget.TextView", text=grade)
        riskTolerance.click()
