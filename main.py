import time

from motion import HomePage
from base_test import BaseTest

class Test_main(BaseTest):
    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)

    def test_click_button(self):
        self.assert_button1_click_switch_touch()
        self.home_page.click_button_2()
        self.home_page.input_text_edit("Input text")
        self.home_page.click_check_box()
        self.home_page.click_switch_button()
        time.sleep(5)

    def assert_button1_click_switch_touch(self):
        self.home_page.click_button_1()
        time.sleep(1)
        self.home_page.get_element(self.home_page.button_1_touch)

        