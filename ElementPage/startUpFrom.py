#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from airtest.core.api import *

from Commons.BaseView import BaseView
from Commons.read_ini import gm_init


class startUpFrom(BaseView):

    # 初始化gm, phone需要从gm获取
    gm_init()


    def Start_APP(self):
        # 获取当前界面的包名和Activity
        CurrentFocus = os.popen("adb -s {} shell dumpsys window | findstr mCurrentFocus".format(self.gm.get_value("deviceuuid"))).read()
        currentActivity = ''.join(re.findall(r"u0\s(.+)}", CurrentFocus))

        # start_app('io.newtype.eddid.app', 'io.newtype.eddid.app.MainActivity')
        if currentActivity.find("io.newtype.eddid.app") == -1:
            # 启动APP
            os.popen("adb -s {} shell am start -n io.newtype.eddid.app/com.bartech.app.main.launcher.LauncherActivity".format(self.gm.get_value("deviceuuid"))).read()

        return currentActivity



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
        # self.phonenumber.set_text("15089514626")
        self.tel_edit.set_text(self.gm.get_value("phone"))

    def send_password(self):
        """
        登陆界面--输入密码

        """
        # self.poco(text="请输入密码").set_text("abcd1234")
        # self.poco("android.widget.ScrollView").child("android.view.ViewGroup").child("android.widget.EditText")[1].set_text("abcd1234")
        self.passwordedit.set_text("abcd1234")

    def click_Loginbtn(self):
        """
        登陆界面--登陆按钮

        """
        # self.poco("android.widget.ScrollView").child("android.view.ViewGroup").child("android.view.ViewGroup").child(
        #     "android.widget.TextView", text="登录").click()

        self.loginbtn.click()
