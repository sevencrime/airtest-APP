#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

    @allure.story("上传身份证")
    @pytest.mark.run(order=2)
    def test_uploadidcard(self, poco):
        upidcard = idcardPage(poco)
        pubTool = publicTool(poco)

        # 判断客户来源
        pubTool.customersource()

        # with allure.step("选择所属地区 -- 内地居民"):
        #     upidcard.click_Chinese()
        # with allure.step("开户准备点击下一步"):
        #     pubTool.click_NextStepbtn()

        with allure.step("上传身份证人像面"):
            upidcard.upload_idcardNegative()
            # pubTool.wait_loading()

        with allure.step("上传身份证国徽面"):
            upidcard.upload_idcardpositive()
            # pubTool.wait_loading()

        with allure.step("滑动页面"):
            time.sleep(5)
            poco("android:id/content").swipe([0.25, -0.9])

        if self.gm.get_value("appApi") == "aos":
            # 输入email
            perinfo = personalInformationPage(poco)

            with allure.step("输入电邮"):
                email = perinfo.send_emali()
            with allure.step("再次输入电邮"):
                reEmail = perinfo.send_reemail()

            with allure.step("点击下一步"):
                # import pdb; pdb.set_trace()
                pubTool.click_NextStepbtn()

            # with allure.step("校验地址弹框标题和内容"):
            #     boxtitle = pubTool.get_boxtitle()
            #     boxcontent = pubTool.get_boxcontent()
            #     assert_equal(boxtitle, "请确认您的身份证地址", "确认地址弹框标题有误")
            #     assert_equal(boxcontent, perinfo.get_address(), "弹框内容与填写内容不符")
            #
            # with allure.step("确认地址弹框--点击确定"):
            #     pubTool.click_boxconfirm()

        else:
            with allure.step("点击下一步"):
                pubTool.click_NextStepbtn()



if __name__ == "__main__":
    pytest.main(["-s", "test_02_uploadidcard.py", '--alluredir', '../report/xml'])
    # os.popen("allure generate {xml} -o {html} --clean".format(xml=os.getcwd() + r'\EDDID_APP\report\xml',
    #                                                           html=os.getcwd() + r'\EDDID_APP\report\html'))