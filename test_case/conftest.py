import datetime
import re
import subprocess
import sys
import traceback

import allure
import pytest
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from pymongo.errors import ServerSelectionTimeoutError

from Commons.GlobalMap import GlobalMap
from Commons.Logging import Logs
from Commons.mongoTool import mongoTool
from ElementPage.publicTool import publicTool

gm = GlobalMap()
log = Logs()
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("airtest-APP\\") + len("airtest-APP\\")]


@pytest.fixture(scope="class")
def query_initialData(poco):
    """
    # 查询数据库获取初始值

    textMatches: 模糊匹配
    """
    # gm = GlobalMap()
    # log = Logs()
    log.debug("正在执行{} 方法".format(sys._getframe().f_code.co_name))
    mongo = mongoTool(gm.get_value("mongohost"))

    totalAnnuallist = []  # 存放全年总收入的初始值
    customerNetAssetValuelist = []  # 存放资产净值的初始值
    fundsSourcelist = []  # 交易的资金/财富来源(选择所有适用)
    channelslist = []   #认识渠道
    investmentTargetlist = [] #投资目标

    if gm.get_value("environment").find("aos") != -1:
        # 查询数据库获取全年总收入和资产净值的字段
        for i in range(3):
            try:
                # result = mongo.findData(gm.get_value("environment"), "accounts", {
                #     'phone': gm.get_value("phone"), 'forLogin': True})

                result = mongo.findData(gm.get_value("environment"), "accounts", {
                    'applyCode': publicTool(poco).get_appcationNumber(), 'forLogin': True})


            except ServerSelectionTimeoutError:
                time.sleep(3)
                continue

            break


    elif gm.get_value("environment") == "test" and gm.get_value("environment") == "uat":
        # result = mongo.findData(gm.get_value("environment"), "apply", {
        # "applySeqId" : publicTool(poco).get_appcationNumber()})
        for i in range(3):
            try:
                result = mongo.aggregate(gm.get_value("environment"),
                                         "apply", [
                                             {'$match': {"applySeqId": publicTool(poco).get_appcationNumber()}},
                                             {'$lookup': {'from': 'apply_info', 'localField': 'applyInfoIds',
                                                          'foreignField': '_id', 'as': 'applyInfos'}},
                                             {'$unwind': '$applyInfos'},
                                             {'$match': {'applyInfos.isMaster': '1'}}
                                         ]
                                         )
            except ServerSelectionTimeoutError:
                time.sleep(3)
                continue

            break


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

    # 您透过哪些渠道认识艾德证券?(选择所有适用)
    crm_channelsdict = {
        "advertising" : "网上广告", 
        "lecture" : "讲座", 
        "friend" : "朋友", 
        "searchEngine" : "搜索引擎", 
        "newspaper" : "报纸", 
        'magazine' : '杂志',
        'forum' : '论坛',
        'socialMedia' : '社交媒体',
        'other' : '其他'
    }


    aos_channelsdict = {
        "onlineAd" : "网上广告", 
        "lecture" : "讲座", 
        "friend" : "朋友", 
        "searchEngine" : "搜索引擎", 
        "newspaper" : "报纸", 
        'magazine' : '杂志',
        'forum' : '论坛',
        'socialMedia' : '社交媒体',
        'other' : '其他'
    }

    investmentTargetdict= {
        "speculation" : "投机",
        "hedging" : "对冲",
        "asset" : "资产增值",
        "income" : "利息/股息收入"
    }



    if gm.get_value("environment").find("aos") != -1:
        # 全年总收入
        for totalAnnual in result['totalAnnualCustomerRevenueHKSource']:
            if totalAnnualdict.__contains__(totalAnnual):
                totalAnnuallist.append(
                    totalAnnualdict[totalAnnual])

        # 资产净值
        for customerNetAssetValue in result['customerNetAssetValueHKSource']:
            if customerNetAssetValuedict.__contains__(customerNetAssetValue):
                customerNetAssetValuelist.append(
                    customerNetAssetValuedict[customerNetAssetValue])

        # 财富来源
        for fundsSource in result['fundsSource']:
            if fundsSourcedict.__contains__(fundsSource):
                fundsSourcelist.append(fundsSourcedict[fundsSource])

        for channe in result['channels']:
            if aos_channelsdict.__contains__(channe):
                channelslist.append(aos_channelsdict[channe])


        for investment in result['investmentTarget']:
            if investmentTargetdict.__contains__(investment):
                investmentTargetlist.append(investmentTargetdict[investment])

        import pdb; pdb.set_trace()
        try:
            if result['isLearnAboutProducts'] != '' and result['isIndustryExperience'] != '' and result['isStocks'] != '' and result['isApplyProduct'] != '':
                gm.set_bool(derivative=True)    # 衍生产品
            else:
                gm.set_bool(derivative=False)
        except:
            gm.set_bool(derivative=False)


        try:
            if result['knowRisk'] == 'Y' or result['knowRisk'] == True:
                gm.set_bool(knowRisk=True)
            else:
                gm.set_bool(knowRisk=False)
        except:
            gm.set_bool(knowRisk=False)


        try:
            gm.set_bool(sameAdderss=result['sameAddress'])  # sameAdderss: 住址与身份证不一致, ture为勾选
        except Exception as e:
            # raise e
            gm.set_bool(sameAdderss=False)

        gm.set_List('accountType', result['accountTypes'])  # 账户类型

    elif gm.get_value("environment") == "test" and gm.get_value("environment") == "uat":
        # 全年总收入
        for totalAnnual in result['applyInfos']['riskInfo']['totalAnnualCustomerRevenueHKSource']:
            if totalAnnualdict.__contains__(totalAnnual):
                totalAnnuallist.append(totalAnnualdict[totalAnnual])

        # 资产净值
        for customerNetAssetValue in result['applyInfos']['riskInfo']['customerNetAssetValueHKSource']:
            if customerNetAssetValuedict.__contains__(customerNetAssetValue):
                customerNetAssetValuelist.append(
                    customerNetAssetValuedict[customerNetAssetValue])

        # 财富来源
        for fundsSource in result['applyInfos']['riskInfo']['sourceOfWealth']:
            if fundsSourcedict.__contains__(fundsSource):
                fundsSourcelist.append(fundsSourcedict[fundsSource])

        for channe in result['channels']:
            if crm_channelsdict.__contains__(channe):
                channelslist.append(crm_channelsdict[channe])

        for investment in result['purposeOfInvestment']:
            if investmentTargetdict.__contains__(investment):
                investmentTargetlist.append(investmentTargetdict[investment])

        try:
            if result['applyInfos']['riskInfo']['isLearnAboutProducts'] != '' and result['applyInfos']['riskInfo'][
                'isIndustryExperience'] != '' and result['applyInfos']['riskInfo']['isStocks'] != '' and \
                    result['applyInfos']['riskInfo']['isApplyToOpenTradingStructure'] != '' and \
                    result['applyInfos']['riskInfo']['isTradingStructureAggree'] != '':
                gm.set_bool(derivative=True)    # 衍生产品
            else:
                gm.set_bool(derivative=False)

        except:
            gm.set_bool(derivative=False)

        gm.set_bool(sameAdderss=result['applyInfos']['syncIDAddress'] == "Y")  # sameAdderss: 住址与身份证不一致, ture为勾选
        gm.set_List('accountType', result['accountType'])   # 账户类型

    gm.set_List('istotalAnnual', totalAnnuallist)
    gm.set_List('customerNetAssetValue', customerNetAssetValuelist)
    gm.set_List('fundsSource', fundsSourcelist)     # 财富来源
    gm.set_List('channels', channelslist)   # 认识渠道
    gm.set_List("investmentTarget", investmentTargetlist)   #投资目标


    log.debug("istotalAnnual的值为:" + "".join(gm.get_value("istotalAnnual")))
    log.debug("customerNetAssetValue的值为:" +
              "".join(gm.get_value("customerNetAssetValue")))
    log.debug("fundsSource的值为:" + "".join(gm.get_value("fundsSource")))
    log.debug("认识渠道的值为:" + "".join(gm.get_value("channels")))
    log.debug("结构性衍生产品相关风险声明披露字段的值为 knowRisk : {}".format(gm.get_value("knowRisk")))

