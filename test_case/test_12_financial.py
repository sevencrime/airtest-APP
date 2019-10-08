#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from airtest.core.api import *
from ElementPage.financialPage import financialPage
from ElementPage.publicTool import publicTool

@allure.feature("相关保证金融资账户")
class Test_financial():

    fix_routetitle = ["相关保证金融资账户"]

    @allure.story("没有勾选(证券保证金), 正常输入")
    @pytest.mark.parametrize("accountHolder", [True, False])
    @pytest.mark.parametrize("orderPerson", [True, False])
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_derivative(self, poco, reloadRoute, orderPerson, accountHolder):
        pubTool = publicTool(poco)
        financial = financialPage(poco)
        with allure.step("您是否是账户的最终实益拥有人? "):
            financial.click_accountHolder(True)

        with allure.step("您是否是最终负责下单的人?? "):
            financial.click_orderPerson(True)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()
            assert_equal(pubTool.get_Routetitle(), "其他资料", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))



    @allure.story("勾选(证券保证金), 正常输入")
    @pytest.mark.parametrize("accountHolder", [True, False])
    @pytest.mark.parametrize("orderPerson", [True, False])
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    @pytest.mark.skipif()
    def test_derivative(self, poco, reloadRoute, orderPerson, accountHolder):
        pubTool = publicTool(poco)
        financial = financialPage(poco)
        with allure.step("您是否是账户的最终实益拥有人? "):
            financial.click_accountHolder(True)

        with allure.step("您是否是最终负责下单的人?? "):
            financial.click_orderPerson(True)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()
            assert_equal(pubTool.get_Routetitle(), "其他资料", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))






if __name__ == "__main__":
    pytest.main(["-s", "test_12_financial.py", '--alluredir', '../report/xml'])






