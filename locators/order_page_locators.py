from selenium.webdriver.common.by import By
from data import *
from locators.base_page_locators import BasePageLocators


class OrderPageLocators(BasePageLocators):
    NAME_FIELD = (By.XPATH, './/input[@placeholder="* Имя"]')
    LAST_NAME_FIELD = (By.XPATH, './/input[@placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_FIELD = (By.XPATH, './/input[@placeholder="* Станция метро"]')
    SOKOL_METRO_STATION = (By.XPATH, './/div[text()="Сокол"]')
    PHONE_NUMBER_FIELD = (By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, './/button[text()="Далее"]')
    SCOOTER_DATE_FIELD = (By.XPATH, './/input[@placeholder="* Когда привезти самокат"]')
    DATE_IN_CALENDAR = (By.XPATH, f'.//div[text()="{DAY}"]')
    RENTAL_PERIOD_FIELD = (By.XPATH, './/div[text()="* Срок аренды"]')
    SELECTED_RENTAL_PERIOD = (By.XPATH, f'.//div[text()="{RENTAL_PERIOD}"]')
    SELECTED_SCOOTER_COLOR = (By.ID, f'{SCOOTER_COLOR}')
    COMMENT_FIELD = (By.XPATH, './/input[@placeholder="Комментарий для курьера"]')
    ADD_ORDER_FIELD = (By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]')
    ORDER_CONFIRMATION_BUTTON = (By.XPATH, './/button[text()="Да"]')
    VIEW_STATUS_BUTTON = (By.XPATH, './/button[text()="Посмотреть статус"]')
