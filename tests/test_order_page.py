import allure
from data import *
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title('Проверка создания заказа')
    @allure.description('Проверка заполенение полей и создание заказа')
    def test_add_order(self, driver):
        order = OrderPage(driver)
        order.click_cookie()
        order.make_order(NAME, LAST_NAME, ADDRESS, PHONE_NUMBER, COMMENT)
        order.check_text(TEXT)
