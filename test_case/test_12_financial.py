#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from airtest.core.api import *

from Commons.GlobalMap import GlobalMap
from ElementPage.financialPage import financialPage
from ElementPage.publicTool import publicTool

@allure.feature("相关保证金融资账户")
class Test_financial():

    gm = GlobalMap()
    fix_routetitle = ["相关保证金融资账户"]

    @pytest.fixture()
    def teardown(self):
        self.gm.set_bool(MarginAccountName=False)
        self.gm.set_bool(MarginAccountNumber=False)
        self.gm.set_bool(iscretionAccountName=False)
        self.gm.set_bool(iscretionAccountNumber=False)
        self.gm.set_bool(CompanyAccountsAccountName=False)
        self.gm.set_bool(CompanyAccountsAccountNumber=False)
        yield
        self.gm.set_bool(MarginAccountName=False)
        self.gm.set_bool(MarginAccountNumber=False)
        self.gm.set_bool(iscretionAccountName=False)
        self.gm.set_bool(iscretionAccountNumber=False)
        self.gm.set_bool(CompanyAccountsAccountName=False)
        self.gm.set_bool(CompanyAccountsAccountNumber=False)


    @allure.story("没有勾选(证券保证金), 正常输入")
    @pytest.mark.parametrize("accountHolder", [True, False])
    @pytest.mark.parametrize("orderPerson", [True, False])
    @pytest.mark.usefixtures('teardown')
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
    @pytest.mark.parametrize("isMarginAccount", [True, False])
    @pytest.mark.parametrize("isDiscretion", [True, False])
    @pytest.mark.parametrize("isCompanyAccounts", [True, False])
    @pytest.mark.parametrize("accountHolder", [True, False])
    @pytest.mark.parametrize("orderPerson", [True, False])
    @pytest.mark.usefixtures('teardown')
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_derivative_securitiesMargin(self, poco, reloadRoute, orderPerson, accountHolder, isCompanyAccounts, isDiscretion, isMarginAccount):
        pubTool = publicTool(poco)
        financial = financialPage(poco)
        with allure.step("您的配偶是否持有艾德证券任何相关的保证金账户?"):
            financial.click_isMarginAccount(isMarginAccount)
            financial.send_AccountName()
            financial.send_AccountNumber()

        with allure.step("您或您的配偶是否单独或共同控制艾德证券之其他保证金账户35%或以上之表决权?"):
            financial.click_isDiscretion(isDiscretion)
            financial.send_AccountName()
            financial.send_AccountNumber()


        with allure.step("您是否有以客户的同一集团公司旗下之公司开立保证金账户？"):
            pubTool.swipe_to_Up()
            financial.click_isCompanyAccounts(isCompanyAccounts)
            pubTool.swipe_to_Up()
            financial.send_AccountName()
            financial.send_AccountNumber()


        with allure.step("您是否是账户的最终实益拥有人? "):
            pubTool.swipe_to_Up()
            financial.click_accountHolder(accountHolder)

        with allure.step("您是否是最终负责下单的人?? "):
            pubTool.swipe_to_Up()
            financial.click_orderPerson(orderPerson)

        with allure.step("点击下一步"):
            pubTool.swipe_to_Up()
            pubTool.click_NextStepbtn()
            assert_equal(pubTool.get_Routetitle(), "其他资料", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))






if __name__ == "__main__":
    pytest.main(["-s", "-v", "--pdb", "test_12_financial.py::Test_financial::test_derivative_securitiesMargin", '--alluredir', '../report/xml'])






