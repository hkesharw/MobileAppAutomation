import time

import urllib3
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.keys import Keys
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

urllib3.disable_warnings()

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
}

url = "http://localhost:4724"

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
# App launch
el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Messages')
el.click()
time.sleep(10)

wait = WebDriverWait(driver, timeout=30)
# click on the dialer
#driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Start chat")').click()
wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Start chat")'))).click()

time.sleep(3)

print("Execution done")
driver.quit()
