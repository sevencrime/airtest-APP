#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import shutil
import traceback

import allure
from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException

from Commons.BaseView import BaseView
from Commons.Logging import Logs
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
        self.boxconfirm.click()


    def get_boxtitle(self):
        """
        获取弹出框的标题和弹框的内容

        """
        self.log.debug("正在执行get_boxtitle方法")

        start = time.time()
        while True:
            self.log.debug("循环查找")
            if self.poco(text="确定").exists() and self.poco(text="取消").exists():
                box_alert_text = self.poco(text="确定").parent().parent().parent().offspring("android.widget.TextView")
                break
            elif self.poco(text="知道了").exists():
                box_alert_text = self.poco(text="知道了").parent().parent().parent().offspring("android.widget.TextView")
                break

            if time.time() - start > 15:
                self.log.debug("循环查找超过15秒, 失败")
                break

            self.poco("android:id/content").invalidate()

        self.log.debug("提示框的标题是: {}".format(box_alert_text[0].get_text()))
        self.log.debug("提示框的标题是: {}".format(box_alert_text[1].get_text()))

        return box_alert_text[0].get_text(), box_alert_text[1].get_text()




    def wait_loading(self, timeout=30):

        self.get_Routetitle()
        start = time.time()
        # 循环判断loading是否存在
        while self.loading.exists():
            self.log.debug("wait_loading as True, loading存在")
            self.loading.invalidate()
            self.poco("android:id/content").invalidate()

            if time.time() - start > timeout:
                self.log.error("wait_loading超时!!!!")
                break

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
        # touch(Template(self.closeform_img, record_pos=(-0.378, -0.774), resolution=(810, 1440)))


        # import pdb; pdb.set_trace()

        title = self.Routetitle.get_text()
        close_btn = self.poco(text=title).sibling("android.view.ViewGroup")[1]
        close_btn.click()

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
        # # 点击返回按钮
        # touch(Template(self.backform_img, record_pos=(-0.42, -0.919), resolution=(1080, 2340)))
        # time.sleep(0.5)

        # import pdb; pdb.set_trace()

        title = self.Routetitle.get_text()
        back_btn = self.poco(text=title).sibling("android.view.ViewGroup")[0]
        back_btn.click()


    def get_appcationNumber(self):
        """
        # 通过申请编号判断客户来源

        textMatches: 模糊匹配
        """
        appcationNumberatext = self.poco(textMatches="申请编号:.*").get_text()

        self.gm.set_value(appcationNumber=appcationNumberatext[5:])
        
        return appcationNumberatext[5:]

    # 检验是否全是中文字符
    def is_all_chinese(self, strs):
        for _char in strs:
            if not '\u4e00' <= _char <= '\u9fa5':
                return False
        return True


    # 检验是否含有中文字符
    def is_contains_chinese(self, strs):
        for _char in strs:
            if '\u4e00' <= _char <= '\u9fa5':
                return True
        return False


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
        start = time.time()
        while not self.Routetitle.exists():
            self.log.debug("Routetitle 不存在")
            if time.time() - start > 20:
                break
            pass

        self.log.debug("调用此方法的是: {}".format(traceback.extract_stack()[-2][2]))
        self.log.debug("调用此方法的模块为: {}, 行数为: {}".format(sys._getframe().f_code.co_filename , sys._getframe().f_back.f_lineno))

        try:
            self.log.debug("当前页面的标题为: {}".format(self.Routetitle.get_text(),))
        except PocoNoSuchNodeException:
            self.log.debug("title获取不到")

        return self.Routetitle.get_text()


    def click_box(self):
        start = time.time()
        while not self.poco(text="知道了").exists():
            self.poco(text="知道了").invalidate()
            if time.time() - start > 20:
                break
        self.poco(text="知道了").click()
