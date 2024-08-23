import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем по элементу')
    def click_element(self, element):
        elm = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elm)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(elm))
        elm.click()

    @allure.step('Проверяем ожидаемый текст элемента')
    def check_text(self, element, expected_result):
        assert self.driver.find_element(*element).text == expected_result

    @staticmethod
    def make_locator(value):
        result = (By.XPATH, f'.//p[text()="{value}"]')
        return result
