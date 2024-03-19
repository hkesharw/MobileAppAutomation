import time

import urllib3
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

urllib3.disable_warnings()

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'language': 'en',
    'locale': 'US'
}

url = "http://localhost:4724"

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
time.sleep(10)
el.click()

driver.quit()
