import pytest
from selenium import webdriver


URL = 'https://qa-scooter.praktikum-services.ru/'


@pytest.fixture(scope='function')
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox()
    driver.get(URL)
    yield driver
    driver.quit()
