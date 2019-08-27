#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView


class startUpFrom(BaseView):

    def firstSetting(self):
        """
        首次使用设置

        """
        try:
            self.exists(self.el_firstSetting_loc).click()
        except:
            return False


    def click_barOpenning(self):
        """
        底部栏--开户选项

        """
        try:
            self.exists(self.baropen).click()
        except:
            return False


    def click_easyOpenning(self):
        """
        便捷开户

        """
        self.easyOpenning.click()

    def click_goLogin(self):
        """
        注册界面--去登陆

        """
        self.goLogin.click()

    def send_phonenumber(self):
        """
        登陆界面--输入电话号码(手机号)

        """
        self.phonenumber.set_text("15089514626")

    def send_password(self):
        """
        登陆界面--输入密码

        """
        # import pdb;pdb.set_trace()
        # self.poco(text="请输入密码").set_text("abcd1234")
        self.poco("android.widget.ScrollView").child("android.view.ViewGroup").child("android.widget.EditText")[1].set_text("abcd1234")

    def click_Loginbtn(self):
        """
        登陆界面--登陆按钮

        """
        self.poco("android.widget.ScrollView").child("android.view.ViewGroup").child("android.view.ViewGroup").child(
            "android.widget.TextView", text="登录").click()
