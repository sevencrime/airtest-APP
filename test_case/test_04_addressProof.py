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
from ElementPage.addressProofPage import addressProofPage
from ElementPage.publicTool import publicTool
from test_case.parentBase import ParentBase


@allure.feature("地址证明")
class Test_addressProof():
    gm = GlobalMap()
    query_initialData()
    fix_routetitle = ["住址信息"]

    @allure.story("正常输入地址证明")
    @pytest.mark.usefixtures('reloadRoute')
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    @pytest.mark.skipif(gm.get_value("sameAdderss") == False, reason="没有勾选地址证明")
    def test_sendAddressProof(self, poco):

        pubTool = publicTool(poco)
        addressProof = addressProofPage(poco)

        with allure.step("上传地址证明"):
            addressProof.upload_addressProve()
            pubTool.wait_loading()

        with allure.step("输入现住址"):
            nowaddress = addressProof.send_Nowaddress()

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()
            pubTool.wait_loading()

        with allure.step("校验地址弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "请确认您的住址", "确认地址弹框标题有误")
            assert_equal(boxcontent, nowaddress, "弹框内容与填写内容不符")

        with allure.step("确认地址弹框--点击确定"):
            pubTool.click_boxconfirm()
            assert_equal(pubTool.get_Routetitle(), "银行卡信息", "页面没有跳转")


if __name__ == "__main__":
    pytest.main(["-s", '--pdb', "test_04_addressProof.py::Test_addressProof", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()