import pytest
import os
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from Commons.GlobalMap import GlobalMap
from Commons.Logging import Logs
from Commons.mongoTool import mongoTool
from ElementPage.publicTool import publicTool


@pytest.fixture(scope="class")
def get_totalAnnual_AND_customerNetAssetValue():
    """
    # 获取就业界面: 全年总收入和资产净值的初始值

    textMatches: 模糊匹配
    """

    gm = GlobalMap()
    log = Logs()
    mongo = mongoTool(gm.get_value("mongohost"))


    totalAnnuallist = []  # 存放全年总收入的初始值
    customerNetAssetValuelist = []  # 存放资产净值的初始值

    # 查询数据库获取全年总收入和资产净值的字段
    result = mongo.findData(gm.get_value("environment"), "accounts", {'phone': "15089514626", 'forLogin': True})

    for totalAnnual in result['totalAnnualCustomerRevenueHKSource']:
        if totalAnnual == 'pension':
            totalAnnuallist.append('退休金')

        if totalAnnual == 'returnOnInvestment':
            totalAnnuallist.append('投资回报')

        if totalAnnual == 'rent':
            totalAnnuallist.append('租金')

        if totalAnnual == 'other':
            totalAnnuallist.append('其他')

        if totalAnnual == 'salary':
            totalAnnuallist.append('薪金')

        if totalAnnual == 'commission':
            totalAnnuallist.append('佣金')

        if totalAnnual == 'selfOperatedBusinessIncome':
            totalAnnuallist.append('自营业务收益')

    for customerNetAssetValue in result['customerNetAssetValueHKSource']:
        if customerNetAssetValue == 'salary':
            customerNetAssetValuelist.append('薪金')

        if customerNetAssetValue == 'propertyInvestment':
            customerNetAssetValuelist.append('物业投资')

        if customerNetAssetValue == 'vehicleInvestment':
            customerNetAssetValuelist.append('车辆投资')

        if customerNetAssetValue == 'savings':
            customerNetAssetValuelist.append('储蓄')

        if customerNetAssetValue == 'stockOrBondInvestment':
            customerNetAssetValuelist.append('股票/债券投资')

        if customerNetAssetValue == 'heritage':
            customerNetAssetValuelist.append('遗产')

        if customerNetAssetValue == 'other':
            customerNetAssetValuelist.append('其他')

        if customerNetAssetValue == 'selfOperatedBusinessIncome':
            customerNetAssetValuelist.append('自营业务收益')

        if customerNetAssetValue == 'pension':
            customerNetAssetValuelist.append('退休金')

    gm.set_List('istotalAnnual', totalAnnuallist)
    gm.set_List('customerNetAssetValue', customerNetAssetValuelist)

    log.debug("istotalAnnual的值为:" + "".join(gm.get_value("istotalAnnual")))
    log.debug("customerNetAssetValue的值为:" + "".join(gm.get_value("customerNetAssetValue")))


@pytest.fixture(scope="session", autouse=True)
def config():
    gm = GlobalMap()
    gm.set_value(environment="aos-uat")
    gm.set_value(appApi="aos")
    gm.set_bool(isbullion=False)
    gm.set_bool(isLeveraged=False)
    gm.set_value(mongohost="mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net")

@pytest.fixture(scope="session", autouse=True)
def poco():
    # os.popen("adb connect 127.0.0.1:7555")
    # poco = AndroidUiautomationPoco(screenshot_each_action=False)

    if not cli_setup():
        auto_setup(__file__, logdir=True,
                   devices=["Android:///", ])

    # connect_device("android://127.0.0.1:5037/127.0.0.1:7555?cap_method=javacap&touch_method=adb")

    poco = AndroidUiautomationPoco(force_restart=True)
    yield poco

    # from airtest.report.report import simple_report
    # simple_report(__file__)

    # # 当前目录
    # curPath = os.path.abspath(os.path.dirname(__file__))
    # # 项目根目录
    # rootPath = curPath[:curPath.find("airtest-APP\\") + len("airtest-APP\\")]
    #
    # # import pdb; pdb.set_trace()
    # xml_report_path = rootPath + r'report\xml'
    # html_report_path = rootPath + r'report\html'
    #
    # os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(xml_report_path=xml_report_path, html_report_path=html_report_path)).read()


@pytest.fixture(scope="class")
def reloadRoute(request, poco):

    routetitle = request.param
    pubTool = publicTool(poco)
    # 点击退出按钮后, 再次进入开户表单
    pubTool.closeform()

    # 判断当前标题, 如不是操作界面, 则点击返回按钮
    if routetitle != pubTool.get_Routetitle:
        pubTool.backform()

