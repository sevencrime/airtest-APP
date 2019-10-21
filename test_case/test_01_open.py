#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import allure
import pytest
from Commons.GlobalMap import GlobalMap
from ElementPage.publicTool import publicTool
from airtest.core.api import *

from ElementPage.startUpFrom import startUpFrom


@allure.feature("启动APP, 进入开户界面")
class Test_open():

    @allure.story("进入开户界面")
    def test_Openning(self, poco):
        pubTool = publicTool(poco)
        startupfrom = startUpFrom(poco)

        with allure.step("启动APP"):
            startupfrom.Start_APP()

        with allure.step("处理权限弹框--点击运行"):
            pubTool.allow_permissionBox()

        # with allure.step("首次使用设置--点击确定"):
        #     boolstr = startupfrom.firstSetting()
        #     if not boolstr:
        #         allure.attach("AppSetpLOG", "首次使用设置弹框没有出现")
        #
        # with allure.step("底部栏选择开户"):
        #     baropen = startupfrom.click_barOpenning()
        #     if not baropen:
        #         allure.attach("AppSetpLOG", "没有底部栏, 非行情APP")

        with allure.step("判断是否登录"):
            if pubTool.get_Routetitle() in ['艾德证券期货', '注册', '登录', '个人中心']:
                pytest.mark.skip(reason="已登录, 跳过下面步骤")

        with allure.step("点击便捷开户"):
            if pubTool.get_Routetitle() == "艾德证券期货":
                startupfrom.click_easyOpenning()

        with allure.step("进入注册界面--点击去登陆"):
            startupfrom.click_goLogin()

        with allure.step("登陆界面--输入手机号"):
            startupfrom.send_phonenumber()

        with allure.step("登陆界面--输入密码"):
            startupfrom.send_password()

        with allure.step("登陆界面--点击登陆按钮"):
            startupfrom.click_Loginbtn()
            pubTool.wait_loading()

        with allure.step("登录后再次点击便捷开户"):
            if pubTool.get_Routetitle() == "艾德证券期货":
                startupfrom.click_easyOpenning()
                pubTool.wait_loading()



if __name__ == "__main__":
    pytest.main(["-s", "-v", "test_01_open.py", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    gm = GlobalMap()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(xml_report_path=gm.get_value("xml_report_path"), html_report_path=gm.get_value("html_report_path"))).read()
