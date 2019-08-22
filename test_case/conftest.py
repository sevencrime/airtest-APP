
import pytest

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

@pytest.fixture(scope="session", autouse=True)
def poco():
    poco = AndroidUiautomationPoco(screenshot_each_action=False)
    return poco

