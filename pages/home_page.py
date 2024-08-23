import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    @allure.step('Проверка перехода на сайт')
    def going_on_link(self, title, domain):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(ec.title_is(title))
        assert domain in self.driver.current_url

    @allure.step('Кликаем по логотипу Яндекса')
    def click_yandex_logo(self):
        self.click_element(HomePageLocators.YANDEX_LOGO)

    @allure.step('Кликаем по логотипу Самоката')
    def click_scooter_logo(self):
        self.click_element(HomePageLocators.SCOOTER_LOGO)

    @allure.step('Кликаем по кнопке создания заказа')
    def click_order_button(self):
        self.click_element(HomePageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step('Проверяем ожидаемый текст элемента')
    def check_answer_text(self, locator, expected_result):
        elm = self.waiting_element(locator)
        assert elm.text == expected_result

    @allure.step('Проверяем текст на главной странице')
    def check_text(self, text):
        elm = self.waiting_element(HomePageLocators.SECTION_ABOUT_QUESTIONS)
        assert  elm.text == text
