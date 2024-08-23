import allure
import pytest
from data import *
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage


class TestHomePage:
    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка ответов после клика на вопросы в разделе "Вопросы о важном"')
    @pytest.mark.parametrize('question, answer', HomePageLocators.QUESTIONS_AND_ANSWERS)
    def test_questions(self, driver, question, answer):
        home_page = HomePage(driver)
        home_page.click_element(HomePageLocators.COOKIE_BUTTON)
        home_page.click_element(question)
        home_page.check_text(home_page.make_locator(answer), answer)

    @allure.title('Проверка перехода на сайт яндекса')
    @allure.description('Проверка перехода на https://dzen.ru/ после клика на логотип Яндекса')
    def test_click_on_yandex_logo(self, driver):
        home_page = HomePage(driver)
        home_page.click_element(HomePageLocators.COOKIE_BUTTON)
        home_page.click_element(HomePageLocators.YANDEX_LOGO)
        home_page.going_on_link(TITLE, DOMAIN_NAME)
