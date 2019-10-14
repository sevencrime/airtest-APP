#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import allure
import pytest
from airtest.core.api import *

from Commons.GlobalMap import GlobalMap
from ElementPage.idcardPage import idcardPage
from ElementPage.personalInformationPage import personalInformationPage
from ElementPage.publicTool import publicTool


@allure.feature("上传身份证")
class Test_uploadidcard():
    gm = GlobalMap()
    fix_routetitle = ["身份证验证"]

    @allure.story("上传身份证")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_uploadidcard(self, poco, reloadRoute):
        upidcard = idcardPage(poco)
        pubTool = publicTool(poco)

        # 判断客户来源
        pubTool.get_appcationNumber()

        with allure.step("选择所属地区 -- 内地居民"):
            upidcard.click_Chinese()

        with allure.step("上传身份证人像面"):
            upidcard.upload_idcardNegative()
            pubTool.wait_loading()

        with allure.step("上传身份证国徽面"):
            upidcard.upload_idcardpositive()
            pubTool.wait_loading()

        with allure.step("滑动页面"):
            assert_equal(pubTool.get_Routetitle(), "身份证验证", msg="页面没有跳转")
            poco("android:id/content").swipe([0.25, -0.9])

        if self.gm.get_value("environment").find("aos") != -1:
            # 输入email
            perinfo = personalInformationPage(poco)

            with allure.step("输入电邮"):
                email = perinfo.send_emali()
            with allure.step("再次输入电邮"):
                reEmail = perinfo.send_reemail()

            with allure.step("点击下一步"):
                pubTool.click_NextStepbtn()

            with allure.step("校验地址弹框标题和内容"):
                # import pdb; pdb.set_trace()
                boxtitle, boxcontent = pubTool.get_boxtitle()
                assert_equal(boxtitle, "请确认您的身份证地址", "确认地址弹框标题有误")
                assert_equal(boxcontent, perinfo.get_address(), "弹框内容与填写内容不符")

            with allure.step("确认地址弹框--点击确定"):
                pubTool.click_boxconfirm()

            with allure.step("页面跳转到<银行卡信息>界面"):
                assert_equal(pubTool.get_Routetitle(), "银行卡信息", msg="页面没有跳转")


        else:
            with allure.step("点击下一步"):
                pubTool.click_NextStepbtn()



if __name__ == "__main__":
    pytest.main(["-s", "--pdb","test_02_uploadidcard.py", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    gm = GlobalMap()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(xml_report_path=gm.get_value("xml_report_path"), html_report_path=gm.get_value("html_report_path"))).read()
