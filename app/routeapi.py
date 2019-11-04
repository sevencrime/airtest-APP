#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app
from test_case.test_01_open import Test_open
import pytest
import os
import re
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


def poco():
    # poco = AndroidUiautomationPoco(screenshot_each_action=False)

    readDeviceId = list(os.popen('adb devices').readlines())
    deviceId = re.findall(r'(.*)\tdevice', readDeviceId[1])

    if not cli_setup():
        try:
            subprocess.Popen("adb connect 127.0.0.1:7555", shell=True).wait(2)
        except:
            pass

        connect_device(
            "Android://127.0.0.1:5037/{device}?ori_method=ADBORI".format(device=''.join(deviceId)))

    driver = AndroidUiautomationPoco(force_restart=True)

    return driver

@app.route('/login', methods=['GET', 'POST'])
def login():

    print(poco())

    Test_open().test_Openning(poco())
    return "Hello"


if __name__ == "__main__":
    app.run(debug = True)
    # login()