#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import allure
import pytest

from Commons import CommonsTool
from ElementPage.introPromoPage import introPromoPage
from ElementPage.publicTool import publicTool
from airtest.core.api import *

@allure.feature("介绍与推广")
@pytest.mark.usefixtures('query_initialData')
class Test_channels():
    fix_routetitle = ["介绍及推广"]

    @allure.story("介绍与推广, 不勾选>>必须勾选才能下一步")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_sendtransaction(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        channel = introPromoPage(poco)
        with allure.step("您透过哪些渠道认识艾德证券期货及/或艾德金业?(选择所有适用)"):

            channels = channel.click_Channels(["网上广告", "讲座"])
            # assert_equal(employ, "无业", "就业情况信息填写有误")

        with allure.step("勾选本人同意艾德证券如上述情况使用本人的个人资料"):
            channel.click_personalInfoDeclartionLangsasImgview(False)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()
            assert_equal(pubTool.get_Routetitle(), "介绍及推广", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))


    @allure.story("介绍与推广, 勾选 >> 必须勾选才能下一步")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_personalInfoDeclartionasY(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        channel = introPromoPage(poco)
        with allure.step("您透过哪些渠道认识艾德证券期货及/或艾德金业?(选择所有适用)"):
            channels = channel.click_Channels(["网上广告", "讲座", "报纸"])
            # assert_equal(employ, "无业", "就业情况信息填写有误")

        with allure.step("勾选本人同意艾德证券如上述情况使用本人的个人资料"):
            channel.click_personalInfoDeclartionLangsasImgview(True)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()
            assert_equal(pubTool.get_Routetitle(), "衍生品产品认识", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))






if __name__ == "__main__":
    pytest.main(["-s", "-v","test_10_channels.py::Test_channels", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()




