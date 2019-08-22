#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from airtest.core.api import *

from ElementPage.startUpFrom import startUpFrom


@allure.feature("启动APP, 进入开户界面")
class Test_open():

    @allure.story("进入开户界面")
    @pytest.mark.run(order=1)
    def test_Openning(self, poco):
        startupfrom = startUpFrom(poco)
        with allure.step("启动APP"):
            start_app("io.newtype.eddid.app")

        with allure.step("处理权限弹框--点击运行"):
            startupfrom.permissionBox()

        with allure.step("首次使用设置--点击确定"):
            boolstr = startupfrom.firstSetting()
            if not boolstr:
                allure.attach("AppSetpLOG", "首次使用设置弹框没有出现")

        with allure.step("底部栏选择开户"):
            startupfrom.click_barOpenning()

        with allure.step("点击便捷开户"):
            startupfrom.click_easyOpenning()

        with allure.step("进入注册界面--点击去登陆"):
            startupfrom.click_goLogin()

        with allure.step("登陆界面--输入手机号"):
            startupfrom.send_phonenumber()

        with allure.step("登陆界面--输入密码"):
            startupfrom.send_password()

        with allure.step("登陆界面--点击登陆按钮"):
            startupfrom.click_Loginbtn()



if __name__ == "__main__":
    pytest.main(["-s", "test_open.py", '--alluredir', '../report/xml'])