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
from ElementPage.personalInformationPage import personalInformationPage
from ElementPage.publicTool import publicTool

@pytest.mark.run(order=3)
@allure.feature("请填写个人资料")
class Test_personalinfomation():
    gm = GlobalMap()
    query_initialData()
    fix_routetitle = ["请填写个人资料"]

    @allure.story("填写个人资料-正常输入")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    @pytest.mark.skipif(gm.get_value("environment").find("aos") != -1, reason="后台是aos接口, 没有该页面, 跳过此用例")
    def test_personal(self, poco, reloadRoute):

        perinfo = personalInformationPage(poco)
        pubTool = publicTool(poco)
        with allure.step("输入电邮"):
            email = perinfo.send_emali()
        with allure.step("再次输入电邮"):
            reEmail = perinfo.send_reemail()
        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("校验地址弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "请确认您的身份证地址", "确认地址弹框标题有误")
            assert_equal(boxcontent, perinfo.get_address(), "弹框内容与填写内容不符")


        with allure.step("确认地址弹框--点击确定"):
            pubTool.click_boxconfirm()

    @allure.story("填写个人资料-邮箱格式不正确")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    @pytest.mark.dependency(depends=["Test_uploadidcard::test_uploadidcard"])
    @pytest.mark.skipif(gm.get_value("environment").find("aos") != -1, reason="后台是aos接口, 没有该页面, 跳过此用例")
    def test_personal_Emailformat(self, poco, reloadRoute):
        pubTool = publicTool(poco)

        perinfo = personalInformationPage(poco)

        with allure.step("输入非邮箱格式的email"):
            perinfo.send_emali("onedi")
            perinfo.send_reemail("onedi")

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()
            # pubTool.wait_loading()

        with allure.step("校验地址弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", "确认地址弹框标题有误")
            assert_equal(boxcontent, "邮件格式不正确", "弹框内容与填写内容不符")

        with allure.step("关闭弹框"):
            pubTool.click_box()

    @allure.story("填写个人资料-邮箱不一致")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    @pytest.mark.dependency(depends=["Test_uploadidcard::test_uploadidcard"])
    @pytest.mark.skipif(gm.get_value("environment").find("aos") != -1, reason="后台是aos接口, 没有该页面, 跳过此用例")
    def test_personal_disEmail(self, poco, reloadRoute):
        pubTool = publicTool(poco)

        perinfo = personalInformationPage(poco)

        with allure.step("两次邮箱不一致"):
            perinfo.send_emali("onedi@qq.cn")
            perinfo.send_reemail("onedi@qq.com")

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()
            # pubTool.wait_loading()

        with allure.step("校验地址弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", "确认地址弹框标题有误")
            assert_equal(boxcontent, "两次邮箱输入不一致", "弹框内容与填写内容不符")

        with allure.step("关闭弹框"):
            pubTool.click_box()

    @allure.story("填写个人资料-邮箱已存在")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    @pytest.mark.dependency(depends=["Test_uploadidcard::test_uploadidcard"])
    @pytest.mark.skipif(gm.get_value("environment").find("aos") != -1, reason="后台是aos接口, 没有该页面, 跳过此用例")
    def test__personalEmail_exists(self, poco, reloadRoute):
        pubTool = publicTool(poco)

        perinfo = personalInformationPage(poco)

        with allure.step("校验邮箱是否存在"):
            perinfo.send_emali("5555@qq.com")
            perinfo.send_reemail("5555@qq.com")

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()
            # pubTool.wait_loading()

        with allure.step("校验地址弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", "确认地址弹框标题有误")
            assert_equal(boxcontent, "电邮已存在", "弹框内容与填写内容不符")

        with allure.step("关闭弹框"):
            pubTool.click_box()


    @allure.story("填写个人资料-电话号码已存在")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    @pytest.mark.dependency(depends=["Test_uploadidcard::test_uploadidcard"])
    @pytest.mark.skipif(gm.get_value("environment").find("aos") != -1, reason="后台是aos接口, 没有该页面, 跳过此用例")
    def test_personal_phoneExists(self, poco, reloadRoute):
        pubTool = publicTool(poco)

        perinfo = personalInformationPage(poco)

        with allure.step("输入正常邮箱"):
            perinfo.send_emali("onedi@qq.com")
            perinfo.send_reemail("onedi@qq.com")

        with allure.step("输入重复的电话号码"):
            perinfo.modify_phone(True, "321321")

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()
            # pubTool.wait_loading()

        with allure.step("校验地址弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", "确认地址弹框标题有误")
            assert_equal(boxcontent, "电话号码(用于通讯)已存在", "弹框内容与填写内容不符")

        with allure.step("关闭弹框"):
            pubTool.click_box()



    @allure.story("填写个人资料-勾选住址和身份证地址不一致")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    @pytest.mark.dependency(depends=["Test_uploadidcard::test_uploadidcard"])
    @pytest.mark.skipif(gm.get_value("environment").find("aos") != -1, reason="后台是aos接口, 没有该页面, 跳过此用例")
    def test_personal_pick_isaddress(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        perinfo = personalInformationPage(poco)
        with allure.step("勾选住址与身份证地址不一致"):
            perinfo.click_isAddress(True)

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()
            pubTool.wait_loading()

        with allure.step("页面跳转到<住址信息>界面"):
            assert_equal(pubTool.get_Routetitle(), "住址信息", msg="页面没有跳转")

        with allure.step("点击返回按钮返回身份证界面"):
            pubTool.backform()
            assert_equal(pubTool.get_Routetitle(), "请填写个人资料", msg="页面跳转到{}页面".format(pubTool.get_Routetitle()))


if __name__ == "__main__":
    pytest.main(["-s", "-v", "--pdb", "test_03_personalinfomation.py::Test_personalinfomation", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()