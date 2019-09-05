#!/usr/bin/env python
# -*- coding: utf-8 -*-
from airtest.core.api import *

from Commons.BaseView import BaseView
from ElementPage.startUpFrom import startUpFrom


class publicTool(BaseView):

    def permissionBox(self):
        """
        处理Android权限弹框

        """
        pass


    def click_NextStepbtn(self):
        """
        开户表单所有的下一步按钮

        """
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

    def wait_loading(self):
        self.loading.wait_for_disappearance(10)
        # while True:
        #     print("死循环")
        #     if not self.loading.exists():
        #         print("退出了")
        #         return True

    def swipe_to_Up(self):
        """
        # 向上滑动屏幕
        """
        self.poco("android:id/content").swipe([0, -0.4])


    def DragFrom_LeftToRight(self, element):
        """
        # 从左边拖动到右键
        """
        element.long_click()
        element.swipe([1, 0])

    def closeform(self):
        """
        # APP关闭按钮"X"
        """
        # 关闭开户表单
        touch(Template(self.closeform_img, record_pos=(-0.331, -0.919), resolution=(1080, 2340)))
        # 点击便捷开户
        startUpFrom(self.poco).click_easyOpenning()

    def backform(self):
        """
        # APP返回按钮
        """
        # 点击返回按钮
        touch(Template(self.backform_img, record_pos=(-0.42, -0.919), resolution=(1080, 2340)))
