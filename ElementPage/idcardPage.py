#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob

from airtest.core.api import *

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
        time.sleep(10)
        self.el_idcardpositive.wait(10)
        self.el_idcardpositive.click()
        self.gallery.click()

        touch(Template("".join(self.idcardimgpath_img), record_pos=(0.109, -0.466), resolution=(1080, 2340)))
        touch(Template("".join(self.idcardimgpositive_img), record_pos=(-0.111, -0.728), resolution=(1080, 2340)))

    def upload_idcardNegative(self):
        """
        身份证正面--人像面

        """
        self.el_idcardNegative.wait(10)
        self.el_idcardNegative.click()
        self.gallery.click()

        touch(Template("".join(self.idcardimgpath_img), record_pos=(0.109, -0.466), resolution=(1080, 2340)))
        touch(Template("".join(self.idcardimgnegative_img), record_pos=(-0.367, -0.721), resolution=(1080, 2340)))

if __name__ == '__main__':
    idcardPage()