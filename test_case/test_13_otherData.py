#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import allure
import pytest
from Commons import CommonsTool
from airtest.core.api import *

from Commons.CommonsTool import isboolean, query_initialData
from Commons.GlobalMap import GlobalMap

from ElementPage.otherDataPage import otherDataPage
from ElementPage.publicTool import publicTool


@allure.feature("其他资料")
class Test_otherDataPage():

    gm = GlobalMap()
    fix_routetitle = ["其他资料"]
    query_initialData()
    boolset = isboolean(knowRisk=gm.get_value("knowRisk"), futures="futuresMargin" in gm.get_value("accountType"))

    @allure.story("其他资料")
    @allure.story("您是否曾经宣告破产或被申请破产提示")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_otherData_bankruptmsg(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        otherdata = otherDataPage(poco)
        with allure.step("您是否曾经宣告破产或被申请破产?"):
            otherdata.click_bankrupt(True)

        with allure.step("校验地址弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", "弹框标题有误")
            assert_equal(boxcontent, "如您曾经宣告破产或被申请破产，请联系客服", "弹框内容与填写内容不符")


    @allure.story("您是否艾德证券期货及/或艾德金业的雇员或任何其雇员的亲属?")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_otherData_customerRelativesmsg(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        otherdata = otherDataPage(poco)
        with allure.step("您是否艾德证券期货及/或艾德金业的雇员或任何其雇员的亲属?"):
            otherdata.click_customerRelatives(True)

        with allure.step("校验地址弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", "弹框标题有误")
            assert_equal(boxcontent, "如您是艾德证券期货的雇员或任何其雇员的亲属，请联系客服", "弹框内容与填写内容不符")


    @allure.story("您是否与任何艾德证券期货及/或艾德金业客户有关连")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_otherData_associatedcustomermsg(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        otherdata = otherDataPage(poco)
        with allure.step("您是否与任何艾德证券期货及/或艾德金业客户有关连"):
            otherdata.click_associatedcustomer(True)

        with allure.step("校验地址弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", "弹框标题有误")
            assert_equal(boxcontent, "如您与任何艾德证券期货客户有关连，请联系客服", "弹框内容与填写内容不符")


    @allure.story("您是否香港交易所之交易所参与者或证监会之持牌人或注册人之董事、雇员或认可人士")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_otherData_directormsg(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        otherdata = otherDataPage(poco)
        with allure.step("您是否香港交易所之交易所参与者或证监会之持牌人或注册人之董事、雇员或认可人士"):
            otherdata.click_director(True)

        with allure.step("校验地址弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", "弹框标题有误")
            assert_equal(boxcontent, "如您是香港交易所之交易所参与者或证监会之持牌人或注册人之董事、雇员或认可人士，请联系客服", "弹框内容与填写内容不符")


    @allure.story("客户是否拥有美国公民或美国合法永久居民身份?")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_otherData_citizenOfUSAmsg(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        otherdata = otherDataPage(poco)
        with allure.step("客户是否拥有美国公民或美国合法永久居民身份?"):
            otherdata.click_citizenOfUSA(True)

        with allure.step("校验地址弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", "弹框标题有误")
            assert_equal(boxcontent, "如您拥有美国公民或美国合法永久居民身份，请联系客服", "弹框内容与填写内容不符")


    @allure.story("就税务而言，您是否是美国居民?")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_otherData_americanResidentmsg(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        otherdata = otherDataPage(poco)
        with allure.step("就税务而言，您是否是美国居民?"):
            otherdata.click_americanResident(True)

        with allure.step("校验地址弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", "弹框标题有误")
            assert_equal(boxcontent, "如您就税务而言，您是否是美国居民，请联系客服", "弹框内容与填写内容不符")


    @allure.story("您是否香港法律定义下的“政治公众人物（PEP）”或与政治公众人物有密切联系")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_otherData_PEP_Peoplemsg(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        otherdata = otherDataPage(poco)
        with allure.step("您是否香港法律定义下的“政治公众人物（PEP）”或与政治公众人物有密切联系"):
            otherdata.click_PEP_People(True)

        with allure.step("校验地址弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", "弹框标题有误")
            assert_equal(boxcontent, "如您是香港法律定义下的“政治公众人物（PEP）”或与政治公众人物有密切联系，请联系客服", "弹框内容与填写内容不符")


    # 需判断期货或衍生产品是否勾选
    @allure.story("选择期货或衍生产品, 投资目标选择'利息/股息收入', 查看提示")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    @pytest.mark.skipif('knowRisk' not in boolset['True'] and 'futures' not in boolset['True'], reason="跳过用例")
    def test_otherData_investmentTargetMSG(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        otherdata = otherDataPage(poco)
        with allure.step("您是否曾经宣告破产或被申请破产?"):
            otherdata.click_bankrupt(False)

        with allure.step("您是否艾德证券期货及/或艾德金业的雇员或任何其雇员的亲属?"):
            otherdata.click_customerRelatives(False)

        with allure.step("您是否与任何艾德证券期货及/或艾德金业客户有关连"):
            otherdata.click_associatedcustomer(False)

        with allure.step("您是否香港交易所之交易所参与者或证监会之持牌人或注册人之董事、雇员或认可人士"):
            otherdata.click_director(False)

        with allure.step("客户是否拥有美国公民或美国合法永久居民身份?"):
            otherdata.click_citizenOfUSA(False)

        with allure.step("就税务而言，您是否是美国居民?"):
            otherdata.click_americanResident(False)

        with allure.step("您是否香港法律定义下的“政治公众人物（PEP）”或与政治公众人物有密切联系"):
            otherdata.click_PEP_People(False)

        with allure.step("您的投资目标"):
            otherdata.click_investmentTarget(["利息/股息收入"])

        with allure.step("风险承受能力"):
            otherdata.click_riskTolerance(grade="高")

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("校验弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", "弹框标题有误")
            assert_equal(boxcontent, "买卖期货、结构性产品及衍生产品并不适合投资目标仅为「利息/股息收入」人士。", "弹框内容与填写内容不符")


    # 同时勾选
    @allure.story("选择期货或衍生产品, 投资目标选择'利息/股息收入', 查看提示")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    @pytest.mark.skipif(not('knowRisk' in boolset['True'] and 'futures' in boolset['True']), reason="跳过用例")
    def test_otherData_derivatives_and_futures(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        otherdata = otherDataPage(poco)
        with allure.step("您是否曾经宣告破产或被申请破产?"):
            otherdata.click_bankrupt(False)

        with allure.step("您是否艾德证券期货及/或艾德金业的雇员或任何其雇员的亲属?"):
            otherdata.click_customerRelatives(False)

        with allure.step("您是否与任何艾德证券期货及/或艾德金业客户有关连"):
            otherdata.click_associatedcustomer(False)

        with allure.step("您是否香港交易所之交易所参与者或证监会之持牌人或注册人之董事、雇员或认可人士"):
            otherdata.click_director(False)

        with allure.step("客户是否拥有美国公民或美国合法永久居民身份?"):
            otherdata.click_citizenOfUSA(False)

        with allure.step("就税务而言，您是否是美国居民?"):
            otherdata.click_americanResident(False)

        with allure.step("您是否香港法律定义下的“政治公众人物（PEP）”或与政治公众人物有密切联系"):
            otherdata.click_PEP_People(False)

        with allure.step("您的投资目标"):
            otherdata.click_investmentTarget(["利息/股息收入", "对冲"])

        with allure.step("风险承受能力"):
            otherdata.click_riskTolerance(grade="低")

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("校验弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", "弹框标题有误")
            assert_equal(boxcontent, "期货买卖不适合风险承受能力为低之客户。结构性产品及衍生产品买卖不适合风险承受能力为低或中之客户", "弹框内容与填写内容不符")
            poco(text="知道了").click()

        with allure.step("再次点击风险承受能力"):
            otherdata.click_riskTolerance(grade="中")

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("再次校验弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", "弹框标题有误")
            assert_equal(boxcontent, "结构性产品及衍生产品买卖不适合风险承受能力为低或中之客户", "弹框内容与填写内容不符")


    # 只勾选期货
    @allure.story("选择期货或衍生产品, 投资目标选择'利息/股息收入', 查看提示")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    @pytest.mark.skipif(not('knowRisk' not in boolset['True'] and 'futures' in boolset['True']), reason="跳过用例")
    def test_otherData_futuresmsg(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        otherdata = otherDataPage(poco)
        with allure.step("您是否曾经宣告破产或被申请破产?"):
            otherdata.click_bankrupt(False)

        with allure.step("您是否艾德证券期货及/或艾德金业的雇员或任何其雇员的亲属?"):
            otherdata.click_customerRelatives(False)

        with allure.step("您是否与任何艾德证券期货及/或艾德金业客户有关连"):
            otherdata.click_associatedcustomer(False)

        with allure.step("您是否香港交易所之交易所参与者或证监会之持牌人或注册人之董事、雇员或认可人士"):
            otherdata.click_director(False)

        with allure.step("客户是否拥有美国公民或美国合法永久居民身份?"):
            otherdata.click_citizenOfUSA(False)

        with allure.step("就税务而言，您是否是美国居民?"):
            otherdata.click_americanResident(False)

        with allure.step("您是否香港法律定义下的“政治公众人物（PEP）”或与政治公众人物有密切联系"):
            otherdata.click_PEP_People(False)

        with allure.step("您的投资目标"):
            otherdata.click_investmentTarget(["利息/股息收入", "对冲"])

        with allure.step("风险承受能力"):
            otherdata.click_riskTolerance(grade="低")

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("校验弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", "弹框标题有误")
            assert_equal(boxcontent, "期货买卖不适合风险承受能力为低之客户", "弹框内容与填写内容不符")


    # 只勾选衍生产品
    @allure.story("选择期货或衍生产品, 投资目标选择'利息/股息收入', 查看提示")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    @pytest.mark.skipif(not('knowRisk' in boolset['True'] and 'futures' not in boolset['True']), reason="跳过用例")
    def test_otherData_derivatives(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        otherdata = otherDataPage(poco)
        with allure.step("您是否曾经宣告破产或被申请破产?"):
            otherdata.click_bankrupt(False)

        with allure.step("您是否艾德证券期货及/或艾德金业的雇员或任何其雇员的亲属?"):
            otherdata.click_customerRelatives(False)

        with allure.step("您是否与任何艾德证券期货及/或艾德金业客户有关连"):
            otherdata.click_associatedcustomer(False)

        with allure.step("您是否香港交易所之交易所参与者或证监会之持牌人或注册人之董事、雇员或认可人士"):
            otherdata.click_director(False)

        with allure.step("客户是否拥有美国公民或美国合法永久居民身份?"):
            otherdata.click_citizenOfUSA(False)

        with allure.step("就税务而言，您是否是美国居民?"):
            otherdata.click_americanResident(False)

        with allure.step("您是否香港法律定义下的“政治公众人物（PEP）”或与政治公众人物有密切联系"):
            otherdata.click_PEP_People(False)

        with allure.step("您的投资目标"):
            otherdata.click_investmentTarget(["利息/股息收入", "对冲"])

        with allure.step("风险承受能力"):
            otherdata.click_riskTolerance(grade="低")

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("校验弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", "弹框标题有误")
            assert_equal(boxcontent, "结构性产品及衍生产品买卖不适合风险承受能力为低或中之客户", "弹框内容与填写内容不符")
            poco(text="知道了").click()

        with allure.step("再次点击风险承受能力"):
            otherdata.click_riskTolerance(grade="中")

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()

        with allure.step("再次校验弹框标题和内容"):
            boxtitle, boxcontent = pubTool.get_boxtitle()
            assert_equal(boxtitle, "温馨提示", "弹框标题有误")
            assert_equal(boxcontent, "结构性产品及衍生产品买卖不适合风险承受能力为低或中之客户", "弹框内容与填写内容不符")


    @allure.story("其他资料, 正常输入")
    @pytest.mark.parametrize("reloadRoute", fix_routetitle, indirect=True)
    def test_otherData(self, poco, reloadRoute):
        pubTool = publicTool(poco)
        otherdata = otherDataPage(poco)
        with allure.step("您是否曾经宣告破产或被申请破产?"):
            otherdata.click_bankrupt(False)

        with allure.step("您是否艾德证券期货及/或艾德金业的雇员或任何其雇员的亲属?"):
            otherdata.click_customerRelatives(False)

        with allure.step("您是否与任何艾德证券期货及/或艾德金业客户有关连"):
            otherdata.click_associatedcustomer(False)

        with allure.step("您是否香港交易所之交易所参与者或证监会之持牌人或注册人之董事、雇员或认可人士"):
            otherdata.click_director(False)

        with allure.step("客户是否拥有美国公民或美国合法永久居民身份?"):
            otherdata.click_citizenOfUSA(False)

        with allure.step("就税务而言，您是否是美国居民?"):
            otherdata.click_americanResident(False)

        with allure.step("您是否香港法律定义下的“政治公众人物（PEP）”或与政治公众人物有密切联系"):
            otherdata.click_PEP_People(False)

        # with allure.step("滑动页面"):
        #     pubTool.swipe_to_Up()

        with allure.step("您的投资目标"):
            otherdata.click_investmentTarget(["投机", "对冲"])

        with allure.step("风险承受能力"):
            otherdata.click_riskTolerance(grade="高")

        with allure.step("点击下一步"):
            pubTool.click_NextStepbtn()


if __name__ == "__main__":
    pytest.main(["-s", "-v", "--pdb", "test_13_otherData.py::Test_otherDataPage::test_otherData_investmentTargetMSG", '--alluredir', '../report/xml_{time}'.format(time=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))])
    xml_report_path, html_report_path = CommonsTool.rmdir5()
    os.popen("allure generate {xml_report_path} -o {html_report_path} --clean".format(
        xml_report_path=xml_report_path, html_report_path=html_report_path)).read()





