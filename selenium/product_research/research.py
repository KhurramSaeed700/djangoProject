from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import const_pr as const
import os
from selenium import webdriver


class Research(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", close_browser=False):
        self.driver_path = driver_path
        self.teardown = close_browser
        os.environ['PATH'] += self.driver_path
        super(Research, self).__init__()
        self.implicitly_wait(15)
        # self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def open_alibaba(self):
        self.get(const.google_url)
        # self.find_element_by_css_selector('body').send_keys(Keys.CONTROL + "t")

    def search(self, search_item):
        search_element=self.find_element_by_css_selector(
            'input[jsaction="paste:puy29d;"]'
        )
        search_element.send_keys(search_item + Keys.ENTER)
        self.find_element(By.CSS_SELECTOR("body")).send_keys(Keys.LEFT_CONTROL + 't')