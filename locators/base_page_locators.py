from selenium.webdriver.common.by import By


class BasePageLocators:
    COOKIE_BUTTON = (By.XPATH, './/button[text()="да все привыкли"]')
    TOP_ORDER_BUTTON = (By.XPATH, './/div[@class="Header_Nav__AGCXC"]/button[1]')
    BOTTOM_ORDER_BUTTON = (By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button')
    SCOOTER_LOGO = (By.XPATH, './/a[@class="Header_LogoScooter__3lsAR"]')
    SECTION_ABOUT_QUESTIONS = (By.XPATH, './/div[text()="Вопросы о важном"]')
