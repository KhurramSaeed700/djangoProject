# this file will include a class with instance methrods
# that will interact with website and filter the results

class BookingFiltration:
    def __init__(self,driver):
        self.driver=driver

    def apply_star_rating(self):
        self.driver.find_element_by_id('filter_class')