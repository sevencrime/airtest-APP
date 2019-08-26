#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseView():

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

        self.el_chinesename = self.poco(text="中文姓名").sibling("android.widget.EditText")
        self.el_lastname = self.poco(text="姓氏").sibling("android.widget.EditText")
        self.el_firstname = self.poco(text="名字").sibling("android.widget.EditText")
        self.el_email = self.poco(text="电邮").sibling("android.widget.EditText")
        self.el_reEmail = self.poco(text="再次输入电邮").sibling("android.widget.EditText")
        self.el_phone = self.poco(text="电话号码(用于通讯)").sibling("android.widget.EditText")
        self.el_idNumber = self.poco(text="证件号码").sibling("android.widget.EditText")
        self.el_iDcardAddress = self.poco(text="身份证地址(*请确认地址无误，如有误请手动修改)").sibling("android.widget.EditText")
        self.el_FalseiDcardAddress = self.poco(text="如住址和身份证地址不一致(请勾选)").sibling("android.widget.ImageView")



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


