import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage


class HomePage(BasePage):
    @allure.step('Проверка перехода на сайт')
    def going_on_link(self, title, domain):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(ec.title_is(title))
        assert domain in self.driver.current_url
