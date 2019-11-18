#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import allure
import pytest
from airtest.core.api import *

from Commons import CommonsTool
from ElementPage.previewPage import PreviewPage
from ElementPage.publicTool import publicTool


@pytest.mark.run(order=17)
@allure.feature("预览页提交")
class Test_Preview():

    @allure.story("预览页直接提交")
    def test_preview_submit(self, poco):
        pubTool = publicTool(poco)
        preview = PreviewPage(poco)
        with allure.step("直接点击下一步"):
            preview.click_submit()
        with allure.step("等待loading"):
            pubTool.wait_loading()
            assert_equal(pubTool.get_Routetitle(), "开始签署开户书", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))
        with allure.step("开始签署PDF"):
            preview.signPDF()
            pubTool.wait_loading()
            assert_equal(pubTool.get_Routetitle(), "开户书签署完成", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))
        with allure.step("开户书签署完成"):
            preview.completePDF()
            pubTool.wait_loading()
            assert_equal(pubTool.get_Routetitle(), "开户进度", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))





if __name__ == "__main__":
    pytest.main(["-s", "-v", "--pdb", "test_17_preview.py::Test_Preview", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()





