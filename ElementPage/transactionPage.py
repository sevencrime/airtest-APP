#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView


class transactionPage(BaseView):
    """
    # 选择交易信息
    """

    def click_fundsSource(self, fundsSource=None):
        """
        # 交易的资金/财富来源

        args:
            fundsSource:  list类型, 资产净值需要勾选的字段
        """

        # 判断 "交易的资金/财富来源" 复选框是否触发
        if self.fundsSourcetext:
            # 遍历需要点击的选项
            for funds in fundsSource:
                fund = self.exists(self.poco(text=funds))
                # 判断资金来源和资产净值是否同时出现
                fund.click()





