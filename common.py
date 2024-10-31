import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture(scope="session")
def driver_setup():
    desired_caps = {}
    url = "http://127.0.0.1:4723/wd/hub"
    desired_caps["platformName"] = "Android"
    desired_caps["appium:avd"] = "Medium_Phone_API_35"
    desired_caps["automationName"] = "uiautomator2"
    desired_caps["appium:app"] = os.path.join(BASE_DIR, "sample_app", "app-release.apk")

    driver = webdriver.Remote(url, options=UiAutomator2Options().load_capabilities(desired_caps))
    yield driver  # driver 객체 반환 및 테스트 코드 실행
    driver.quit() # 테스트 코드 실행 완료 후 실행
