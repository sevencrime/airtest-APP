#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import glob
import shutil
import traceback

import allure
from airtest.core.api import *

from Commons.GlobalMap import GlobalMap
from Commons.Logging import Logs

gm = GlobalMap()
log = Logs()

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("airtest-APP\\") + len("airtest-APP\\")]

# def retry(poco, times=3,wait_time=10):
#     '''
#     失败重试装饰器
#     :param times: 重试次数
#     :param wait_time: 重试等待时间
#     :return:
#     '''
#     def warp_func(func):
#         def fild_retry(self, *args, **kwargs):
#             for t in range(times):
#                 try:
#                     func(self, poco, *args, **kwargs)
#                     return
#                 except:
#                     # 截图
#                     time.sleep(wait_time)
#         return fild_retry
#     return warp_func


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



def retry(times=3,wait_time=3):
    '''
    失败重试装饰器
    :param times: 重试次数
    :param wait_time: 重试等待时间
    :return:
    '''
    import pdb; pdb.set_trace()
    def wrapper(func):
        import pdb; pdb.set_trace()
        def inner_wrapper(self, *args, **kwargs):
            log.debug("正在执行用例 : {}".format(func.__name__, ) )
            poco = gm.get_value("poco")
            import pdb; pdb.set_trace()
            for t in range(times):
                try:
                    return func(self, poco, *args, **kwargs)
                except Exception as e:
                    raise e
                    log.error(e)
                    nowtime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                    # 截图
                    os.popen(r"adb shell screencap -p /sdcard/screen{}.png".format(nowtime))
                    # pull
                    if os.path.exists(rootPath+"Logs/error_screenIMG") is False:
                        os.makedirs(rootPath+"Logs/error_screenIMG")
                    os.popen(r"adb pull /sdcard/screen{time}.png {pngfile}".format(time=nowtime, pngfile = rootPath+"Logs/error_screenIMG"))
                    # 删除原图片
                    os.popen(r"adb shell rm /sdcard/screen{}.png".format(nowtime))
                    # 等待重复
                    time.sleep(wait_time)

        return inner_wrapper
    return wrapper

