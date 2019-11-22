#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os

import allure
import pytest
from airtest.core.api import *

from Commons import CommonsTool
from Commons.CommonsTool import query_initialData
from Commons.GlobalMap import GlobalMap
from ElementPage.financialPage import financialPage
from ElementPage.publicTool import publicTool


@pytest.mark.run(order=12)
@allure.feature("相关保证金融资账户")
class Test_financial():

    gm = GlobalMap()
    query_initialData()
    fix_routetitle = ["相关保证金融资账户"]

    @pytest.fixture()
    def teardown(self):
        # 三个配偶信息
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


    # @allure.story("从底部开始输入")
    # @pytest.mark.usefixtures('teardown')
    # @pytest.mark.skipif(gm.get_value("Routetitle") == "其他资料", reason="有值了, 跳过")
    # @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    # def test_derivative_reverseRun(self, poco, reloadRoute):
    #     pubTool = publicTool(poco)
    #     financial = financialPage(poco)
    #
    #     financial.click_orderPerson(False)



    @allure.story("没有勾选(证券保证金), 正常输入")
    @pytest.mark.parametrize("accountHolder", [True, False])
    @pytest.mark.parametrize("orderPerson", [True, False])
    @pytest.mark.usefixtures('teardown')
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    @pytest.mark.skipif("securitiesMargin" in gm.get_value("accountType"), reason="勾选了证券保证金")
    def test_derivative(self, poco, reloadRoute, orderPerson, accountHolder):
        pubTool = publicTool(poco)
        financial = financialPage(poco)
        with allure.step("您是否是账户的最终实益拥有人? "):
            financial.click_accountHolder(accountHolder)

        with allure.step("校验最终实益拥有人是否触发弹框 "):
            if not accountHolder:
                # 校验弹框      
                boxtitle, boxcontent = pubTool.get_boxtitle()
                assert_equal(boxtitle, "温馨提示", "相关保证金融资账户弹框标题有误")
                assert_equal(boxcontent, "如您并非账户的最终实益拥有人，请联络我们的客服: +852 3896 6333 或电邮：cs@eddid.com.hk", "弹框内容与填写内容不符")
                poco(text="知道了").click()

        with allure.step("您是否是最终负责下单的人?? "):
            financial.click_orderPerson(orderPerson)

        with allure.step("校验最终负责下单人是否触发弹框? "):
            if not orderPerson:
                boxtitle, boxcontent = pubTool.get_boxtitle()
                assert_equal(boxtitle, "温馨提示", "相关保证金融资账户弹框标题有误")
                if not accountHolder:
                    assert_equal(boxcontent, "如您并非账户的最终实益拥有人，请联络我们的客服: +852 3896 6333 或电邮：cs@eddid.com.hk", "弹框内容与填写内容不符")
                else:
                    assert_equal(boxcontent, "如您并非账户最终下单人，请联络我们的客服: +852 3896 6333 或电邮：cs@eddid.com.hk", "弹框内容与填写内容不符")
                    
                poco(text="知道了").click()

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()
            if accountHolder and orderPerson:
                assert_equal(pubTool.get_Routetitle(), "其他资料", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))
            else:
                assert_equal(pubTool.get_Routetitle(), "相关保证金融资账户", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))



    @allure.story("勾选(证券保证金), 正常输入")
    @pytest.mark.parametrize("isMarginAccount", [True, False])
    @pytest.mark.parametrize("isDiscretion", [True, False])
    @pytest.mark.parametrize("isCompanyAccounts", [True, False])
    @pytest.mark.parametrize("accountHolder", [True, False])
    @pytest.mark.parametrize("orderPerson", [True, False])
    @pytest.mark.usefixtures('teardown')
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    @pytest.mark.skipif("securitiesMargin" not in gm.get_value("accountType"), reason="没有勾选证券保证金")
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
            financial.click_isCompanyAccounts(isCompanyAccounts)
            pubTool.swipe_to_Up()
            financial.send_AccountName()
            financial.send_AccountNumber()

        with allure.step("您是否是账户的最终实益拥有人? "):
            financial.click_accountHolder(accountHolder)

        with allure.step("校验最终实益拥有人是否触发弹框 "):
            if not accountHolder:
                # 校验弹框      
                boxtitle, boxcontent = pubTool.get_boxtitle()
                assert_equal(boxtitle, "温馨提示", "相关保证金融资账户弹框标题有误")
                assert_equal(boxcontent, "如您并非账户的最终实益拥有人，请联络我们的客服: +852 3896 6333 或电邮：cs@eddid.com.hk", "弹框内容与填写内容不符")
                poco(text="知道了").click()

        with allure.step("您是否是最终负责下单的人?? "):
            financial.click_orderPerson(orderPerson)

        with allure.step("校验最终负责下单人是否触发弹框? "):
            if not orderPerson:
                boxtitle, boxcontent = pubTool.get_boxtitle()
                assert_equal(boxtitle, "温馨提示", "相关保证金融资账户弹框标题有误")
                assert_equal(boxcontent, "如您并非账户最终下单人，请联络我们的客服: +852 3896 6333 或电邮：cs@eddid.com.hk", "弹框内容与填写内容不符")
                poco(text="知道了").click()


        with allure.step("点击下一步"):
            # pubTool.swipe_to_Up()
            pubTool.click_NextStepbtn()
            if accountHolder and orderPerson:
                assert_equal(pubTool.get_Routetitle(), "其他资料", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))
            else:
                assert_equal(pubTool.get_Routetitle(), "相关保证金融资账户", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))




if __name__ == "__main__":
    pytest.main(["-s", "-v", "--pdb", "test_12_financial.py::Test_financial", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()