@pytest.fixture()
def reloadRoute(request, poco):
    """
    # 退出重新加载页面, 清除页面前端缓存

    """

    routetitle = request.param
    pubTool = publicTool(poco)

    start = time.time()
    while poco(text="取消").exists():
        poco(text="取消").click()
        if time.time() - start > 20:
            break

    start1 = time.time()
    while poco(text="知道了").exists():
        poco(text="知道了").click()
        if time.time() - start1 > 20:
            break

    # 点击退出按钮后, 再次进入开户表单
    pubTool.closeform()
    pubTool.wait_loading()
    title = pubTool.get_Routetitle()
    # 获取标题
    gm.set_value(Routetitle=title)
    log.debug("当前的页面标题为: {}".format(title))

    # 判断当前标题, 如不是操作界面, 则点击返回按钮
    if routetitle != pubTool.get_Routetitle():
        pubTool.backform()


@pytest.fixture(scope="session", autouse=True)
def config():
    gm.set_value(environment="aos-uat")  # 记录数据库
    gm.set_value(phone = "13148814889")
    gm.set_bool(isbullion=False)  # 记录黄金账户是否开启
    gm.set_bool(isLeveraged=False)  # 记录外汇账户是否开启
    # mongo数据库地址
    gm.set_value(
        mongohost="mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net")


