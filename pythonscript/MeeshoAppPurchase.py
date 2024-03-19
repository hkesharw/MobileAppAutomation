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

urllib3.disable_warnings()

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
}

url = "http://localhost:4724"

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
#App launch
el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Meesho')
el.click()
time.sleep(10)
#driver.find_element(by=AppiumBy.ID, value='com.meesho.supply:id/tvMale').click()
#time.sleep(3)
#driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='ENGLISH').click()
#time.sleep(3)
#driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='com.meesho.supply:id/iv_icon').click()
#time.sleep(2)

#Serach Text Box
driver.find_element(by=AppiumBy.ID, value='com.meesho.supply:id/query_edit_text').click()
time.sleep(1)
driver.find_element(by=AppiumBy.ID, value='com.meesho.supply:id/query_edit_text').click()
time.sleep(1)


#Entering value in serach box

driver.find_element(by=AppiumBy.ID, value='com.meesho.supply:id/query_edit_text').send_keys('water bottle')
time.sleep(5)

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(998, 1948)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

time.sleep(5)

#Product page

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(129, 1225)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()


time.sleep(5)

#buy button
driver.find_element(by=AppiumBy.ID, value='com.meesho.supply:id/primary_cta').click()
time.sleep(5)
#buy button
driver.find_element(by=AppiumBy.ID, value='com.meesho.supply:id/secondary_cta').click()
time.sleep(5)
#login page
driver.find_element(by=AppiumBy.ID, value='com.meesho.supply:id/phone_edit_text').send_keys('8517057519')
time.sleep(5)
#otp page
driver.find_element(by=AppiumBy.ID, value='com.meesho.supply:id/next_button').click()
time.sleep(10)

k1 = input("Enter the first digit otp : ")
time.sleep(1)
driver.find_element(by=AppiumBy.ID, value='com.meesho.supply:id/first_otp_digit').send_keys(k1)

k2 = input("Enter the second digit otp : ")
time.sleep(1)
driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.ViewAnimator/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[2]').send_keys(k2)


k3 = input("Enter the third digit otp : ")
time.sleep(1)
driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.ViewAnimator/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[3]').send_keys(k3)


k4 = input("Enter the fourth digit otp : ")
time.sleep(1)
driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.ViewAnimator/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[4]').send_keys(k4)


k5 = input("Enter the fifth digit otp : ")
time.sleep(1)
driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.ViewAnimator/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[5]').send_keys(k5)

k6 = input("Enter the sixth digit otp : ")
time.sleep(1)
driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.ViewAnimator/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[6]').send_keys(k6)

time.sleep(3)

#click on verify button

driver.find_element(by=AppiumBy.ID, value='com.meesho.supply:id/otp_continue_button').click()
time.sleep(5)

#continue button on cart

driver.find_element(by=AppiumBy.ID, value='com.meesho.supply:id/multi_cta_info_primary_cta').click()
time.sleep(5)

#cash on delivery option select


actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(456, 576)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(0.1)
actions.w3c_actions.pointer_action.release()
actions.perform()

time.sleep(5)

#place order button lcick

driver.find_element(by=AppiumBy.ID, value='com.meesho.supply:id/multi_cta_info_primary_cta').click()
time.sleep(30)

#review close button

#driver.find_element(by=AppiumBy.ID, value='com.meesho.supply:id/iv_icon').click()
#time.sleep(5)

#thanku shopping text

confirm = driver.find_element(by=AppiumBy.ID, value='com.meesho.supply:id/title').text
print(confirm)
time.sleep(10)

print("Execution done")
driver.quit()
