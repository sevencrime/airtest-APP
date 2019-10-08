#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob

from airtest.core.api import *

from Commons.BaseView import BaseView
from ElementPage.publicTool import publicTool


class idcardPage(BaseView):

    def permission(func):
        """
        处理权限弹框
        :param func:
        :return:
        """

        def wrapper(self, *args, **kwargs):
            import pdb; pdb.set_trace()
            try:
                return func(self, *args, **kwargs)
            except:
                pubTool = publicTool(self.poco)
                pubTool.allow_permissionBox()
                return func(self, *args, **kwargs)
        return wrapper


    def click_Chinese(self):
        """
        选择内地居民

        """
        self.el_chinese.click()

    # @permission
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

    # @permission
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