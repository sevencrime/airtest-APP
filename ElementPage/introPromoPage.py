#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView
from Commons.GlobalMap import GlobalMap


class introPromoPage(BaseView):
    """
    # 介绍与推广
    """

    # gm = GlobalMap()

    def click_Channels(self, channelslist=None):
        """
        # 您透过哪些渠道认识艾德证券期货及/或艾德金业?(选择所有适用)

        args:
            fundsSource:  list类型, 资产净值需要勾选的字段
        """

        if not self.gm.get_value('isbullion'):
            el_channel = self.poco(text="您透过哪些渠道认识艾德证券期货?")
        else:
            el_channel = self.poco(text="您透过哪些渠道认识艾德证券期货及/或艾德金业?")

        # 遍历需要点击的选项
        for channels in channelslist:
            channel = self.exists(self.poco(text=channels))
            # 判断资金来源和资产净值是否同时出现
            channel.click()





