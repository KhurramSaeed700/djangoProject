import constant as const
import os
from selenium import webdriver

from selenium.booking_filtration import BookingFiltration


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", close_browser=False):
        self.driver_path = driver_path
        self.teardown = close_browser
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param="changed_currency=1;selected_currency={currency}"]'
            # 'data-modal-header-async-url-param="changed_currency=1;selected_currency=PKR"'
        )
        selected_currency_element.click()

    def destination(self, place_to_go):
        destination_element = self.find_element_by_id('ss')
        destination_element.clear()
        destination_element.send_keys(place_to_go)

        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
            # 'data-date="2021-09-08"'
        )
        check_in_element.click()
        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
            # 'data-date="2021-09-08"'
        )
        check_out_element.click()

    def select_adults(self, count=1):
        adult_element = self.find_element_by_id('xp__guests__toggle')
        adult_element.click()

        while True:
            decrease_adult_element = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adult_element.click()

            adult_value_element = self.find_element_by_id('group_adults')  # value of adults reaches 1 then exit loop
            adult_value = adult_value_element.get_attribute('value')  # this will give back value of adults

            if int(adult_value) == 1:
                break

        increase_button_element = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )
        for i in range(count - 1):
            increase_button_element.click()

    def click_search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()

    def apply_filtration(self):
        filter = BookingFiltration(driver=self)
