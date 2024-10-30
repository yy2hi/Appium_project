import os
import unittest

from appium import webdriver
from appium.options.android import UiAutomator2Options

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class BaseTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}

        url = "http://127.0.0.1:4723/wd/hub"
        desired_caps["platformName"] = "Android"
        desired_caps["appium:avd"] = "Medium_Phone_API_35"
        desired_caps["automationName"] = "uiautomator2"
        desired_caps["appium:app"] = os.path.join(BASE_DIR, "sample_app", "app-release.apk")

        self.driver = webdriver.Remote(
             url, options=UiAutomator2Options().load_capabilities(desired_caps)
        )

def tearDown(self):
     if self.driver:
        self.driver.quit()