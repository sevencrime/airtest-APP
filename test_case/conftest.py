import pytest
import os

from airtest.cli.parser import cli_setup
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from Commons.GlobalMap import GlobalMap


@pytest.fixture(scope="session", autouse=True)
def config():
    gm = GlobalMap()
    gm.set_bool(isbullion=False)
    gm.set_bool(isLeveraged=False)

@pytest.fixture(scope="session", autouse=True)
def poco():
    # os.popen("adb connect 127.0.0.1:7555")
    # poco = AndroidUiautomationPoco(screenshot_each_action=False)

    if not cli_setup():
        auto_setup(__file__, logdir=True,
                   devices=["Android:///", ])

    poco = AndroidUiautomationPoco(force_restart=True)
    return poco
