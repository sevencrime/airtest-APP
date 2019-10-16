#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView


class personalInformationPage(BaseView):
    """
    请填写个人资料

    """

    def modify_title(self, ismodify):
        self.disExists_swipe(self.el_title)
        try:
            assert self.el_title.get_text() == '宜小信'
        except Exception as e:
            self.log.error("姓名OCR识别有误, 错误的中文姓名为: {}".format(self.el_title.get_text()))

        if ismodify:
            # 判断是否修改
            self.el_title.set_text("修改中文姓名")
            self.el_title.invalidate()
            title = self.el_title.get_text()

        return title


    def modify_chinesename(self, ismodify):
        self.disExists_swipe(self.el_chinesename)
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
        self.disExists_swipe(self.el_email).set_text(email)

    def send_reemail(self, email="15089514626@sina.cn"):
        """
        再次输入电邮

        """
        self.disExists_swipe(self.el_reEmail).set_text(email)


    def get_address(self):
        """
        获取地址栏的值

        """
        return self.disExists_swipe(self.el_iDcardAddress).get_text()


