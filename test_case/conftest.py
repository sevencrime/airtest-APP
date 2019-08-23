
import pytest
import os
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

@pytest.fixture(scope="session", autouse=True)
def poco():
    os.popen("adb connect 127.0.0.1:7555")
    # poco = AndroidUiautomationPoco(screenshot_each_action=False)
    poco = AndroidUiautomationPoco()
    return poco

