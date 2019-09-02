#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob

from airtest.core.api import *

from Commons.BaseView import BaseView


class idcardPage(BaseView):
    # 当前目录
    curPath = os.path.abspath(os.path.dirname(__file__))
    # 项目根目录
    rootPath = curPath[:curPath.find("airtest-APP\\") + len("airtest-APP\\")]

    # 采用图片识别方式上传身份证
    idcardimgpath = glob.glob(rootPath + r'\testData\testIMG\tpl1567406605623.png')
    idcardimgnegative = glob.glob(rootPath + r'\testData\testIMG\tpl1567407008671.png')
    idcardimgpositive = glob.glob(rootPath + r'\testData\testIMG\tpl1567408843326.png')

    def click_Chinese(self):
        """
        选择内地居民

        """
        self.el_chinese.click()


    def upload_idcardpositive(self):
        """
        身份证正面--国徽面

        """
        import pdb; pdb.set_trace()
        self.el_idcardpositive.wait_for_appearance().click()
        self.gallery.click()

        touch(Template("".join(self.idcardimgpath), record_pos=(0.109, -0.466), resolution=(1080, 2340)))
        touch(Template("".join(self.idcardimgpositive), record_pos=(-0.111, -0.728), resolution=(1080, 2340)))
        return True

    def upload_idcardNegative(self):
        """
        身份证正面--人像面

        """
        self.el_idcardNegative.click()
        self.gallery.click()

        touch(Template("".join(self.idcardimgpath), record_pos=(0.109, -0.466), resolution=(1080, 2340)))
        touch(Template("".join(self.idcardimgnegative), record_pos=(-0.367, -0.721), resolution=(1080, 2340)))

        return True
