#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Commons.GlobalMap import GlobalMap


class BaseView():

    gm = GlobalMap()

    def __init__(self, poco):
        self.poco = poco

        # 公用
        self.nextStepbtn = self.poco(text="下一步")
        self.boxCancel = self.poco(text="取消")
        self.boxconfirm = self.poco(text="确定")
        self.Album = self.poco(text="相册选取")
        self.loading = self.poco("android.widget.ProgressBar")

        self.el_firstSetting_loc = self.poco("io.newtype.eddid.app:id/btn_start")
        self.baropen = self.poco(text="开户")
        self.easyOpenning = self.poco(text="便捷开户")
        self.goLogin = self.poco(text="去登录")
        self.phonenumber = self.poco(text="请输入手机号")

        self.el_chinese = self.poco(text="我是内地居民")
        self.el_idcardNegative = self.poco(text="请上传身份证人像面")

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
        self.totalAnnualCustomerRevenueHK = self.poco(text="全年总收入(港元)").sibling("android.view.ViewGroup").offspring("android.widget.TextView")
        self.customerNetAssetValueHK = self.poco(text="资产净值(港元)").sibling("android.view.ViewGroup").offspring("android.widget.TextView")
        self.sourcesfunds = self.poco(text="请注明资金来源(可多选)")
        self.assetsvalue = self.poco(text="请注明资产净值(可多选)")
        # self.salary = self.poco(text="就业")
        # self.saving = self.poco(text="储蓄")
        # self.investmentreturn = self.poco(text="投资回报")
        # self.rent = self.poco(text="租金")
        # self.commission = self.poco(text="佣金")
        # self.other = self.poco(text="其他")
        # self.Property = self.poco(text="物业投资")
        # self.vehicle = self.poco(text="车辆投资")
        # self.Stockorbond = self.poco(text="股票/债券投资")
        # self.heritage = self.poco(text="遗产")
        # self.selfOperatedBusinessIncome = self.poco(test="自营业务收益")
        # self.pension = self.poco(test="退休金")

        # 选择交易信息
        self.fundsSourcetext = self.poco(text="交易的资金/财富来源(选择所有适用)")

        # 介绍与推广
        self.channel = self.poco(text="您透过哪些渠道认识艾德证券期货及/或艾德金业?(选择所有适用)")

        # 其他资料
        self.investmentTarget = self.poco(text="您的投资目标是")

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
            element.wait_for_appearance()
            return element
        except Exception as e:
            print("找不到元素 {}".format(element))
            print(e)


