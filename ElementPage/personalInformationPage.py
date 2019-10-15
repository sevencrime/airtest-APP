#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView


class personalInformationPage(BaseView):
    """
    请填写个人资料

    """

    def modify_chinesename(self, ismodify):
        try:
            assert self.el_chinesename.get_text() == '宜小信'
        except Exception as e:
            self.log.error("姓名OCR识别有误, 错误的中文姓名为: {}".format(self.el_chinesename.get_text()))

        if ismodify:
            # 判断是否修改
            self.el_chinesename.set_text("修改中文姓名")
            self.el_chinesename.invalidate()
            chineseanme = self.el_chinesename.get_text()


        return chineseanme

    def send_emali(self, email="15089514626@sina.cn"):
        """
        输入邮箱

        """
        # import pdb; pdb.set_trace()
        self.exists(self.el_email).set_text(email)

    def send_reemail(self, email="15089514626@sina.cn"):
        """
        再次输入电邮

        """
        self.exists(self.el_reEmail).set_text(email)


    def get_address(self):
        """
        获取地址栏的值

        """
        return self.exists(self.el_iDcardAddress).get_text()


