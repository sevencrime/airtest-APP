#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import shutil
import sys
import traceback

import pytest
from airtest.core.api import *
from pymongo.errors import ServerSelectionTimeoutError

from Commons.GlobalMap import GlobalMap
from Commons.Logging import Logs
from Commons.mongoTool import mongoTool
from ElementPage.publicTool import publicTool

gm = GlobalMap()
log = Logs()

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("airtest-APP\\") + len("airtest-APP\\")]


def rmdir5():

    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = curPath[:curPath.find("airtest-APP\\") + len("airtest-APP\\")]
    xml_report_pathlib = glob.glob(rootPath + r'report\\xml*')
    html_report_pathlib = glob.glob(rootPath + r'report\\html*')

    try:
        html_report_name = rootPath + r'report\html' + os.path.basename(xml_report_pathlib[-1])[3:]

    except IndexError:
        log.debug("调用 <rmdir5> 方法的是: {}".format(traceback.extract_stack()[-2][2]))
        log.error("rmdir5, 数组越界")

    except Exception as e:
        raise e

    # 判断文件目录是否超过5个
    # 生成后才调用该方法, 所以要+1
    if len(xml_report_pathlib) >= 6:
        # shutil模块, 文件高级库
        shutil.rmtree(xml_report_pathlib[0])

    if len(html_report_pathlib) >= 5:
        # 删除第一个
        shutil.rmtree(html_report_pathlib[0])

    # self.gm.set_value(xml_report_path=xml_report_pathlib[-1])
    # self.gm.set_value(html_report_path=html_report_name)
    return xml_report_pathlib[-1], html_report_name



def isboolean(**kwargs):

    set_true = set()   # 存放为true的字段
    set_false = set()  # 存放为False的字段
    booleanlist = {}

    for key_, value_ in kwargs.items():
        if value_ :
            set_true.add(key_)
        else:
            set_false.add(key_)


    booleanlist['True'] = set_true
    booleanlist['False'] = set_false
    return booleanlist



def query_initialData():
    """
    # 查询数据库获取初始值

    textMatches: 模糊匹配
    """
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
                result = mongo.findData(gm.get_value("environment"), "accounts", {
                    'phone': gm.get_value("phone"), 'forLogin': True})

                # result = mongo.findData(gm.get_value("environment"), "accounts", {
                #     'phone': publicTool(poco).get_appcationNumber(), 'forLogin': True})


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
                                             {'$match': {"applySeqId": gm.get_value("appcationNumber")}},
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

