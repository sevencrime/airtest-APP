#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import pytest
import allure
from Commons.GlobalMap import GlobalMap

if __name__ == "__main__":
    pytest.main(["-s", "-v", "./test_case/test_01_open.py", '--alluredir',
                 './report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')),
                 "--reruns=3", "--reruns-delay=3"])
    gm = GlobalMap()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=gm.get_value("xml_report_path"), html_report_path=gm.get_value("html_report_path"))).read()
