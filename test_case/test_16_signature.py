#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import allure
import pytest

from Commons import CommonsTool
from ElementPage.publicTool import publicTool
from ElementPage.signaturePage import signaturePage


@allure.feature("签名确认")
class Test_Signature():

    @allure.story("签名确认")
    def test_signaturepass(self, poco):
        pubTool = publicTool(poco)
        sign = signaturePage(poco)
        with allure.step("在签名位置划线"):
            sign.signatureview().swipe([-0.6, 0.5])

        with allure.step("点击提交按钮"):
            sign.click_signSubmit()

        with allure.step("如果有权限弹框, 点击允许"):
            pubTool.allow_permissionBox()






if __name__ == "__main__":
    pytest.main(["-s", "test_16_signature.py", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()





