#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os

import allure
import pytest

from Commons import CommonsTool
from ElementPage.RiskDisclosurePage import RiskDisclosurePage
from ElementPage.publicTool import publicTool


@allure.feature("风险披露")
class Test_riskDisclosure():

    @allure.story("风险披露")
    @pytest.mark.run(order=3)
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




if __name__ == "__main__":
    pytest.main(["-s", "test_14_riskDisclosure.py", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()





