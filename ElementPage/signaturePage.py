#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-10-08 14:20:40
from Commons.BaseView import BaseView


class signaturePage(BaseView):
    """
    # 签名确认
    """

    def signatureview(self):
        return self.signature


    def click_signSubmit(self):

        self.signSubmit.click()


    def click_ReSign(self):

        self.resign.click()


