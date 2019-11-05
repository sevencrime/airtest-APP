#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView


class PreviewPage(BaseView):
    """
    # 预览页
    """

    # 预览页提交按钮
    def click_submit(self):
        self.disExists_swipe(self.previewSubmit).click()

    # 签署PDF
    def signPDF(self):
        index = 0
        for btn in self.signPDF_btn:
            if index == 1:
                btn.click()
            index += 1

    # 签署完成提交
    def completePDF(self):
        self.completePDF_btn.click()
