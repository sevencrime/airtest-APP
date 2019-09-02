#!/usr/bin/env python
# -*- coding: utf-8 -*-
import allure
import pytest
from airtest.core.api import *

from ElementPage.idcardPage import idcardPage
from ElementPage.publicTool import publicTool


@allure.feature("上传身份证")
class Test_uploadidcard():

    @allure.story("上传身份证")
    @pytest.mark.run(order=2)
    def test_uploadidcard(self, poco):
        upidcard = idcardPage(poco)
        pubTool = publicTool(poco)
        with allure.step("选择所属地区 -- 内地居民"):
            upidcard.click_Chinese()
        with allure.step("开户准备点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("上传身份证人像面"):
            upidcard.upload_idcardNegative

        with allure.step("上传身份证国徽面"):
            upidcard.upload_idcardpositive()

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()



if __name__ == "__main__":
    pytest.main(["-s", "test_02_uploadidcard.py", '--alluredir', '../report/xml'])
    # os.popen("allure generate {xml} -o {html} --clean".format(xml=os.getcwd() + r'\EDDID_APP\report\xml',
    #                                                           html=os.getcwd() + r'\EDDID_APP\report\html'))