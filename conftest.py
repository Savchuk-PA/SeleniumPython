import pytest
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def get_chrome_options():
    ua = UserAgent()
    options = Options()
    options.add_argument(f'user-agent={ua.chrome}')
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_argument('log-level=3')
    return options


@pytest.fixture(scope="function")
def driver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path="driver\\chromedriver.exe", options=options)
    driver.delete_all_cookies()
    yield driver
    driver.quit()
