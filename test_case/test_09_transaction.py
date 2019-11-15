#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import allure
import pytest
from airtest.core.api import *

from Commons import CommonsTool
from Commons.CommonsTool import query_initialData
from ElementPage.publicTool import publicTool
from ElementPage.transactionPage import transactionPage

@pytest.mark.run(order=9)
@allure.feature("选择交易信息")
class Test_transaction():

    fix_routetitle = ["选择交易信息"]
    query_initialData()

    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    @allure.story("选择交易信息")
    def test_sendtransaction(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        transac = transactionPage(poco)
        with allure.step("输入交易资金/财富来源"):
            employ = transac.click_fundsSource(["储蓄", "其他"])

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("点击返回按钮返回账户信息界面"):
            pubTool.backform()
            assert_equal(pubTool.get_Routetitle(), "选择交易信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))


if __name__ == "__main__":
    pytest.main(["-s", "test_09_transaction.py::Test_transaction", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()





