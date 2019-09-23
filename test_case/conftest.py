import pytest
import os
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from Commons.GlobalMap import GlobalMap


@pytest.fixture(scope="session", autouse=True)
def config():
    gm = GlobalMap()
    gm.set_value(environment="aos-uat")
    gm.set_value(appApi="aos")
    gm.set_bool(isbullion=False)
    gm.set_bool(isLeveraged=False)
    gm.set_List(istotalAnnual=[])

@pytest.fixture(scope="session", autouse=True)
def poco():
    # os.popen("adb connect 127.0.0.1:7555")
    # poco = AndroidUiautomationPoco(screenshot_each_action=False)

    if not cli_setup():
        auto_setup(__file__, logdir=True,
                   devices=["Android:///", ])

    poco = AndroidUiautomationPoco(force_restart=True)
    yield poco

    # from airtest.report.report import simple_report
    # simple_report(__file__)

    # 当前目录
    curPath = os.path.abspath(os.path.dirname(__file__))
    # 项目根目录
    rootPath = curPath[:curPath.find("airtest-APP\\") + len("airtest-APP\\")]

    # import pdb; pdb.set_trace()
    xml_report_path = rootPath + r'report\xml'
    html_report_path = rootPath + r'report\html'

    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(xml_report_path=xml_report_path, html_report_path=html_report_path)).read()


