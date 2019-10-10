#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import allure
import pytest

from ElementPage.customerStatementPage import customerStatementPage
from ElementPage.publicTool import publicTool

@allure.feature("其他资料")
class Test_CustomerStatement():

    @allure.story("其他资料")
    @pytest.mark.run(order=3)
    def test_otherData(self, poco):
        pubTool = publicTool(poco)
        customer = customerStatementPage(poco)

        with allure.step("勾选所有客户声明"):
            customer.click_CustomerStatement01()
            customer.click_CustomerStatement02()
            customer.click_CustomerStatement03()
            customer.click_CustomerStatement04()
            customer.click_CustomerStatement05()
            customer.click_CustomerStatement06()

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()



if __name__ == "__main__":
    pytest.main(["-s", "test_15_customerStatement.py", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])






