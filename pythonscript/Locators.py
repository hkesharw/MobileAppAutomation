import time

import urllib3
from selenium.webdriver.common.keys import Keys
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

urllib3.disable_warnings()

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
}

url = "http://localhost:4724"

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Chrome')
el.click()
time.sleep(3)
driver.find_element(by=AppiumBy.ID, value='com.android.chrome:id/search_box_text').send_keys('saurabhtyping')
time.sleep(1)
driver.press_keycode(66)
time.sleep(3)
print("Execution done")
driver.quit()
