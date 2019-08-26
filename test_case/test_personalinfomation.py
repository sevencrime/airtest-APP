#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from airtest.core.api import *

from ElementPage.personalInformationPage import personalInformationPage
from ElementPage.idcardPage import idcardPage
from ElementPage.publicPage import publicPage


@allure.feature("请填写个人资料")
class Test_personalinfomation():

    @allure.story("填写个人资料")
    @pytest.mark.run(order=3)
    def test_Openning(self, poco):
        perinfo = personalInformationPage(poco)
        pubpage = publicPage(poco)
        with allure.step("输入电邮"):
            perinfo.send_emali()
        with allure.step("再次输入电邮"):
            perinfo.send_reemail()
        with allure.step("点击下一步"):
            pubpage.click_NextStepbtn()
        with allure.step("确认地址弹框--点击确定"):
            pubpage.click_boxconfirm()


if __name__ == "__main__":
    pytest.main(["-s", "test_personalinfomation.py", '--alluredir', '../report/xml'])
    # os.popen("allure generate {xml} -o {html} --clean".format(xml=os.getcwd() + r'\EDDID_APP\report\xml',
    #                                                           html=os.getcwd() + r'\EDDID_APP\report\html'))