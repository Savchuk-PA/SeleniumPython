import time
from typing import List

from selenium.webdriver import Keys
from selenium.webdriver.remote.webelement import WebElement
from data.data import MainPageData
from locators.locators import MainPageLocators, MainBarLocators, ProductListLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    __locators = MainPageLocators
    __locators_main_bar = MainBarLocators
    __locators_list_product = ProductListLocators

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get("https://kazanexpress.ru/")

    def click_catalog_button(self):
        self.element_is_visible(self.__locators.CATALOG_LIST_BUTTON).click()

    def get_elements_in_catalog(self) -> List[WebElement]:
        return self.elements_are_visible(self.__locators.CATALOG_LIST_LINK)

    def get_count_element_list(self):
        return len(self.elements_are_visible(self.__locators.CATALOG_LIST_LINK))

    def get_catalog_link_title_name_text(self):
        elements = self.get_elements_in_catalog()
        return [element.text for element in elements]

    @staticmethod
    def get_actual_list_link_text_in_catalog_product():
        return list(MainPageData.DICT_CATALOG_LINK_URL.keys())

    def click_catalog_link(self, link_number):
        self.click_catalog_button()
        elements = self.get_elements_in_catalog()
        elements[link_number].click()

    def wait_load_title(self):
        self.element_is_visible(self.__locators.TITLE_H1)

    def check_swiper(self):
        return self.element_is_visible(self.__locators.SWIPER_CONTAINER).is_displayed()

    def check_position(self):
        return self.element_is_visible(self.__locators.SWIPER_CONTAINER).rect

    def input_search(self, search_name: str):
        self.element_is_visible(self.__locators_main_bar.SEARCH_INPUT).send_keys(search_name)
        self.element_is_visible(self.__locators_main_bar.SEARCH_INPUT).send_keys(Keys.ENTER)

    def get_list_product(self):
        return self.elements_are_visible(self.__locators_list_product.LIST_PRODUCT)

    def get_product_text(self):
        return self.element_is_visible(self.__locators_list_product.TITLE_PRODUCT).text
