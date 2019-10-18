#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView
import datetime

class personalInformationPage(BaseView):
    """
    请填写个人资料

    """

    def modify_title(self, ismodify):
        self.disExists_swipe(self.el_title)
        try:
            assert self.el_title.get_text() == '小姐'
        except Exception as e:
            self.log.error("称呼OCR识别有误, 错误的称谓为: {}".format(self.el_title.get_text()))

        if ismodify:
            # 判断是否修改
            # 下拉框
            self.click_select(self.el_title, "先生")
            self.el_title.invalidate()
            title = self.el_title.get_text()

        return title


    def modify_chinesename(self, ismodify):
        self.disExists_swipe(self.el_chinesename)
        try:
            assert self.el_chinesename.get_text() == '宜小信'
        except Exception as e:
            self.log.error("中文姓名OCR识别有误, 错误的中文姓名为: {}".format(self.el_chinesename.get_text()))

        if ismodify:
            # 判断是否修改
            self.el_chinesename.set_text("修改中文姓名")
            self.el_chinesename.invalidate()
            chineseanme = self.el_chinesename.get_text()

        return chineseanme

    def modify_lastname(self, ismodify):
        self.disExists_swipe(self.el_lastname)
        try:
            assert self.el_lastname.get_text() == 'Yi'
        except Exception as e:
            self.log.error("姓氏OCR识别有误, 错误的姓为: {}".format(self.el_lastname.get_text()))

        if ismodify:
            # 判断是否修改
            self.el_lastname.set_text("Zheng")
            self.el_lastname.invalidate()
            title = self.el_lastname.get_text()

        return title

    def modify_firstname(self, ismodify):
        self.disExists_swipe(self.el_firstname)
        try:
            assert self.el_firstname.get_text() == 'Xiaoxin'
        except Exception as e:
            self.log.error("名字OCR识别有误, 错误的名为: {}".format(self.el_firstname.get_text()))

        if ismodify:
            # 判断是否修改
            self.el_firstname.set_text("Onedi")
            self.el_firstname.invalidate()
            firstname = self.el_firstname.get_text()

        return firstname

    def modify_idNumber(self, ismodify):
        self.disExists_swipe(self.el_idNumber)
        try:
            assert self.el_idNumber.get_text() == '132261198811160681'
        except Exception as e:
            self.log.error("身份证OCR识别有误, 错误的身份证为: {}".format(self.el_idNumber.get_text()))

        if ismodify:
            # 判断是否修改
            self.el_idNumber.set_text("441502199602120225")
            self.el_idNumber.invalidate()
            idNumber = self.el_idNumber.get_text()

        return idNumber

    def modify_birthday(self, ismodify, datestr=None):
        '''
        修改 / 获取 出生日期
        :param ismodify: 判断是否修改
        :param datestr:  年/月 , og:2002.02.07
        :return:
        '''

        self.disExists_swipe(self.el_birthday)
        try:
            assert self.el_birthday.get_text() == '1988.11.16'
        except Exception as e:
            self.log.error("出生日期OCR识别有误, 错误的出生日期为: {}".format(self.el_birthday.get_text()))

        if ismodify:
            self.datePickerView(self.el_birthday, datestr=datestr)

        self.el_birthday.invalidate()
        return self.el_birthday.get_text()


    def modify_country(self, ismodify):
        self.disExists_swipe(self.el_country)
        try:
            assert self.el_country.get_text() == '中华人民共和国'
        except Exception as e:
            self.log.error("国籍OCR识别有误, 错误的国籍为: {}".format(self.el_country.get_text()))

        if ismodify:
            # 判断是否修改
            self.el_country.set_text("中国")
            self.el_country.invalidate()
            country = self.el_country.get_text()

        return country

    def modify_countryIssue(self, ismodify):
        self.disExists_swipe(self.el_countryIssue)
        try:
            assert self.el_countryIssue.get_text() == '东台市公安局'
        except Exception as e:
            self.log.error("签发机关OCR识别有误, 错误的签发机关为: {}".format(self.el_countryIssue.get_text()))

        if ismodify:
            # 判断是否修改
            self.el_countryIssue.set_text("汕尾市公安局")
            self.el_countryIssue.invalidate()
            country = self.el_countryIssue.get_text()

        return country

    def modify_validityPeriod(self, ismodify, datestr=None):
        self.disExists_swipe(self.el_validityPeriod)
        try:
            assert self.el_validityPeriod.get_text() == '2023.04.17'
        except Exception as e:
            self.log.error("有效期OCR识别有误, 错误的有效期为: {}".format(self.el_validityPeriod.get_text()))

        if ismodify:
            # 判断是否修改
            self.datePickerView(self.el_validityPeriod, datestr=datestr)

        return self.el_validityPeriod.get_text()


    def modify_phone(self, ismodify, phone):
        self.disExists_swipe(self.el_phone)
        try:
            assert self.el_phone.get_text() == '15089514626'
        except Exception as e:
            self.log.error("电话号码识别有误, 错误的中文姓名为: {}".format(self.el_phone.get_text()))

        if ismodify:
            # 判断是否修改
            self.el_phone.set_text(phone)
            self.el_phone.invalidate()
            phone = self.el_phone.get_text()

        return phone



    def send_emali(self, email="15089514626@sina.cn"):
        """
        输入邮箱

        """
        # import pdb; pdb.set_trace()
        self.disExists_swipe(self.el_email).set_text(email)

    def send_reemail(self, email="15089514626@sina.cn"):
        """
        再次输入电邮

        """
        self.disExists_swipe(self.el_reEmail).set_text(email)


    def get_address(self):
        """
        获取地址栏的值

        """
        return self.disExists_swipe(self.el_iDcardAddress).get_text()


    def click_isAddress(self, isFlag):
        '''
        勾选地址证明
        '''

        # 判断是否勾选, sameAddress

        if not self.gm.get_value("sameAdderss") and isFlag:
            self.disExists_swipe(self.el_isAddress).click()
            self.gm.set_bool(sameAdderss=True)

        elif self.gm.get_value("sameAdderss") and not isFlag:
            self.disExists_swipe(self.el_isAddress).click()
            self.gm.set_bool(sameAdderss=False)




