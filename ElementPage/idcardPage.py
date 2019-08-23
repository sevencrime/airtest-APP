#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commons.BaseView import BaseView


class idcardPage(BaseView):

    def click_Chinese(self):
        """
        选择内地居民

        """
        self.poco(text="我是内地居民").click()


    def click_NextStepbtn(self):
        """
        开户表单所有的下一步按钮

        """
        self.poco(text="下一步").click()

    def upload_idcardpositive(self):
        """
        身份证正面--国徽面

        """
        pass


    def upload_idcardNegative(self):
        """
        身份证正面--人像面

        """
        # adb push "C:\Users\Onedi Zheng\Desktop\111.jpg" / storage / emulated / 0 / DCIM / Camera
        self.poco(text="请上传身份证人像面").click()
        self.poco(text="相册选取").click()