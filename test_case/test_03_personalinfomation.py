#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from airtest.core.api import *

from ElementPage.personalInformationPage import personalInformationPage
from ElementPage.idcardPage import idcardPage
from ElementPage.publicTool import publicTool


@allure.feature("请填写个人资料")
class Test_personalinfomation():

    @allure.story("填写个人资料")
    @pytest.mark.run(order=3)
    def test_personal(self, poco):
        perinfo = personalInformationPage(poco)
        pubtool = publicTool(poco)
        with allure.step("输入电邮"):
            email = perinfo.send_emali()
        with allure.step("再次输入电邮"):
            reEmail = perinfo.send_reemail()
        with allure.step("点击下一步"):
            pubtool.click_NextStepbtn()

        with allure.step("校验地址弹框标题和内容"):
            boxtitle = pubtool.get_boxtitle()
            boxcontent = pubtool.get_boxcontent()
            assert_equal(boxtitle, "请确认您的身份证地址", "确认地址弹框标题有误")
            assert_equal(boxcontent, perinfo.get_address(), "弹框内容与填写内容不符")

        with allure.step("确认地址弹框--点击确定"):
            pubtool.click_boxconfirm()



if __name__ == "__main__":
    pytest.main(["-s", "test_03_personalinfomation.py", '--alluredir', '../report/xml'])
    # os.popen("allure generate {xml} -o {html} --clean".format(xml=os.getcwd() + r'\EDDID_APP\report\xml',
    #                                                           html=os.getcwd() + r'\EDDID_APP\report\html'))