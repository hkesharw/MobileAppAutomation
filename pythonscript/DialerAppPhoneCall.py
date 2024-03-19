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
el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Phone')
el.click()
time.sleep(10)

# click on the dialer

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="key pad"]').click()
time.sleep(3)

# click on the number

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="1,"]').click()
time.sleep(1)
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="2,ABC"]').click()
time.sleep(1)
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="3,DEF"]').click()
time.sleep(1)
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="4,GHI"]').click()
time.sleep(1)
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="5,JKL"]').click()
time.sleep(1)
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="6,MNO"]').click()
time.sleep(1)
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="7,PQRS"]').click()
time.sleep(1)
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="8,TUV"]').click()
time.sleep(1)
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="9,WXYZ"]').click()
time.sleep(1)
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="0"]').click()
time.sleep(1)

# click on call

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="dial").click()
time.sleep(10)

# number which was called
wait = WebDriverWait(driver, timeout=30)

number = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.android.dialer:id/contactgrid_contact_name"))).text


print(number)

# end call

#wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "End call")))
driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='End call').click()

print("Execution done")
driver.quit()
