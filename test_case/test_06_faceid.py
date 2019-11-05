#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import allure
import pytest
from airtest.core.api import *

from Commons import CommonsTool
from Commons.GlobalMap import GlobalMap
from Commons.Logging import Logs
from Commons.mongoTool import mongoTool
from ElementPage.publicTool import publicTool


@allure.feature("人脸识别")
class Test_faceid():

    # mongo = mongoTool('mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net')
    gm = GlobalMap()
    log = Logs()
    fix_routetitle = ['人脸识别']

    @allure.story("人脸识别")
    @pytest.mark.usefixtures('reloadRoute')
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_bankCard(self, poco):
        mongo = mongoTool(self.gm.get_value("mongohost"))
        pubTool = publicTool(poco)
        pubTool.get_appcationNumber()
        with allure.step("修改数据库currentRoute"):
            # 判断申请编号, 判断是APP还是H5数据还是老版APP数据

            if self.gm.get_value("environment").find("aos") != -1:
                collection = "accounts"
                query = {"applyCode":self.gm.get_value("appcationNumber"),  "forLogin":True}
                setdata = {"$set": {"currentRoute": "/account"}}
            elif self.gm.get_value("environment") == "uat" != -1 or self.gm.get_value("environment") == "test" != -1:
                collection = "apply"
                query = {"applySeqId":self.gm.get_value("appcationNumber")}
                setdata = { "$set" : { "step" : "AccountInformation"} }
            else:
                self.log.debug("数据可能有问题哦!!!")


            mongo.UpdataData(database=self.gm.get_value("environment"), collection=collection , query=query, setdata = setdata)

        with allure.step("退出开户表单"):
            pubTool.closeform()

        with allure.step("重新进入表单"):
            pass



if __name__ == "__main__":
    pytest.main(["-s", "test_06_faceid.py", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()





