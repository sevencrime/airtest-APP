#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from airtest.core.api import *

from ElementPage.publicTool import publicTool
from ElementPage.startUpFrom import startUpFrom


@allure.feature("启动APP, 进入开户界面")
class Test_open():

    @allure.story("进入开户界面")
    @pytest.mark.run(order=1)
    def test_Openning(self, poco):
        startupfrom = startUpFrom(poco)
        pubTool = publicTool(poco)
        # with allure.step("启动APP"):
        #     start_app(package="io.newtype.eddid.app")

        with allure.step("处理权限弹框--点击运行"):
            pubTool.permissionBox()

        # with allure.step("首次使用设置--点击确定"):
        #     boolstr = startupfrom.firstSetting()
        #     if not boolstr:
        #         allure.attach("AppSetpLOG", "首次使用设置弹框没有出现")
        #
        # with allure.step("底部栏选择开户"):
        #     baropen = startupfrom.click_barOpenning()
        #     if not baropen:
        #         allure.attach("AppSetpLOG", "没有底部栏, 非行情APP")

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

        with allure.step("登录后再次点击便捷开户"):
            startupfrom.click_easyOpenning()


if __name__ == "__main__":
    pytest.main(["-s", "test_01_open.py", '--alluredir', '../report/xml'])
    # os.popen("allure generate {xml} -o {html} --clean".format(xml=os.getcwd() + r'\EDDID_APP\report\xml',
    #                                                           html=os.getcwd() + r'\EDDID_APP\report\html'))