import datetime
import re
import subprocess
import sys

import allure
import pytest
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

from Commons.GlobalMap import GlobalMap
from Commons.Logging import Logs
from ElementPage.publicTool import publicTool

gm = GlobalMap()
log = Logs()
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("airtest-APP\\") + len("airtest-APP\\")]


@pytest.fixture()
def reloadRoute(request, poco):
    """
    # 退出重新加载页面, 清除页面前端缓存

    """
    log.debug("正在执行{} 方法".format(sys._getframe().f_code.co_name, ))

    routetitle = request.param
    pubTool = publicTool(poco)

    start = time.time()
    while poco(text="取消").exists():
        poco(text="取消").click()
        if time.time() - start > 20:
            break

    start1 = time.time()
    while poco(text="知道了").exists():
        poco(text="知道了").click()
        if time.time() - start1 > 20:
            break

    start2 = time.time()
    while poco(text="便捷开户").exists():
        poco(text="便捷开户").click()
        if time.time() - start2 > 20:
            break

    # 点击退出按钮后, 再次进入开户表单
    pubTool.closeform()
    pubTool.wait_loading()
    title = pubTool.get_Routetitle()
    # 获取标题
    gm.set_value(Routetitle=title)
    log.debug("当前的页面标题为: {}".format(title))

    # 判断当前标题, 如不是操作界面, 则点击返回按钮
    if routetitle != pubTool.get_Routetitle():
        pubTool.backform()


# @pytest.fixture(scope="session", autouse=True)
# def config():
#     gm.set_value(environment="aos-uat")  # 记录数据库
#     gm.set_value(phone = "13148814889")
#     gm.set_bool(isbullion=False)  # 记录黄金账户是否开启
#     gm.set_bool(isLeveraged=False)  # 记录外汇账户是否开启
#     # mongo数据库地址
#     gm.set_value(
#         mongohost="mongodb+srv://eddiddevadmin:atfxdev2018@dev-clientdb-nckz7.mongodb.net")


@pytest.fixture(scope="session", autouse=True)
def poco():
    log.debug("正在执行{} 方法".format(sys._getframe().f_code.co_name, ))
    # poco = AndroidUiautomationPoco(screenshot_each_action=False)

    # if not cli_setup():
    #     auto_setup(__file__, logdir=True,
    #                devices=["Android:///", ])
    if not cli_setup():
        # 模拟器 >> 网易mumu模拟器连接cap_method=JAVACAP&&ori_method=ADBORI
        try:
            subprocess.Popen("adb connect 127.0.0.1:7555", shell=True).wait(2)
            readDeviceId = list(os.popen('adb devices').readlines())
            deviceId = re.findall(r'(.*)\tdevice', readDeviceId[1])
        except:
            readDeviceId = list(os.popen('adb devices').readlines())
            # 获取第一个

        for deviceid in readDeviceId:
            deviceId = re.findall(r'(.*)\tdevice', deviceid)
            if ''.join(deviceId) == "f7b6acb9":
                deviceuuid = "f7b6acb9"
                break

            elif ''.join(deviceId) == "127.0.0.1:7555":
                deviceuuid = "127.0.0.1:7555"
                break

        # connect_device(
        #     "Android://127.0.0.1:5037/127.0.0.1:7555?ori_method=ADBORI")
        log.debug("当前操作的设备为: {}".format(deviceuuid))
        gm.set_value(deviceuuid=deviceuuid)

        connect_device(
            "Android://127.0.0.1:5037/{device}?ori_method=ADBORI".format(device=deviceuuid))

        # connect_device(
        #     "Android://127.0.0.1:5037/127.0.0.1:7555?ori_method=ADBORI".format(device=''.join(deviceuuid)))

    poco = AndroidUiautomationPoco(force_restart=True)
    gm.set_bool(poco=poco)  # 全局poco

    yield poco


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    '''
    捕获测试用例结果
    :param item:
    :param call:
    :return:
    '''
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    if rep.when == 'call':
        if rep.failed:
            print("我已经捕获失败了")
            nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            # 截图
            subprocess.Popen(
                r"adb -s {driver} shell screencap -p /sdcard/Pictures/screen{time}.png".format(
                    driver=device().uuid,time=nowtime),shell=True).wait()

            if os.path.exists(rootPath + "Logs/error_screenIMG") is False:
                os.makedirs(rootPath + "Logs/error_screenIMG")

            # pull
            subprocess.Popen(
                r"adb -s {driver} pull /sdcard/Pictures/screen{time}.png {pngfile}".format(
                    driver=device().uuid, time=nowtime, pngfile=rootPath + "Logs/error_screenIMG"), shell=True).wait()
            # 删除
            subprocess.Popen(r"adb -s {driver} shell rm /sdcard/Pictures/screen{time}.png".format(driver=device().uuid, time=nowtime),shell=True).wait()
            # 刷新文件夹
            subprocess.Popen(
                r"adb -s {driver} shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/Pictures/screen{time}.png".format(
                    driver=device().uuid, time=nowtime)).wait()

            testimg = open(rootPath + "Logs/error_screenIMG/screen{time}.png".format(time=nowtime), 'rb').read()
            # allure.attach(body, name, attachment_type, extension)
            # body - 要写入文件的原始内容。
            # name - 包含文件名的字符串
            # attachment_type - 其中一个allure.attachment_type值
            # extension - 提供的将用作创建文件的扩展名
            allure.attach(testimg, "screen", allure.attachment_type.PNG)


        elif rep.passed:
            pass


# def pytest_collection_modifyitems(config, items):
#     import pdb; pdb.set_trace()
# #
#     print("222222222222222222222222222222")
#     """ 根据指定的mark参数场景，动态选择case的执行顺序"""
#     for item in items:
#         scenarios = [
#             marker for marker in item.own_markers
#             if marker.name.startswith('scenarios')
#             and marker.name in config.option.markexpr
#         ]
#         if len(scenarios) == 1 and not item.get_closest_marker('run'):
#            item.add_marker(pytest.mark.run(order=scenarios[0].args[0]))