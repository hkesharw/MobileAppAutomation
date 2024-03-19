import time

from appium import webdriver
from appium.webdriver.common.appiumby import By, AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


def sign_in_android(username, password, driver, locator_sheet_android):

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, (locator_sheet_android[0, 'accessibility_id'])).click()

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, (locator_sheet_android[0, 'accessibility_id'])).send_keys(username)

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, (locator_sheet_android[0, 'accessibility_id'])).send_keys(password)

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, (locator_sheet_android[0, 'accessibility_id'])).click()

    time.sleep(30)

    print("Login Successful")


def sign_in_ios(username, password, driver, locator_sheet_ios):

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, (locator_sheet_ios[0, 'accessibility_id'])).click()

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, (locator_sheet_ios[0, 'accessibility_id'])).send_keys(username)

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, (locator_sheet_ios[0, 'accessibility_id'])).send_keys(password)

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, (locator_sheet_ios[0, 'accessibility_id'])).click()

    time.sleep(30)

    print("Login Successful")
