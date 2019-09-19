#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Commons.BaseView import BaseView


class bankCardInformationPage(BaseView):
    """
    银行卡

    """
    def send_bankCardNo(self, bankNo="12345678"):
        """
        输入银行卡号

        """
        bankCardNo = self.exists(self.el_bankCardNo)
        bankCardNo.set_text(bankNo)
        return bankCardNo

    def send_bankName(self, text="中国建设银行"):
        """
        输入银行卡号

        """
        bankname = self.exists(self.el_bankName)
        bankname.set_text(text)
        return bankname

    def send_bankPhone(self, bankphone="15089514626"):
        """
        输入银行卡号

        """
        bankPhone = self.exists(self.el_bankPhone)
        bankPhone.set_text(bankphone)
        return bankPhone

