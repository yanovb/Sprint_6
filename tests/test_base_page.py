import allure
from data import QUESTIONS_ABOUT_IMPORTANT_TEXT
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class TestBasePage:
    @allure.title('Проверка возврата на начальную страницу')
    @allure.description('Проверка возврата на начальную страницу после нажатия на логотип Самоката')
    def test_return_to_home_page(self, driver):
        base_page = BasePage(driver)
        base_page.click_element(BasePageLocators.BOTTOM_ORDER_BUTTON)
        base_page.click_element(BasePageLocators.SCOOTER_LOGO)
        base_page.check_text(BasePageLocators.SECTION_ABOUT_QUESTIONS, QUESTIONS_ABOUT_IMPORTANT_TEXT)
