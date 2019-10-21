#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import pytest
import allure
from Commons.GlobalMap import GlobalMap

if __name__ == "__main__":
    pytest.main(["-s", "-v", "./test_case", "--pdb", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    gm = GlobalMap()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(xml_report_path=gm.get_value("xml_report_path"), html_report_path=gm.get_value("html_report_path"))).read()

