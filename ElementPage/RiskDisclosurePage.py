#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView
from ElementPage.publicTool import publicTool


class RiskDisclosurePage(BaseView):
    """
    # 风险披露
    """

    def click_player(self):
        self.player.click()


    def drag_progressbar(self):
        pubtool = publicTool(self.poco)
        pubtool.DragFrom_LeftToRight(self.progressbar)


    def click_isUnderstandRisk(self):
        self.isUnderstandRisk.click()

