import time

import pytest

from locators.locators import MainPageLocators
from pages.main_page import MainPage
from data.data import MainPageData
from data.data import Error, SearchData


class TestMain:

    def test_catalog_count_title_link(self, driver):
        main = MainPage(driver)
        main.click_catalog_button()
        actual_count_elements_catalog = main.get_count_element_list()
        expected_count_elements_catalog = MainPageData.CATALOG_COUNT_LINK
        assert actual_count_elements_catalog == expected_count_elements_catalog, Error.count_element_wrong

    def test_catalog_link_name(self, driver):
        main = MainPage(driver)
        main.click_catalog_button()
        actual_catalog_link_title_text = main.get_catalog_link_title_name_text()
        expected_catalog_link_title_text = MainPage.get_actual_list_link_text_in_catalog_product()
        assert actual_catalog_link_title_text == expected_catalog_link_title_text, Error.text_elements_wrong

    @pytest.mark.parametrize('number_link, url_redirect_page', [
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Электроника'],
         MainPageData.DICT_CATALOG_LINK_URL['Электроника']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Бытовая техника'],
         MainPageData.DICT_CATALOG_LINK_URL['Бытовая техника']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Одежда'],
         MainPageData.DICT_CATALOG_LINK_URL['Одежда']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Обувь'],
         MainPageData.DICT_CATALOG_LINK_URL['Обувь']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Аксессуары'],
         MainPageData.DICT_CATALOG_LINK_URL['Аксессуары']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Красота'],
         MainPageData.DICT_CATALOG_LINK_URL['Красота']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Здоровье'],
         MainPageData.DICT_CATALOG_LINK_URL['Здоровье']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Красота'],
         MainPageData.DICT_CATALOG_LINK_URL['Красота']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Товары для дома'],
         MainPageData.DICT_CATALOG_LINK_URL['Товары для дома']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Строительство и ремонт'],
         MainPageData.DICT_CATALOG_LINK_URL['Строительство и ремонт']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Детские товары'],
         MainPageData.DICT_CATALOG_LINK_URL['Детские товары']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Хобби и творчество'],
         MainPageData.DICT_CATALOG_LINK_URL['Хобби и творчество']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Товары для взрослых'],
         MainPageData.DICT_CATALOG_LINK_URL['Товары для взрослых']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Спорт и отдых'],
         MainPageData.DICT_CATALOG_LINK_URL['Спорт и отдых']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Продукты питания'],
         MainPageData.DICT_CATALOG_LINK_URL['Продукты питания']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Бытовая химия и личная гигиена'],
         MainPageData.DICT_CATALOG_LINK_URL['Бытовая химия и личная гигиена']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Канцтовары'],
         MainPageData.DICT_CATALOG_LINK_URL['Канцтовары']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Зоотовары'],
         MainPageData.DICT_CATALOG_LINK_URL['Зоотовары']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Книги'],
         MainPageData.DICT_CATALOG_LINK_URL['Книги']),
        (MainPageData.DICT_CATALOG_LINK_POSITION_NUMBER['Дача, сад и огород'],
         MainPageData.DICT_CATALOG_LINK_URL['Дача, сад и огород']),
    ])
    def test_catalog_link_redirect(self, driver, number_link, url_redirect_page):
        main = MainPage(driver)
        main.click_catalog_link(number_link)
        main.wait_load_title()
        actual_url_page = main.get_url()
        expected_url_page = url_redirect_page
        assert actual_url_page == expected_url_page, f"Ожидалось {expected_url_page}, пришло {actual_url_page}"

    def test_check_visible_swiper_container(self, driver):
        main = MainPage(driver)
        actual_result_visible_swiper = main.check_swiper()
        assert actual_result_visible_swiper is True, Error.element_not_visible

    def test_check_search(self, driver):
        main = MainPage(driver)
        main.input_search(SearchData.MANUFACTURERS_NAME[0])
        elements_list_product = main.get_list_product()
        elements_list_product[0].click()
        actual_title_product_text = main.get_product_text()
        result = SearchData.MANUFACTURERS_NAME[0].lower() in actual_title_product_text.lower()
        assert result is True
