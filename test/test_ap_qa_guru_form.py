import os
import time
from selene import browser, have, be
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver import Keys


def test_practice_form():
    browser.open('/')

    """Закрываем всплывающее окно и выполняем проверку что находимся на нужной странице"""
    s('[data-testid="ClearIcon"]').click()
    s('.MuiTypography-h4').should(have.exact_text('Practice form'))

    """Заполняем First и Last Name"""
    s('[type=text][data-testid=firstName]').should(be.blank).type("Alex")
    s('[type=text][data-testid=lastName]').should(be.blank).type("Davydov")

    """Заполняем Email"""
    s('[type=text][data-testid=email]').should(be.blank).type('AlexDavydov92@gmail.com')

    """Заполняем Mobile"""
    s('[name=phone]').type('8005553535')

    """Выбираем Language"""
    ss('[role=button]')[0].click()
    ss('li.MuiMenuItem-root')[2].click()

    """Заполняем Date of birth"""
    s('[data-testid=dateOfBirth]').click().type('20061992').press_enter()

    """Выбираем Gender"""
    s('[data-testid=gender][value=Male]').click()

    """Выбираем Gobbies"""
    s('[data-testid=hobbies][value=Reading]').click()


    """Выбираем Subject"""
    ss('[role=button]')[1].click()
    ss('li.MuiMenuItem-root')[3].click().press_escape()

    """Выбираем State"""
    ss('[role=button]')[3].click()
    ss('li.MuiMenuItem-root')[9].click()

    """Выбираем City"""
    ss('[role=button]')[4].click()
    ss('li.MuiMenuItem-root')[2].click()

    """Двигаем Slider"""
    for i in range(1, 25):
        browser.element('.MuiSlider-thumb').element('input').type(Keys.ARROW_RIGHT)

    """Заполняем Address"""
    s('[data-testid=address]').type("South Street")

#    """Подгружаем Picture"""
#    s('[role=presentation]').send_keys(os.path.normpath('image/self.png'))


    s('[type=submit]').click()
    time.sleep(4)






