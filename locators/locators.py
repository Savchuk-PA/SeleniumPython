from selenium.webdriver.common.by import By


class MainPageLocators:
    CATALOG_LIST_BUTTON = (By.CSS_SELECTOR, "button[data-test-id='button__catalog']")
    CATALOG_LIST_LINK = (By.XPATH, "//li[@class='parent-category-item']")
    CATALOG_LIST_LINK_FOR_URL = (By.CSS_SELECTOR, ".parent-categories .parent-category-link")
    LOGO = (By.CSS_SELECTOR, "svg[class='hidden-mbs visible-mbm logo']")
    TITLE_H1 = (By.XPATH, "//h1[@data-test-id='text__title']")
    SWIPER_CONTAINER = (By.CSS_SELECTOR, ".swiper-container .swiper-container")


class MainBarLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[data-test-id = 'input__search']")


class ProductListLocators:
    LIST_PRODUCT = (By.CSS_SELECTOR, ".ui-card .product-card-image")
    TITLE_PRODUCT = (By.CSS_SELECTOR, "h1[data-test-id = 'text__product-name']")



