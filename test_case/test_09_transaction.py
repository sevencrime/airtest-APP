#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest

from ElementPage.publicTool import publicTool
from ElementPage.transactionPage import transactionPage


@allure.feature("就业信息")
class Test_transaction():

    @allure.story("选择交易信息")
    @pytest.mark.run(order=3)
    def test_sendtransaction(self, poco):
        pubtool = publicTool(poco)
        transac = transactionPage(poco)
        with allure.step("输入交易资金/财富来源"):
            employ = transac.click_fundsSource(["储蓄"])
            # assert_equal(employ, "无业", "就业情况信息填写有误")

        with allure.step("点击下一步"):
            pubtool.click_NextStepbtn()


if __name__ == "__main__":
    pytest.main(["-s", "test_09_transaction.py", '--alluredir', '../report/xml'])






