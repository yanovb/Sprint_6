from datetime import datetime
import random

NAME = 'Ян'
LAST_NAME = 'Янов'
ADDRESS = 'Ленинградский проспект, 76 к3 '
PHONE_NUMBER = '+79099990909'
DAY = datetime.today().strftime('%d')
RENTAL_PERIOD = str(random.choice([
    'сутки',
    'двое суток',
    'трое суток',
    'четверо суток',
    'пятеро суток',
    'шестеро суток',
    'семеро суток'
]))
SCOOTER_COLOR = str(random.choice([
    'black',
    'grey'
]))
COMMENT = 'test comment'
TEXT = 'Посмотреть статус'
QUESTIONS_ABOUT_IMPORTANT_TEXT = 'Вопросы о важном'
TITLE = 'Дзен'
DOMAIN_NAME = 'dzen'
