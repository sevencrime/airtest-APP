#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import pytest
from Commons import CommonsTool
from Commons.CommonsTool import query_initialData

if __name__ == "__main__":
    # query_initialData("run.py")

    # "--reruns=3", "--reruns-delay=3"  #重试
    pytest.main(["-s", "-v", "./test_case/", '--alluredir',
                 './report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')), "--reruns=2",
                 "--reruns-delay=3"])

    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()
