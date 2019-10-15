import allure
import pytest
import os
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from Commons.GlobalMap import GlobalMap
from Commons.Logging import Logs
from Commons.mongoTool import mongoTool
from ElementPage.publicTool import publicTool


gm = GlobalMap()
gm._init()
log = Logs()

@pytest.fixture(scope="class")
def query_initialData():
    """
    # 查询数据库获取初始值

    textMatches: 模糊匹配
    """
    # gm = GlobalMap()
    # log = Logs()
    global gm

    mongo = mongoTool(gm.get_value("mongohost"))

    totalAnnuallist = []  # 存放全年总收入的初始值
    customerNetAssetValuelist = []  # 存放资产净值的初始值
    fundsSourcelist = []  # 交易的资金/财富来源(选择所有适用)

    # 查询数据库获取全年总收入和资产净值的字段
    result = mongo.findData(gm.get_value("environment"), "accounts", {
                            'phone': "15089514626", 'forLogin': True})

    totalAnnualdict = {
        "pension": "退休金",
        "returnOnInvestment": "投资回报",
        "rent": "租金",
        "other": "其他",
        "salary": "薪金",
        "commission": "佣金",
        "selfOperatedBusinessIncome": "自营业务收益",

    }

    customerNetAssetValuedict = {
        "salary": "薪金",
        "propertyInvestment": "物业投资",
        "vehicleInvestment": "车辆投资",
        "savings": "储蓄",
        "stockOrBondInvestment": "股票/债券投资",
        "heritage": "遗产",
        "other": "其他",
        "selfOperatedBusinessIncome": "自营业务收益",
        "pension": "退休金",

    }

    fundsSourcedict = {
        "deposit": "储蓄",
        "selfOperatedBusinessIncome": "自营业务收益",
        "investment": "投资",
        "other": "其他",
        "salary": "薪金",
        "pension": "退休金",
    }

    # 全年总收入
    for totalAnnual in result['totalAnnualCustomerRevenueHKSource']:
        if totalAnnualdict.__contains__(totalAnnual):
            totalAnnuallist.append(totalAnnualdict[totalAnnual])

    # 资产净值
    for customerNetAssetValue in result['customerNetAssetValueHKSource']:
        if customerNetAssetValuedict.__contains__(customerNetAssetValue):
            customerNetAssetValuelist.append(
                customerNetAssetValuedict[customerNetAssetValue])

    # 财富来源
    for fundsSource in result['fundsSource']:
        if fundsSourcedict.__contains__(fundsSource):
            fundsSourcelist.append(fundsSourcedict[fundsSource])

    if result['isLearnAboutProducts'] == 'Y' and result['isIndustryExperience'] == 'Y' and result['isStocks'] == 'Y' and result['isApplyProduct'] == 'Y' and result['knowRisk'] == 'Y':
        gm.set_bool(derivative=True)

    gm.set_List('istotalAnnual', totalAnnuallist)
    gm.set_List('customerNetAssetValue', customerNetAssetValuelist)
    gm.set_List('fundsSource', fundsSourcelist)


    log.debug("istotalAnnual的值为:" + "".join(gm.get_value("istotalAnnual")))
    log.debug("customerNetAssetValue的值为:" +
              "".join(gm.get_value("customerNetAssetValue")))
    log.debug("fundsSource的值为:" + "".join(gm.get_value("fundsSource")))


@pytest.fixture()
def reloadRoute(request, poco):
    """
    # 退出重新加载页面, 清除页面前端缓存

    """

    global gm

    routetitle = request.param
    pubTool = publicTool(poco)
    # 点击退出按钮后, 再次进入开户表单
    pubTool.closeform()
    pubTool.wait_loading()

    # 获取标题
    gm.set_value(Routetitle=pubTool.get_Routetitle())

    # 判断当前标题, 如不是操作界面, 则点击返回按钮
    if routetitle != pubTool.get_Routetitle():
        pubTool.backform()



@pytest.fixture(scope="session", autouse=True)
def config():
    global gm
    gm.set_value(environment="aos-uat")     # 记录数据库
    gm.set_bool(isbullion=False)        # 记录黄金账户是否开启
    gm.set_bool(isLeveraged=False)      # 记录外汇账户是否开启
    # mongo数据库地址
    gm.set_value(
        mongohost="mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net")


@pytest.fixture(scope="session", autouse=True)
def poco():
    # poco = AndroidUiautomationPoco(screenshot_each_action=False)

    # if not cli_setup():
    #     auto_setup(__file__, logdir=True,
    #                devices=["Android:///", ])

    if not cli_setup():
        # 模拟器 >> 网易mumu模拟器连接cap_method=JAVACAP&&ori_method=ADBORI
        os.popen("adb connect 127.0.0.1:7555").read()
        connect_device(
            "Android://127.0.0.1:5037/127.0.0.1:7555?ori_method=ADBORI")

    poco = AndroidUiautomationPoco(force_restart=True)
    pubTool = publicTool(poco)
    # report限制5条
    pubTool.rmdir5()

    yield poco

    # from airtest.report.report import simple_report
    # simple_report(__file__)
    # os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
    #     xml_report_path=xml_report_path, html_report_path=html_report_path)).read()
