#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import shutil
import traceback

import allure
from airtest.core.api import *

from Commons.Logging import Logs

log = Logs()

def retry(times=3,wait_time=10):
    '''
    失败重试装饰器
    :param times: 重试次数
    :param wait_time: 重试等待时间
    :return:
    '''
    def warp_func(func):
        def fild_retry(self, *args, **kwargs):
            for t in range(times):
                try:
                    func(self, *args, **kwargs)
                    return
                except:
                    # 截图
                    time.sleep(wait_time)
        return fild_retry
    return warp_func


def rmdir5(self):

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
