#!/usr/bin/env python
# -*- coding: utf-8 -*-
from airtest.core.api import *

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
        self.poco("android:id/content").swipe([0, -0.4])
        self.nextStepbtn.click()

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


    def get_boxtitle(self):
        """
        获取弹出框的标题

        """
        boxtitle = self.poco("android:id/content").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[0].child("android.widget.TextView")
        return boxtitle.get_text()

    def get_boxcontent(self):
        """
        获取弹出框的提示内容
        """
        boxcontent = self.poco("android:id/content").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.widget.TextView")
        return boxcontent.get_text()


