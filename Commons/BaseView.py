#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from Commons.GlobalMap import GlobalMap
from Commons.Logging import Logs


class BaseView():

    gm = GlobalMap()
    log = Logs()

    def __init__(self, poco):
        self.poco = poco
        # 当前目录
        curPath = os.path.abspath(os.path.dirname(__file__))
        # 项目根目录
        rootPath = curPath[:curPath.find("airtest-APP\\") + len("airtest-APP\\")]

        # 公用
        self.nextStepbtn = self.poco(text="下一步").parent()
        self.boxCancel = self.poco(text="取消")
        self.boxconfirm = self.poco(text="确定")
        self.gallery = self.poco(text="相册选取")
        self.loading = self.poco("android.widget.ProgressBar")
        self.Routetitle = self.poco("android.widget.FrameLayout").offspring("android.widget.TextView")
        self.permission_allow_button = self.poco("com.android.packageinstaller:id/permission_allow_button", text="始终允许")
        self.permission_title = self.poco("com.android.packageinstaller:id/permission_title")

        self.closeform_img = rootPath + r'testData\testIMG\closeform.png'
        self.backform_img = rootPath + r'testData\testIMG\backform.png'

        self.el_firstSetting_loc = self.poco("io.newtype.eddid.app:id/btn_start")
        self.baropen = self.poco(text="开户")
        self.easyOpenning = self.poco(text="便捷开户")
        self.goLogin = self.poco(text="去登录")
        self.phonenumber = self.poco(text="请输入手机号")

        self.el_chinese = self.poco(text="我是内地居民")
        self.el_idcardNegative = self.poco(text="请上传身份证人像面")
        self.el_idcardpositive = self.poco(text="请上传身份证国徽面")

        # 采用图片识别方式上传身份证
        self.idcardimgpath_img = rootPath + r'testData\\testIMG\\idcardFolder.png'
        self.idcardimgnegative_img = rootPath + r'testData\\testIMG\\idcardimgnegative.png'
        self.idcardimgpositive_img = rootPath + r'testData\\testIMG\\idcardimgpositive.png'

        # 个人信息界面
        self.el_chinesename = self.poco(text="中文姓名").sibling("android.widget.EditText")
        self.el_lastname = self.poco(text="姓氏").sibling("android.widget.EditText")
        self.el_firstname = self.poco(text="名字").sibling("android.widget.EditText")
        self.el_email = self.poco(text="电邮").sibling("android.widget.EditText")
        self.el_reEmail = self.poco(text="再次输入电邮").sibling("android.widget.EditText")
        self.el_phone = self.poco(text="电话号码(用于通讯)").sibling("android.widget.EditText")
        self.el_idNumber = self.poco(text="证件号码").sibling("android.widget.EditText")
        self.el_iDcardAddress = self.poco(text="身份证地址(*请确认地址无误，如有误请手动修改)").sibling("android.widget.EditText")
        self.el_FalseiDcardAddress = self.poco(text="如住址和身份证地址不一致(请勾选)").sibling("android.widget.ImageView")

        # 银行卡信息
        self.el_bankCardNo = self.poco(text="卡号").sibling("android.widget.EditText")
        self.el_bankName = self.poco(text="银行名称").sibling("android.widget.EditText")
        self.el_bankPhone = self.poco(text="绑定手机号").sibling("android.widget.EditText")

        # 账户信息
        self.el_accountType = self.poco(text="账户类型").sibling("android.widget.TextView")
        self.el_accountopeningway = self.poco(text="开户方法").sibling("android.widget.TextView")
        self.el_securitiesCash = self.poco(text="香港及环球证券账户(现金)").sibling("android.widget.ImageView")
        self.el_securitiesMargin = self.poco(text="香港及环球证券账户(保证金)").sibling("android.widget.ImageView")
        self.el_futuresMargin = self.poco(text="香港及环球期货账户(保证金)").sibling("android.widget.ImageView")
        self.el_leverMargin = self.poco(text="杠杆式外汇账户(保证金)").sibling("android.widget.ImageView")
        self.el_bullionMargin = self.poco(text="艾德金业现货黄金账户(保证金)").sibling("android.widget.ImageView")

        # 就业情况
        self.el_employ = self.poco(text="就业情况").sibling("android.view.ViewGroup").offspring("android.widget.TextView")
        self.position = self.poco(text="职位").sibling("android.widget.EditText")
        self.BusinessNature = self.poco(text="业务性质").sibling("android.widget.EditText")
        self.companyName = self.poco(text="公司名称").sibling("android.widget.EditText")
        self.employmenTime = self.poco(text="受雇年期").sibling("android.view.ViewGroup").offspring("android.widget.TextView")
        self.el_officeaddr = self.poco(text="办公室地址").parent().sibling("android.widget.EditText")
        self.totalAnnualCustomerRevenueHK = self.poco(text="全年总收入(港元)").sibling("android.view.ViewGroup").offspring("android.widget.TextView")
        self.customerNetAssetValueHK = self.poco(text="资产净值(港元)").sibling("android.view.ViewGroup").offspring("android.widget.TextView")
        self.sourcesfunds = self.poco(text="请注明资金来源(可多选)")
        self.assetsvalue = self.poco(text="请注明资产净值来源(可多选)")
        self.otherfunds = self.poco(text="请输入其他资金来源").sibling("android.widget.EditText")
        self.otherassets = self.poco(text="请输入其他资产净值来源").sibling("android.widget.EditText")
        self.otherassetsvalue = self.poco(text="请输入其他资产净值来源").sibling("android.widget.EditText")


        # 选择交易信息
        self.fundsSourcetext = self.poco(text="交易的资金/财富来源(选择所有适用)")
        self.otherfundsSource = self.poco(text="请提供其他财富来源").sibling("android.widget.EditText")
        self.securities_date = self.poco(text="证券").sibling("android.view.ViewGroup").offspring("android.widget.TextView")
        self.CBBC_date = self.poco(text="牛熊证").sibling("android.view.ViewGroup").offspring("android.widget.TextView")
        self.DerivativeWarrant_date = self.poco(text="衍生权证(涡轮)").sibling("android.view.ViewGroup").offspring("android.widget.TextView")
        self.futures_date = self.poco(text="期货").sibling("android.view.ViewGroup").offspring("android.widget.TextView")
        self.Option_date = self.poco(text="期权").sibling("android.view.ViewGroup").offspring("android.widget.TextView")
        self.Optional_date = self.poco(text="其他投资(选填)").sibling("android.widget.EditText")
        self.otherInvestment_date = self.poco(text="其他投资").sibling("android.view.ViewGroup").offspring("android.widget.TextView")

        # 相关保证金融资账户
        self.AccountName = self.poco(textMatches=".*账户持有人姓名").sibling("android.widget.EditText")
        self.AccountNumber = self.poco(textMatches=".*账户号码").sibling("android.widget.EditText")
        self.beneficiaryName = self.poco(textMatches=".*受益人名称").sibling("android.widget.EditText")
        self.ordersName = self.poco(textMatches=".*最终负责下单人姓名").sibling("android.widget.EditText")

        # 其他资料
        self.investmentTarget = self.poco(text="您的投资目标是")

        # 风险披露
        self.player = self.poco("android.widget.SeekBar").sibling("android.view.ViewGroup").child("android.widget.ImageView")
        self.progressbar = self.poco("android.widget.SeekBar")
        self.isUnderstandRisk = self.poco(text="本人已收听风险披露语音，清楚明白并完全接受语音中所声明的全部风险。").sibling("android.view.ViewGroup").child("android.widget.ImageView")

        # 签名
        self.signature = self.poco("android.view.View")
        self.signSubmit = self.poco(text="提").parent()
        self.resign = self.poco(text="重").parent()



    def isElementRadio(self, content, isFlag):
        """
        # 开户表单radio单选框定位方式

        args:
            content: 类型string, 定位栏的标题文本
            isFlag: 类型:Bool

        """
        if isFlag:
            element = self.poco(text=content).sibling("android.view.ViewGroup").child("android.widget.TextView", text="是")
        else:
            element = self.poco(text=content).sibling("android.view.ViewGroup").child("android.widget.TextView", text="否")

        return element

    def isElementCheck(self, content):
        """
        # 开户表单check单个复选框定位方式

        args:
            content: 类型string, 定位栏的标题文本
            isFlag: 类型:Bool

        """
        element = self.poco(text=content).parent().sibling("android.view.ViewGroup").child("android.widget.ImageView")

        return element

    def exists(self, element):
        """
        先等待元素出现, 再判断元素是否显示

        """
        try:
            # return self.poco.wait_for_any(element)
            element.wait_for_appearance(30)
            # element.wait(5)
            # element.exists()
            return element
        except Exception as e:
            print("找不到元素 {}".format(element))
            print(e)


    def disExists_swipe(self, element):
        '''
        元素不在界面上, 滑动界面
        :param element:
        :return:
        '''

        while not element.exists():
            self.log.debug("disExists_swipe进来")
            element.invalidate()
            contentEle = self.poco("android:id/content")
            contentEle.invalidate()
            contentEle.swipe([0, -0.3])

        element.invalidate()
        return element


    def click_select(self, selectelement, selectText):
        """
        # 选择下拉框的值, 判断与当前值是否一致

        args:
            selectelement : 需要操作的元素
            selectText : 需要选择的, 下拉框的值
        """

        selectElement = self.exists(selectelement)

        # 获取就业情况栏位的值
        try:
            employtext = selectElement.get_text()
        except:
            employtext = None

        # 判断下拉选项当前值是否与当前选中的一致
        if selectText != employtext:
            # 点击就业情况下拉框
            selectElement.click()
            # 下拉框选值:employ
            self.poco(text=selectText).click()

            return True
