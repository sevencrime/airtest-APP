#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import subprocess

import pytest

from Commons import CommonsTool

# 清理缓存数据
# subprocess.Popen(r"adb -s f7b6acb9 shell pm clear io.newtype.eddid.app").wait()
subprocess.Popen(r"adb shell pm clear io.newtype.eddid.app").wait()

# "--reruns=3", "--reruns-delay=3"  #重试
pytest.main(["-s", "-v", "./test_case/", '--alluredir',
             './report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')),
             # "--reruns=2",
             # "--reruns-delay=2",
             "--pdb"
             ])

xml_report_path, html_report_path = CommonsTool.rmdir5()
os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
    xml_report_path=xml_report_path, html_report_path=html_report_path)).read()
