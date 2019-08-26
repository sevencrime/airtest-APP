#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commons.BaseView import BaseView


class publicPage(BaseView):

    def permissionBox(self):
        """
        处理Android权限弹框

        """
        pass


    def click_NextStepbtn(self):
        """
        开户表单所有的下一步按钮

        """
        self.exists(self.nextStepbtn).click()

    def click_boxCancel(self):
        """
        开户表单-- 弹出确认框--取消按钮

        """
        self.boxCancel.click()


    def click_boxconfirm(self):
        """
        开户表单-- 弹出确认框--确定按钮

        """
        self.exists(self.boxconfirm).click()