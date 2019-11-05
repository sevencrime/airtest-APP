#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView


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

        channel = set(self.gm.get_value("channels")).symmetric_difference(channelslist)
        self.log.debug("需要点击的选项有: {}".format(','.join(channel)))

        # 遍历需要点击的选项
        for channels in channel:
            cha = self.exists(self.poco(text=channels))
            # 判断资金来源和资产净值是否同时出现
            cha.click()

        self.gm.set_List('channels', channelslist)



    def click_personalInfoDeclartionLangsasImgview(self, isFlag):
        # 本人同意艾德证券期货根据「个人资料之使用声明」使用或转移本人的个人资料做直接促销用途。勾选
        if not self.gm.get_value("Routetitle") == "衍生品产品认识" and isFlag :
            self.personalInfoDeclartionLangsasImgview.click()

        elif self.gm.get_value("Routetitle") == "衍生品产品认识" and not isFlag :
            self.personalInfoDeclartionLangsasImgview.click()




    def click_personalInfoDeclartionLangsas(self):

        return self.personalInfoDeclartionLangsas.get_value()


