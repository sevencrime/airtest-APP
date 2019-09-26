#!/usr/bin/env python
# -*- coding: utf-8 -*-
import traceback

from airtest.core.api import *

from Commons.BaseView import BaseView
from Commons.Logging import Logs
from ElementPage.startUpFrom import startUpFrom
import sys

class publicTool(BaseView):

    log = Logs()

    def permissionBox(self):
        """
        处理Android权限弹框

        """
        pass


    def click_NextStepbtn(self, title=None):
        """
        开户表单所有的下一步按钮

        """
        self.nextStepbtn.wait_for_appearance(30)
        index = 0
        while index < 10:
            # if index > 10:
            #     self.log.debug("'下一步'按钮循环点击超过10次, 退出")
            #     break

            # 获取页面标题内容, 目的是为了刷新页面
            # self.get_Routetitle()
            self.nextStepbtn.invalidate()
            # 判断按钮是否高亮, 通过focusable属性
            if self.nextStepbtn.attr("focusable"):
                self.log.debug("'下一步'按钮高亮")
                self.nextStepbtn.click()
                # return True
                break
            #     if title != None:
            #         try:
            #             assert_equal(self.get_Routetitle(), title, msg="页面标题错误")
            #             return True
            #         except AssertionError:
            #             self.log.debug("循环点击")
            #             continue
            #     else:
            #         return True

            index += 1

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
        获取弹出框的标题和弹框的内容

        """
        index = 0
        while True:

            try:
                # 获取页面标题, 代替页面刷新
                self.get_Routetitle()
                # 弹出框标题
                boxtitle = self.poco("android:id/content").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[0].child("android.widget.TextView")
                self.log.debug("获取boxtitle成功, 标题是{}".format(boxtitle))
                # 弹出框内容
                boxcontent = self.poco("android:id/content").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.widget.TextView")
                self.log.debug("获取boxcontent成功, 内容是{}".format(boxcontent))
                return boxtitle.get_text(), boxcontent.get_text()

            except Exception as e:
                self.log.debug("弹框标题或内容获取失败")

            finally:
                index += 1
                if index > 10:
                    break



    def wait_loading(self):
        self.loading.wait_for_disappearance(30)
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
        time.sleep(0.5)

    def customersource(self):
        """
        # 通过申请编号判断客户来源

        textMatches: 模糊匹配
        """
        appcationNumberatext = self.poco(textMatches="申请编号:.*").get_text()
        # 判断申请编号是否APP或H5
        if appcationNumberatext.find("app") != -1 or appcationNumberatext.find("h5") != -1:
            if self.gm.get_value("environment") == "uat":
                self.gm.set_value(source='aos-uat')
            else:
                self.gm.set_value(source='aos')

        else:
            if self.gm.get_value("enviroment") == "uat":
                self.gm.set_value(source='uat')
            else:
                self.gm.set_value(source='test')

            self.gm.set_value(appcationNumber=appcationNumberatext[5:])


    def get_Routetitle(self):
        """
        # 获取页面的标题

            # invalidate() : 刷新Android界面
                Android的invalidate与postInvalidate都是用来刷新界面的。
                在UI主线程中，用invalidate()，本质是调用View的onDraw（）绘制。
                主线程之外，用postInvalidate()。

                地址:
                https://www.zybuluo.com/natsumi/note/470226
        """
        self.Routetitle.invalidate()
        self.log.debug("调用此方法的是: {}".format(traceback.extract_stack()[-2][2]))
        self.log.debug("调用此方法的模块为: {}, 行数为: {}".format(sys._getframe().f_code.co_filename , sys._getframe().f_back.f_lineno))
        self.log.debug("当前页面的标题为: {}".format(self.Routetitle.get_text()))
        return self.Routetitle.get_text()




