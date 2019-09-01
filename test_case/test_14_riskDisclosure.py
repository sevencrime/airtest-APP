#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest

from ElementPage.RiskDisclosurePage import RiskDisclosurePage
from ElementPage.otherDataPage import otherDataPage
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
    pytest.main(["-s", "test_14_riskDisclosure.py", '--alluredir', '../report/xml'])






