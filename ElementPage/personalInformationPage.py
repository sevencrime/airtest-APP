#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView


class personalInformationPage(BaseView):
    """
    请填写个人资料

    """

    def send_emali(self, email="onedi@qq.com"):
        """
        输入邮箱

        """
        # import pdb; pdb.set_trace()
        self.exists(self.el_email).set_text(email)

    def send_reemail(self, email="onedi@qq.com"):
        """
        再次输入电邮

        """
        self.exists(self.el_reEmail).set_text(email)


    def get_address(self):
        """
        获取地址栏的值

        """
        return self.exists(self.el_iDcardAddress).get_text()
