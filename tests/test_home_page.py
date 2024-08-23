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
        home_page.click_cookie()
        home_page.click_element(question)
        home_page.check_answer_text(HomePage.make_locator(answer), answer)

    @allure.title('Проверка перехода на сайт яндекса')
    @allure.description('Проверка перехода на https://dzen.ru/ после клика на логотип Яндекса')
    def test_click_on_yandex_logo(self, driver):
        home_page = HomePage(driver)
        home_page.click_cookie()
        home_page.click_yandex_logo()
        home_page.going_on_link(TITLE, DOMAIN_NAME)

    @allure.title('Проверка возврата на начальную страницу')
    @allure.description('Проверка возврата на начальную страницу после нажатия на логотип Самоката')
    def test_return_to_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.click_cookie()
        home_page.click_order_button()
        home_page.click_scooter_logo()
        home_page.check_text(QUESTIONS_ABOUT_IMPORTANT_TEXT)
