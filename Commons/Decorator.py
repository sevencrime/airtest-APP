#!/usr/bin/env python
# -*- coding: utf-8 -*-
import traceback

import allure
from airtest.core.api import *

from Commons.Logging import Logs

log = Logs()

def retry(func):
    '''
    失败重试装饰器
    :return:
    '''

    log.debug("调用 <retry> 的是: {}".format(traceback.extract_stack()[-2][2]))
    def wrapper(self, *args, **kwargs):
        for i in range(3):
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                # raise e
                # 失败截图
                Screenshotpath = snapshot()
                import pdb; pdb.set_trace()
                file = open(Screenshotpath, 'rb').read()
                allure.attach('test_img', file, allure.attach_type.PNG)

    return wrapper

