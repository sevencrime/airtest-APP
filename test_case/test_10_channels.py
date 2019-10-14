#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import allure
import pytest

from ElementPage.introPromoPage import introPromoPage
from ElementPage.publicTool import publicTool
from ElementPage.transactionPage import transactionPage


@allure.feature("介绍与推广")
@pytest.mark.usefixtures('query_initialData')
class Test_channels():
    fix_routetitle = ["介绍与推广"]

    @allure.story("介绍与推广")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_sendtransaction(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        channel = introPromoPage(poco)
        with allure.step("您透过哪些渠道认识艾德证券期货及/或艾德金业?(选择所有适用)"):

            channels = channel.click_Channels(["网上广告", "讲座"])
            # assert_equal(employ, "无业", "就业情况信息填写有误")

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()



if __name__ == "__main__":
    pytest.main(["-s", "test_10_channels.py", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    gm = GlobalMap()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(xml_report_path=gm.get_value("xml_report_path"), html_report_path=gm.get_value("html_report_path"))).read()





