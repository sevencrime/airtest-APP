#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import allure
import pytest
from airtest.core.api import *

from Commons import CommonsTool
from Commons.CommonsTool import query_initialData
from Commons.GlobalMap import GlobalMap
from Commons.Logging import Logs
from Commons.mongoTool import mongoTool
from ElementPage.accountInformationPage import accountInformationPage
from ElementPage.publicTool import publicTool


@pytest.mark.run(order=7)
@allure.feature("账户信息")
class Test_AccountInformation():
    gm = GlobalMap()
    log = Logs()
    query_initialData()
    # mongo = mongoTool('mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net')

    @allure.story("填写账户信息--默认证券现金+期货")
    @pytest.mark.defaultType
    def test_Account(self, poco):
        # mongo = mongoTool(self.gm.get_value("mongohost"))
        pubTool = publicTool(poco)
        # pubTool.get_appcationNumber()
        accountinfo = accountInformationPage(poco)
        with allure.step("判断外汇账户和金业账户是否出现"):
            accountinfo.get_leverMargin()
            accountinfo.get_bullionMargin()

        with allure.step("选择账户类别"):
            # 
            pass
            # accountinfo.click_securitiesCash(True)
            # accountinfo.click_securitiesMargin(True)
            # accountinfo.click_futuresMargin(True)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

    @allure.story("勾选证券现金")
    @pytest.mark.securitiesCash
    def test_Account(self, poco):
        # mongo = mongoTool(self.gm.get_value("mongohost"))
        pubTool = publicTool(poco)
        # pubTool.get_appcationNumber()
        accountinfo = accountInformationPage(poco)
        with allure.step("判断外汇账户和金业账户是否出现"):
            accountinfo.get_leverMargin()
            accountinfo.get_bullionMargin()

        with allure.step("选择账户类别--证券现金"):
            accountinfo.click_securitiesCash(True)
            accountinfo.click_securitiesMargin(False)
            accountinfo.click_futuresMargin(False)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

    @allure.story("勾选证券保证金")
    @pytest.mark.securitiesMargin
    def test_Account(self, poco):
        # mongo = mongoTool(self.gm.get_value("mongohost"))
        pubTool = publicTool(poco)
        # pubTool.get_appcationNumber()
        accountinfo = accountInformationPage(poco)
        with allure.step("判断外汇账户和金业账户是否出现"):
            accountinfo.get_leverMargin()
            accountinfo.get_bullionMargin()

        with allure.step("选择账户类别--证券保证金"):
            accountinfo.click_securitiesCash(False)
            accountinfo.click_securitiesMargin(True)
            accountinfo.click_futuresMargin(False)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

    @allure.story("勾选期货账户")
    @pytest.mark.futuresMargin
    def test_Account(self, poco):
        # mongo = mongoTool(self.gm.get_value("mongohost"))
        pubTool = publicTool(poco)
        # pubTool.get_appcationNumber()
        accountinfo = accountInformationPage(poco)
        with allure.step("判断外汇账户和金业账户是否出现"):
            accountinfo.get_leverMargin()
            accountinfo.get_bullionMargin()

        with allure.step("选择账户类别--期货账户"):
            accountinfo.click_securitiesCash(False)
            accountinfo.click_securitiesMargin(False)
            accountinfo.click_futuresMargin(True)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()


    @allure.story("勾选证券保证金+期货账户")
    @pytest.mark.securitiesMargin_AND_futuresMargin
    def test_Account(self, poco):
        # mongo = mongoTool(self.gm.get_value("mongohost"))
        pubTool = publicTool(poco)
        # pubTool.get_appcationNumber()
        accountinfo = accountInformationPage(poco)
        with allure.step("判断外汇账户和金业账户是否出现"):
            accountinfo.get_leverMargin()
            accountinfo.get_bullionMargin()

        with allure.step("选择账户类别--期货账户"):
            accountinfo.click_securitiesCash(False)
            accountinfo.click_securitiesMargin(True)
            accountinfo.click_futuresMargin(True)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()



if __name__ == "__main__":
    pytest.main(["-s", "test_07_accountInformation.py::Test_AccountInformation", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()




