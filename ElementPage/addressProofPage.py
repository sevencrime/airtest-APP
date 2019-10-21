#!/usr/bin/env python
# -*- coding: utf-8 -*-
from airtest.core.api import *
from Commons.BaseView import BaseView


class addressProofPage(BaseView):
    """
    地址证明

    """

    def upload_addressProve(self):
        '''
        上传地址证明
        :return:
        '''
        self.addressProve.click()
        # 选择相册上传
        self.gallery.wait(5)
        self.gallery.click()

        if device().uuid == '127.0.0.1:7555':
            touch(Template("".join(self.mumuidcardimgpath_img), record_pos=(-0.17, 0.572), resolution=(810, 1440)))
            time.sleep(1)
            touch(Template("".join(self.mumuidcardimgpositive_img), record_pos=(-0.002, 0.277), resolution=(810, 1440)))

    def send_Nowaddress(self):

        self.Nowaddress.set_text("深圳桑达科技大厦123@qaz../")
        self.Nowaddress.invalidate()

        return self.Nowaddress.get_text()

