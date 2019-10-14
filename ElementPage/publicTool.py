#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import shutil
import traceback

from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException

from Commons.BaseView import BaseView
from Commons.Logging import Logs
from ElementPage.startUpFrom import startUpFrom
import sys

class publicTool(BaseView):

    log = Logs()

    def allow_permissionBox(self):
        """
        处理Android权限弹框

        """
        try:
            # 循环5次, 点击多个弹框
            for i in range(5):
                self.permission_allow_button.invalidate()
                permission_title = self.permission_title.get_text()
                self.log.info("权限 >> {}".format(permission_title,))
                self.permission_allow_button.click()

        except Exception as e:
            self.log.debug("没有出现权限弹框")
            pass


    def click_NextStepbtn(self, title=None):
        """
        开户表单所有的下一步按钮

        """
        self.log.debug("调用此方法的是: {}".format(traceback.extract_stack()[-2][2]))
        # index = 0
        # while index < 10:
        #     self.log.debug("进入下一步循环")
        #     # 获取页面标题内容, 目的是为了刷新页面
        #     # self.nextStepbtn.invalidate()
        #     nextStepbtn = self.disExists_swipe(self.nextStepbtn)
        #     # 判断按钮是否高亮, 通过focusable属性
        #     if nextStepbtn.attr("focusable"):
        #         self.log.debug("'下一步'按钮高亮")
        #         nextStepbtn.click()
        #         break
        #
        #     index += 1

        nextStepbtn = self.disExists_swipe(self.nextStepbtn)
        nextStepbtn.click()



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
        # index = 0
        # while True:
        #
        #     try:
        #         # 获取页面标题, 代替页面刷新
        #         self.get_Routetitle()
        #         # 弹出框标题
        #         boxtitle = self.poco("android:id/content").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.view.ViewGroup")[0].child("android.widget.TextView")
        #         self.log.debug("获取boxtitle成功, 标题是{}".format(boxtitle))
        #         # 弹出框内容
        #         boxcontent = self.poco("android:id/content").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup")[1].child("android.view.ViewGroup").child("android.view.ViewGroup").child("android.widget.TextView")
        #         self.log.debug("获取boxcontent成功, 内容是{}".format(boxcontent))
        #         return boxtitle.get_text(), boxcontent.get_text()
        #
        #     except Exception as e:
        #         self.log.debug("弹框标题或内容获取失败")
        #
        #     finally:
        #         index += 1
        #         if index > 10:
        #             break


        boxalert = self.poco("android:id/content").child("android.widget.FrameLayout").child("android.view.ViewGroup").child("android.view.ViewGroup")[-1].offspring("android.widget.TextView")

        while not boxalert.exists():
            boxalert.invalidate()
            pass

        self.log.debug("提示框的标题是: {}".format(boxalert[0].get_text()))
        self.log.debug("提示框的标题是: {}".format(boxalert[1].get_text()))

        return boxalert[0].get_text(), boxalert[1].get_text()




    def wait_loading(self):

        self.get_Routetitle()
        # 循环判断loading是否存在
        while self.loading.exists():
            self.log.debug("wait_loading as True, loading存在")
            self.loading.invalidate()
            time.sleep(1)


    def swipe_to_Up(self):
        """
        # 向上滑动屏幕
        """
        contentEle = self.poco("android:id/content")
        contentEle.invalidate()
        contentEle.swipe([0, -0.4])

    def swipe_to_Down(self):
        """
        # 向下滑动屏幕
        """
        contentEle = self.poco("android:id/content")
        contentEle.invalidate()
        contentEle.swipe([0, 0.4])


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
        touch(Template(self.closeform_img, record_pos=(-0.378, -0.774), resolution=(810, 1440)))

        # 重复十次
        for i in range(10):
            if self.get_Routetitle() == "艾德证券期货":
                # 点击便捷开户
                self.easyOpenning.click()
                break


    def backform(self):
        """
        # APP返回按钮
        """
        # 点击返回按钮
        touch(Template(self.backform_img, record_pos=(-0.42, -0.919), resolution=(1080, 2340)))
        time.sleep(0.5)

    def get_appcationNumber(self):
        """
        # 通过申请编号判断客户来源

        textMatches: 模糊匹配
        """
        appcationNumberatext = self.poco(textMatches="申请编号:.*").get_text()

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

        while not self.Routetitle.exists():
            self.log.debug("Routetitle 不存在")
            pass

        self.log.debug("调用此方法的是: {}".format(traceback.extract_stack()[-2][2]))
        self.log.debug("调用此方法的模块为: {}, 行数为: {}".format(sys._getframe().f_code.co_filename , sys._getframe().f_back.f_lineno))
        try:
            self.log.debug("当前页面的标题为: {}".format(self.Routetitle.get_text(),))
        except PocoNoSuchNodeException:
            self.log.debug("首页title获取不到")

        return self.Routetitle.get_text()



    def rmdir5(self):

        curPath = os.path.abspath(os.path.dirname(__file__))
        rootPath = curPath[:curPath.find("airtest-APP\\") + len("airtest-APP\\")]
        xml_report_pathlib = glob.glob(rootPath + r'report\\xml*')
        html_report_pathlib = glob.glob(rootPath + r'report\\html*')

        html_report_name = rootPath + r'report\html' + os.path.basename(xml_report_pathlib[-1])[3:]
        # 判断文件目录是否超过5个
        # 生成后才调用该方法, 所以要+1
        if len(xml_report_pathlib) >= 6:
            # shutil模块, 文件高级库
            shutil.rmtree(xml_report_pathlib[0])

        if len(html_report_pathlib) >= 5:
            # 删除第一个
            shutil.rmtree(html_report_pathlib[0])

        self.gm.set_value(xml_report_path=xml_report_pathlib[-1])
        self.gm.set_value(html_report_path=html_report_name)
        return xml_report_pathlib[-1], html_report_name

