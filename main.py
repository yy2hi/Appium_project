import time
import pytest
from motion import HomePage
from common import driver_setup  # driver_setup fixture 가져오기

@pytest.fixture
def home_page(driver_setup):
    return HomePage(driver_setup)  # driver_setup을 사용하여 HomePage 인스턴스 생성

def test_click_button(home_page):
    assert_button1_click_switch_touch(home_page)
    home_page.click_button_2()
    home_page.input_text_edit("Input text")
    home_page.click_check_box()
    home_page.click_switch_button()
    time.sleep(5)

def assert_button1_click_switch_touch(home_page):
    home_page.click_button_1()
    time.sleep(1)
    element = home_page.get_element(home_page.button_1_touch)
    assert element is not None
