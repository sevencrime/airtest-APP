#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import allure
import pytest
from airtest.core.api import *

from Commons import CommonsTool
from Commons.CommonsTool import query_initialData
from Commons.GlobalMap import GlobalMap
from ElementPage.personalInformationPage import personalInformationPage
from ElementPage.publicTool import publicTool


@allure.feature("请填写个人资料")
class Test_personalinfomation():
    gm = GlobalMap()
    query_initialData()
    fix_routetitle = ["请填写个人资料"]

    @allure.story("填写个人资料")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    @pytest.mark.skipif(gm.get_value("environment").find("aos") != -1, reason="后台是aos接口, 没有该页面, 跳过此用例")
    def test_personal(self, poco, reloadRoute):

        perinfo = personalInformationPage(poco)
        pubTool = publicTool(poco)
        with allure.step("输入电邮"):
            email = perinfo.send_emali()
        with allure.step("再次输入电邮"):
            reEmail = perinfo.send_reemail()
        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("校验地址弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "请确认您的身份证地址", "确认地址弹框标题有误")
            assert_equal(boxcontent, perinfo.get_address(), "弹框内容与填写内容不符")


        with allure.step("确认地址弹框--点击确定"):
            pubTool.click_boxconfirm()



if __name__ == "__main__":
    pytest.main(["-s", "test_03_personalinfomation.py", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()