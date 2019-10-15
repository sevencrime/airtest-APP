#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import allure
import pytest
from Commons.GlobalMap import GlobalMap

from ElementPage.otherDataPage import otherDataPage
from ElementPage.publicTool import publicTool


@allure.feature("其他资料")
class Test_otherDataPage():

    fix_routetitle = ["其他资料"]

    @allure.story("其他资料")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_otherData(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        otherdata = otherDataPage(poco)
        with allure.step("您是否曾经宣告破产或被申请破产?"):
            otherdata.click_bankrupt(False)

        with allure.step("您是否艾德证券期货及/或艾德金业的雇员或任何其雇员的亲属?"):
            otherdata.click_customerRelatives(False)

        with allure.step("您是否与任何艾德证券期货及/或艾德金业客户有关连"):
            otherdata.click_associatedcustomer(False)

        with allure.step("您是否香港交易所之交易所参与者或证监会之持牌人或注册人之董事、雇员或认可人士"):
            otherdata.click_director(False)

        with allure.step("客户是否拥有美国公民或美国合法永久居民身份?"):
            otherdata.click_citizenOfUSA(False)

        with allure.step("就税务而言，您是否是美国居民?"):
            otherdata.click_americanResident(False)

        with allure.step("您是否香港法律定义下的“政治公众人物（PEP）”或与政治公众人物有密切联系"):
            otherdata.click_PEP_People(False)

        # with allure.step("滑动页面"):
        #     pubTool.swipe_to_Up()

        with allure.step("您的投资目标"):
            otherdata.click_investmentTarget(["投机", "对冲"])

        with allure.step("风险承受能力"):
            otherdata.click_riskTolerance(grade="高")

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()


if __name__ == "__main__":
    pytest.main(["-s", "test_13_otherData.py", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    gm = GlobalMap()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(xml_report_path=gm.get_value("xml_report_path"), html_report_path=gm.get_value("html_report_path"))).read()






