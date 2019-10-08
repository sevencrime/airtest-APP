#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest

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
    pytest.main(["-s", "test_16_signature.py", '--alluredir', '../report/xml'])






