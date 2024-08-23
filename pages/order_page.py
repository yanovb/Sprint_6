import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Добавляем значение в поле')
    def add_value(self, element, value):
        elm = self.waiting_element(element)
        elm.send_keys(value)

    @allure.step('Создаем заказ')
    def make_order(self, name, last_name, address, phone_number, comment):
        self.click_element(OrderPageLocators.TOP_ORDER_BUTTON)
        self.add_value(OrderPageLocators.NAME_FIELD, name)
        self.add_value(OrderPageLocators.LAST_NAME_FIELD, last_name)
        self.add_value(OrderPageLocators.ADDRESS_FIELD, address)
        self.click_element(OrderPageLocators.METRO_FIELD)
        self.click_element(OrderPageLocators.SOKOL_METRO_STATION)
        self.add_value(OrderPageLocators.PHONE_NUMBER_FIELD, phone_number)
        self.click_element(OrderPageLocators.NEXT_BUTTON)
        self.click_element(OrderPageLocators.SCOOTER_DATE_FIELD)
        self.click_element(OrderPageLocators.DATE_IN_CALENDAR)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click_element(OrderPageLocators.SELECTED_RENTAL_PERIOD)
        self.click_element(OrderPageLocators.SELECTED_SCOOTER_COLOR)
        self.add_value(OrderPageLocators.COMMENT_FIELD, comment)
        self.click_element(OrderPageLocators.ADD_ORDER_FIELD)
        self.click_element(OrderPageLocators.ORDER_CONFIRMATION_BUTTON)

    @allure.step('Проверяем ожидаемый текст элемента')
    def check_text(self, expected_result):
        elm = self.waiting_element(OrderPageLocators.VIEW_STATUS_BUTTON)
        assert elm.text == expected_result
