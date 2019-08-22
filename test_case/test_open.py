#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pytest
from airtest.core.api import *

class Test_open():

    def test_s3(self, poco):

        start_app("io.newtype.eddid.app")

        poco(text="开户").click()
        poco(text="便捷开户").click()
        poco(text="去登录").click()
        poco(text="请输入手机号").set_text("15089514626")
        poco(text="请输入密码").set_text("abcd1234")

        poco("android.widget.ScrollView").child("android.widget.TextView").child("android.view.ViewGroup").child(
            "android.widget.TextView", text="登录")


if __name__ == "__main__":
    pytest.main(["-s", "test_open.py"])