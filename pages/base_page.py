import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание когда элемент будет кликабельным')
    def waiting_element(self, element):
        elm = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elm)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(elm))
        return elm

    @allure.step('Кликаем по элементу')
    def click_element(self, element):
        elm = self.waiting_element(element)
        elm.click()

    @allure.step('Принимаем куки')
    def click_cookie(self):
        elm = self.waiting_element(BasePageLocators.COOKIE_BUTTON)
        elm.click()

    @staticmethod
    def make_locator(value):
        result = (By.XPATH, f'.//p[text()="{value}"]')
        return result
