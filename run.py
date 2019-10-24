#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import pytest
import allure

from Commons import CommonsTool

if __name__ == "__main__":
    # "--reruns=3", "--reruns-delay=3"  #重试
    pytest.main(["-s", "-v", "./test_case", '--alluredir',
                 './report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')), "--reruns=3",
                 "--reruns-delay=3"])

    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()
