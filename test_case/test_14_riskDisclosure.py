#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import allure
import pytest
from airtest.core.api import *

from Commons import CommonsTool
from ElementPage.RiskDisclosurePage import RiskDisclosurePage
from ElementPage.publicTool import publicTool


@pytest.mark.run(order=14)
@allure.feature("风险披露")
class Test_riskDisclosure():

    @allure.story("风险披露")
    def test_otherData(self, poco):
        pubTool = publicTool(poco)
        riskdisclosure = RiskDisclosurePage(poco)
        with allure.step("点击按钮开始播放音频"):
            riskdisclosure.click_player()

        with allure.step("拖动音频进度条"):
            riskdisclosure.drag_progressbar()

        with allure.step("勾选复选框, 明白风险"):
            riskdisclosure.click_isUnderstandRisk()

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()
            assert_equal(pubTool.get_Routetitle(), "客户声明", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))



if __name__ == "__main__":
    pytest.main(["-s", "test_14_riskDisclosure.py", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()