@pytest.fixture(scope="session", autouse=True)
def poco(config):
    # poco = AndroidUiautomationPoco(screenshot_each_action=False)

    readDeviceId = list(os.popen('adb devices').readlines())
    deviceId = re.findall(r'(.*)\tdevice', readDeviceId[1])

    # if not cli_setup():
    #     auto_setup(__file__, logdir=True,
    #                devices=["Android:///", ])

    if not cli_setup():
        # 模拟器 >> 网易mumu模拟器连接cap_method=JAVACAP&&ori_method=ADBORI
        try:
            subprocess.Popen("adb connect 127.0.0.1:7555", shell=True).wait(2)
        except:
            pass
        # connect_device(
        #     "Android://127.0.0.1:5037/127.0.0.1:7555?ori_method=ADBORI")

        connect_device(
            "Android://127.0.0.1:5037/{device}?ori_method=ADBORI".format(device=''.join(deviceId)))

        # auto_setup(basedir=__file__,
        #            devices = ["Android://127.0.0.1:5037/127.0.0.1:7555?ori_method=ADBORI"],
        #            logdir=rootPath+'airlog')

    poco = AndroidUiautomationPoco(force_restart=True)
    gm.set_bool(poco=poco)  # 全局poco

    yield poco


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    '''
    捕获测试用例结果
    :param item:
    :param call:
    :return:
    '''
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    if rep.when == 'call':
        if rep.failed:
            print("我已经捕获失败了")
            nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            # 截图
            subprocess.Popen(
                r"adb -s {driver} shell screencap -p /sdcard/Pictures/screen{time}.png".format(driver=device().uuid,time=nowtime),shell=True).wait()

            if os.path.exists(rootPath + "Logs/error_screenIMG") is False:
                os.makedirs(rootPath + "Logs/error_screenIMG")

            # pull
            subprocess.Popen(
                r"adb -s {driver} pull /sdcard/Pictures/screen{time}.png {pngfile}".format(driver=device().uuid,
                                                                                            time=nowtime,pngfile=rootPath + "Logs/error_screenIMG"),shell=True).wait()

            # 删除
            subprocess.Popen(r"adb -s {driver} shell rm /sdcard/Pictures/screen{time}.png".format(driver=device().uuid,time=nowtime),shell=True).wait()


            testimg = open(rootPath + "Logs/error_screenIMG/screen{time}.png".format(time=nowtime), 'rb').read()
            # allure.attach(body, name, attachment_type, extension)
            # body - 要写入文件的原始内容。
            # name - 包含文件名的字符串
            # attachment_type - 其中一个allure.attachment_type值
            # extension - 提供的将用作创建文件的扩展名
            allure.attach(testimg, "screen", allure.attachment_type.PNG)


        elif rep.passed:
            pass
