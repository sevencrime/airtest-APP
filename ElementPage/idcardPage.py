#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commons.BaseView import BaseView


class idcardPage(BaseView):

    def click_Chinese(self):
        """
        选择内地居民

        """
        self.el_chinese.click()


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
        self.el_idcardNegative.click()
        self.Album.click()