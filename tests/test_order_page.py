import allure
from data import *
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title('Проверка создания заказа')
    @allure.description('Проверка заполенение полей и создание заказа')
    def test_add_order(self, driver):
        order = OrderPage(driver)
        order.click_element(OrderPageLocators.COOKIE_BUTTON)
        order.click_element(OrderPageLocators.TOP_ORDER_BUTTON)
        order.add_value(OrderPageLocators.NAME_FIELD, NAME)
        order.add_value(OrderPageLocators.LAST_NAME_FIELD, LAST_NAME)
        order.add_value(OrderPageLocators.ADDRESS_FIELD, ADDRESS)
        order.click_element(OrderPageLocators.METRO_FIELD)
        order.click_element(OrderPageLocators.SOKOL_METRO_STATION)
        order.add_value(OrderPageLocators.PHONE_NUMBER_FIELD, PHONE_NUMBER)
        order.click_element(OrderPageLocators.NEXT_BUTTON)
        order.click_element(OrderPageLocators.SCOOTER_DATE_FIELD)
        order.click_element(OrderPageLocators.DATE_IN_CALENDAR)
        order.click_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        order.click_element(OrderPageLocators.SELECTED_RENTAL_PERIOD)
        order.click_element(OrderPageLocators.SELECTED_SCOOTER_COLOR)
        order.add_value(OrderPageLocators.COMMENT_FIELD, COMMENT)
        order.click_element(OrderPageLocators.ADD_ORDER_FIELD)
        order.click_element(OrderPageLocators.ORDER_CONFIRMATION_BUTTON)
        order.check_text(OrderPageLocators.VIEW_STATUS_BUTTON, TEXT)
