#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import sys
import os
import allure
import pytest
from airtest.core.api import *

from Commons import CommonsTool
from Commons.GlobalMap import GlobalMap
from Commons.Logging import Logs
from ElementPage.bankCardInformationPage import bankCardInformationPage
from ElementPage.publicTool import publicTool


@allure.feature("银行卡信息")
class Test_bankCardInformation():
    log = Logs()
    fix_routetitle = ["银行卡信息"]

    @allure.story("内地银行卡号非空校验")
    @pytest.mark.usefixtures('reloadRoute')
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_bankCardnullvalue(self, poco):
        self.log.debug("正在执行{} 方法".format(sys._getframe().f_code.co_name, ))
        pubTool = publicTool(poco)
        bankcard = bankCardInformationPage(poco)
        with allure.step("输入卡号"):
            bankcard.send_bankCardNo(bankNo="")

        with allure.step("输入银行名称"):
            bankcard.send_bankName()

        with allure.step("输入绑定手机号"):
            bankcard.send_bankPhone()

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("页面停留在<银行卡信息>界面"):
            assert_equal(pubTool.get_Routetitle(), "银行卡信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))

    @allure.story("内地银行卡号输入中文")
    @pytest.mark.usefixtures('reloadRoute')
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_bankCard_sendChinese(self, poco):
        self.log.debug("正在执行{} 方法".format(sys._getframe().f_code.co_name, ))
        pubTool = publicTool(poco)
        bankcard = bankCardInformationPage(poco)
        with allure.step("输入卡号"):
            bankcard.send_bankCardNo(bankNo="内地银行卡号")

        with allure.step("输入银行名称"):
            bankcard.send_bankName()

        with allure.step("输入绑定手机号"):
            bankcard.send_bankPhone()

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("校验弹框内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", msg="银行卡信息界面弹框标题有误")
            assert_equal(boxcontent, "卡号只能输入数字", msg="银行卡信息界面弹框内容有误")
            # 关闭弹框
            pubTool.click_box()

        with allure.step("页面停留在<银行卡信息>界面"):
            assert_equal(pubTool.get_Routetitle(), "银行卡信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))

    @allure.story("内地银行卡号输入组合字符")
    @pytest.mark.usefixtures('reloadRoute')
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_bankCard_sendAll(self, poco):
        self.log.debug("正在执行{} 方法".format(sys._getframe().f_code.co_name, ))
        pubTool = publicTool(poco)
        bankcard = bankCardInformationPage(poco)
        with allure.step("输入卡号"):
            bankcard.send_bankCardNo(bankNo="内地abc123,./")

        with allure.step("输入银行名称"):
            bankcard.send_bankName()

        with allure.step("输入绑定手机号"):
            bankcard.send_bankPhone()

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("校验弹框内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", msg="银行卡信息界面弹框标题有误")
            assert_equal(boxcontent, "卡号只能输入数字", msg="银行卡信息界面弹框内容有误")
            # 关闭弹框
            pubTool.click_box()


        with allure.step("页面停留在<银行卡信息>界面"):
            assert_equal(pubTool.get_Routetitle(), "银行卡信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))


    @allure.story("银行名称输入空值")
    @pytest.mark.usefixtures('reloadRoute')
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_bankCardnameNull(self, poco):
        self.log.debug("正在执行{} 方法".format(sys._getframe().f_code.co_name, ))
        pubTool = publicTool(poco)
        bankcard = bankCardInformationPage(poco)
        with allure.step("输入卡号"):
            bankcard.send_bankCardNo()

        with allure.step("输入银行名称"):
            bankcard.send_bankName("")

        with allure.step("输入绑定手机号"):
            bankcard.send_bankPhone()

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("页面停留在<银行卡信息>界面"):
            assert_equal(pubTool.get_Routetitle(), "银行卡信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))

    @allure.story("银行名称输入组合字符")
    @pytest.mark.usefixtures('reloadRoute')
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_bankCardname_sendAll(self, poco):
        self.log.debug("正在执行{} 方法".format(sys._getframe().f_code.co_name, ))
        pubTool = publicTool(poco)
        bankcard = bankCardInformationPage(poco)
        with allure.step("输入卡号"):
            bankcard.send_bankCardNo()

        with allure.step("输入银行名称"):
            bankcard.send_bankName("中国银行abc123.,/@")

        with allure.step("输入绑定手机号"):
            bankcard.send_bankPhone()

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("页面跳转到人脸识别界面"):
            assert_equal(pubTool.get_Routetitle(), "人脸识别", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))

        with allure.step("点击返回按钮返回银行卡信息界面"):
            pubTool.backform()
            assert_equal(pubTool.get_Routetitle(), "银行卡信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))

    @allure.story("绑定手机号不填")
    @pytest.mark.usefixtures('reloadRoute')
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_bankCardPhone_Null(self, poco):
        self.log.debug("正在执行{} 方法".format(sys._getframe().f_code.co_name, ))
        pubTool = publicTool(poco)
        bankcard = bankCardInformationPage(poco)
        with allure.step("输入卡号"):
            bankcard.send_bankCardNo()

        with allure.step("输入银行名称"):
            bankcard.send_bankName()

        with allure.step("输入绑定手机号"):
            bankcard.send_bankPhone("")

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("页面停留在<银行卡信息>界面"):
            assert_equal(pubTool.get_Routetitle(), "银行卡信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))

    @allure.story("绑定手机号输入中文")
    @pytest.mark.usefixtures('reloadRoute')
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_bankCardPhone_sendChinese(self, poco):
        self.log.debug("正在执行{} 方法".format(sys._getframe().f_code.co_name, ))
        pubTool = publicTool(poco)
        bankcard = bankCardInformationPage(poco)
        with allure.step("输入卡号"):
            bankcard.send_bankCardNo()

        with allure.step("输入银行名称"):
            bankcard.send_bankName()

        with allure.step("输入绑定手机号"):
            bankcard.send_bankPhone("手机号")

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("校验弹框内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", msg="银行卡信息界面弹框标题有误")
            assert_equal(boxcontent, "绑定手机号只能输入数字", msg="银行卡信息界面弹框内容有误")
            # 关闭弹框
            pubTool.click_box()

        with allure.step("页面停留在<银行卡信息>界面"):
            assert_equal(pubTool.get_Routetitle(), "银行卡信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))


    @allure.story("绑定手机号输入组合字符")
    @pytest.mark.usefixtures('reloadRoute')
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_bankCardPhone_sendAll(self, poco):
        self.log.debug("正在执行{} 方法".format(sys._getframe().f_code.co_name, ))
        pubTool = publicTool(poco)
        bankcard = bankCardInformationPage(poco)
        with allure.step("输入卡号"):
            bankcard.send_bankCardNo()

        with allure.step("输入银行名称"):
            bankcard.send_bankName()

        with allure.step("输入绑定手机号"):
            bankcard.send_bankPhone("手机号123abc,./")

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("校验弹框内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", msg="银行卡信息界面弹框标题有误")
            assert_equal(boxcontent, "绑定手机号只能输入数字", msg="银行卡信息界面弹框内容有误")
            # 关闭弹框
            pubTool.click_box()

        with allure.step("页面停留在<银行卡信息>界面"):
            assert_equal(pubTool.get_Routetitle(), "银行卡信息", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))



if __name__ == "__main__":
    pytest.main(["-s", "-v", "test_05_bankCardInformation.py::Test_bankCardInformation", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()




