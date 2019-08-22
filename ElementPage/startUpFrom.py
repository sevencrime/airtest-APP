#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView


class startUpFrom(BaseView):

    firstSetting_loc = 'io.newtype.eddid.app:id/btn_start'

    def permissionBox(self):
        """
        处理Android权限弹框

        """
        pass


    def firstSetting(self):
        """
        首次使用设置

        """
        try:
            self.poco(self.firstSetting_loc).click()
            return True
        except:
            return False

    def click_barOpenning(self):
        """
        底部栏--开户选项

        """
        # self.poco(self.barOpenning_loc).click()
        self.poco(text="开户").click()

    def click_easyOpenning(self):
        """
        便捷开户

        """
        self.poco(text="便捷开户").click()

    def click_goLogin(self):
        """
        注册界面--去登陆

        """
        self.poco(text="去登录").click()

    def send_phonenumber(self):
        """
        登陆界面--输入电话号码(手机号)

        """
        self.poco(text="请输入手机号").set_text("15089514626")


    def send_password(self):
        """
        登陆界面--输入密码

        """
        self.poco(text="请输入密码").set_text("abcd1234")


    def click_Loginbtn(self):
        """
        登陆界面--登陆按钮

        """
        self.poco("android.widget.ScrollView").child("android.widget.TextView").child("android.view.ViewGroup").child(
            "android.widget.TextView", text="登录").click()

