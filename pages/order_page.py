import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Добавляем значение в поле')
    def add_value(self, element, value):
        elm = self.driver.find_element(*element)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(elm))
        elm.send_keys(value)
