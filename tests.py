# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests.py


from selenium import webdriver

from settings import valid_email, valid_password, invalid_number, invalid_number_1, invalid_number_2, invalid_email, invalid_email_1, login, personal_account
from selenium.webdriver.common.by import By
import time
# driver = webdriver.Chrome()
# driver.get('https://google.com')

# тест RT-001 загрузка страницы авторизации
def test_passport_rt_positiv_autoris_main_page(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
# Make the screenshot of browser window:
    selenium.save_screenshot('result_1.png')

# тест RT-002 соответствие страницы авторизации требованиям
def test_passport_rt_positiv_autoris_main_page_right_1(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)

    assert selenium.find_element(By.CSS_SELECTOR, "section#page-right")

# тест RT-003 типы авторизации
def test_passport_rt_positiv_autoris_main_page_right_4(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    assert selenium.find_element(By.CSS_SELECTOR, "div#t-btn-tab-phone").text == "Телефон"

def test_passport_rt_positiv_autoris_main_page_right_5(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    assert selenium.find_element(By.CSS_SELECTOR, "div#t-btn-tab-mail").text == "Почта"

def test_passport_rt_positiv_autoris_main_page_right_6(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    assert selenium.find_element(By.CSS_SELECTOR, "div#t-btn-tab-login").text == "Логин"

def test_passport_rt_positiv_autoris_main_page_right_7(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    assert selenium.find_element(By.CSS_SELECTOR, "div#t-btn-tab-ls").text == "Лицевой счёт"

# тест RT-005 автоматическое изменение выбора аутентификации, при введении соответствующих данных (email)
def test_passport_rt_positiv_autoris_change_email(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
# add email
    field_email = selenium.find_element(By.ID, "username")
    field_email.click()
    field_email.clear()
    field_email.send_keys(valid_email)
    # add password
    field_pass = selenium.find_element(By.ID,"password")
    field_pass.click()
    assert selenium.find_element(By.CLASS_NAME, "rt-input__placeholder--top").text == "Электронная почта"

# тест RT-006 автоматическое изменение выбора аутентификации, при введении соответствующих данных (login)
def test_passport_rt_positiv_autoris_change_login(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
# add login
    field_login = selenium.find_element(By.ID, "username")
    field_login.click()
    field_login.clear()
    field_login.send_keys(login)
#     # add password
    field_pass = selenium.find_element(By.ID,"password")
    field_pass.click()
    assert selenium.find_element(By.CLASS_NAME, "rt-input__placeholder--top").text == "Логин"

# тест RT-007 автоматическое изменение выбора аутентификации, при введении соответствующих данных (personal_account)(БАГ)
def test_passport_rt_positiv_autoris_change_personal_account(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
# add personal_account
    field_personal_account = selenium.find_element(By.ID, "username")
    field_personal_account.click()
    field_personal_account.clear()
    field_personal_account.send_keys(personal_account)
    time.sleep(5)
#     # add password
    field_pass = selenium.find_element(By.ID,"password")
    field_pass.click()
    assert selenium.find_element(By.CLASS_NAME, "rt-input__placeholder--top").text == "Лицевой счет"

# тест RT-010 авторизация пользователя с валидными данными (email+пароль)
def test_passport_rt_positiv_autoris(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    # add email
    field_email = selenium.find_element(By.ID, "username")
    field_email.click()
    field_email.clear()
    field_email.send_keys(valid_email)

    # add password
    field_pass = selenium.find_element(By.ID,"password")
    field_pass.clear()
    field_pass.send_keys(valid_password)
    btn_submit = selenium.find_element(By.ID,"kc-login")
    btn_submit.click()
    time.sleep(10)

    user_card = selenium.find_element(By.CSS_SELECTOR, "div#app > main > div > div:nth-of-type(2) > div")
    if user_card:
        # Make the screenshot of browser window:
        selenium.save_screenshot('result_2.png')
    else:
        raise Exception("login error")

# тест RT-011 авторизация пользователя в системе с незарегистрированным номером телефона
def test_passport_rt_negativ_autoris_1(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    # add number
    field_number = selenium.find_element(By.ID, "username")
    field_number.click()
    field_number.clear()
    field_number.send_keys(invalid_number)

    # add password
    field_pass = selenium.find_element(By.ID,"password")
    field_pass.clear()
    field_pass.send_keys(valid_password)
    btn_submit = selenium.find_element(By.ID,"kc-login")
    btn_submit.click()
    time.sleep(10)

    filed_error = selenium.find_element(By.ID, "form-error-message")
    if filed_error:
        # Make the screenshot of browser window:
        selenium.save_screenshot('result_3.png')
    else:
        raise Exception("error_1")

# тест RT-012 авторизация пользователя в системе по номеру телефона с неверным форматом (количество цифр меньше, чем нужно)
def test_passport_rt_negativ_autoris_2(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    # add number
    field_number = selenium.find_element(By.ID, "username")
    field_number.click()
    field_number.clear()
    field_number.send_keys(invalid_number_1)

    # add password
    field_pass = selenium.find_element(By.ID,"password")
    field_pass.clear()
    field_pass.send_keys(valid_password)
    btn_submit = selenium.find_element(By.ID,"kc-login")
    btn_submit.click()
    time.sleep(10)

    filed_help = selenium.find_element(By.CSS_SELECTOR, "section#page-right > div > div > div > form > div > div:nth-of-type(2) > span")
    if filed_help:
# Make the screenshot of browser window:
        selenium.save_screenshot('result_4.png')
    else:
        raise Exception("error_2")

# тест RT-014 авторизация пользователя в системе по номеру телефона с неверным форматом (пустая строка)
def test_passport_rt_negativ_autoris_3(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    # add number
    field_number = selenium.find_element(By.ID, "username")
    field_number.click()
    field_number.clear()
    field_number.send_keys(invalid_number_2)

    # add password
    field_pass = selenium.find_element(By.ID,"password")
    field_pass.clear()
    field_pass.send_keys(valid_password)
    btn_submit = selenium.find_element(By.ID,"kc-login")
    btn_submit.click()
    time.sleep(10)

    assert selenium.find_element(By.CSS_SELECTOR, "section#page-right > div > div > div > form > div > div:nth-of-type(2) > span").text == "Введите номер телефона"

# тест RT-013 Авторизация пользователя в системе по номеру телефона с неверным форматом (количество цифр больше, чем нужно)
def test_passport_rt_negativ_autoris_3(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    # add number
    field_number = selenium.find_element(By.ID, "username")
    field_number.click()
    field_number.clear()
    field_number.send_keys(invalid_number_3)
    time.sleep(10)
    # Make the screenshot of browser window:
    selenium.save_screenshot('result_passport_rt_5.png')


# тест RT-015 Авторизация пользователя в системе с незарегистрированной электронной почтой
def test_passport_rt_negativ_autoris_4(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    # add number
    field_email = selenium.find_element(By.ID, "username")
    field_email.click()
    field_email.clear()
    field_email.send_keys(invalid_email)

    # add password
    field_pass = selenium.find_element(By.ID,"password")
    field_pass.clear()
    field_pass.send_keys(valid_password)
    btn_submit = selenium.find_element(By.ID,"kc-login")
    btn_submit.click()
    time.sleep(10)

    assert selenium.find_element(By.CSS_SELECTOR, "span#form-error-message").text == "Неверный логин или пароль"

# тест RT-016 Авторизация пользователя в системе по электронной почте с неверным форматом (пустая строка)
def test_passport_rt_negativ_autoris_5(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    # add number
    field_number = selenium.find_element(By.ID, "t-btn-tab-mail")
    field_number.click()
    field_number = selenium.find_element(By.ID, "username")
    field_number.click()
    field_number.clear()
    field_number.send_keys(invalid_email_1)

    # add password
    field_pass = selenium.find_element(By.ID,"password")
    field_pass.clear()
    field_pass.send_keys(valid_password)
    btn_submit = selenium.find_element(By.ID,"kc-login")
    btn_submit.click()
    time.sleep(10)

    assert selenium.find_element(By.CSS_SELECTOR, "section#page-right > div > div > div > form > div > div:nth-of-type(2) > span").text == "Введите адрес, указанный при регистрации"

# тест RT-017 Авторизация по валидной электронной почте без пароля (БАГ)
def test_passport_rt_negativ_autoris_6(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    # add email
    field_email = selenium.find_element(By.ID, "username")
    field_email.click()
    field_email.clear()
    field_email.send_keys(valid_email)

    # add password
    # field_pass = selenium.find_element(By.ID,"password")
    # field_pass.clear()
    # field_pass.send_keys(valid_password)
    btn_submit = selenium.find_element(By.ID,"kc-login")
    btn_submit.click()
    time.sleep(10)

    assert selenium.find_element(By.ID, "password").text == "Введите пароль"


# тест RT-018 Переход на страницу авторизации через соц. сети (vk)
def test_passport_rt_positiv_vk(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    vk = selenium.find_element(By.ID,"oidc_vk")
    vk.click()
    time.sleep(10)
    vk_autoris = selenium.find_element(By.CSS_SELECTOR,"div#oauth_wrap_content > div > a")
    if vk_autoris:
        # Make the screenshot of browser window:
        selenium.save_screenshot('result_passport_rt_6.png')
    else:
        raise Exception("login error_1")

# тест RT-019 Переход на страницу авторизации через соц. сети (одноклассники)
def test_passport_rt_positiv_ok(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    ok = selenium.find_element(By.ID,"oidc_ok")
    ok.click()
    time.sleep(10)
    ok_autoris = selenium.find_element(By.CSS_SELECTOR,"div#widget-el > div > a")
    if ok_autoris:
        # Make the screenshot of browser window:
        selenium.save_screenshot('result_passport_rt_7.png')
    else:
        raise Exception("login error_2")
#
# тест RT-020 Переход на страницу авторизации через соц. сети (одноклассники)
def test_passport_rt_positiv_mail(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    mail = selenium.find_element(By.ID,"oidc_mail")
    mail.click()
    time.sleep(10)
    mail_autoris = selenium.find_element(By.CSS_SELECTOR,"div#wrp > div > span")
    if mail_autoris:
        # Make the screenshot of browser window:
        selenium.save_screenshot('result_passport_rt_8.png')
    else:
        raise Exception("login error_3")

# тест RT-021 Переход на страницу авторизации через соц. сети (google)
def test_passport_rt_positiv_google(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    google = selenium.find_element(By.ID,"oidc_google")
    google.click()
    time.sleep(10)
    google_autoris = selenium.find_element(By.CSS_SELECTOR,"div#initialView > div:nth-of-type(2)")
    if google_autoris:
        # Make the screenshot of browser window:
        selenium.save_screenshot('result_passport_rt_9.png')
    else:
        raise Exception("login error_4")

# тест RT-022 Переход на страницу авторизации через соц. сети (yandex) (Страница не открывается только при работе автоматизированного тестового ПО)
def test_passport_rt_positiv_yandex(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    yandex = selenium.find_element(By.CSS_SELECTOR,"a#oidc_ya")
    yandex.click()
    time.sleep(10)
    yandex_autoris = selenium.find_element(By.CSS_SELECTOR,"div#root > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div:nth-of-type(2)")
    if yandex_autoris:
        # Make the screenshot of browser window:
        selenium.save_screenshot('result_passport_rt_10.png')
    else:
        raise Exception("login error_5")

# тест RT-023 Переход на страницу Восстановления пароля
def test_passport_rt_positiv_password_recovery(selenium):
    selenium.get("https://b2c.passport.rt.ru")
    time.sleep(10)
    forgot_password = selenium.find_element(By.ID,"forgot_password")
    forgot_password.click()
    password_recovery = selenium.find_element(By.CSS_SELECTOR,"section#page-right > div > div > h1").text == "Восстановление пароля"
    time.sleep(10)
    if password_recovery:
        # Make the screenshot of browser window:
        selenium.save_screenshot('result_passport_rt_11.png')
    else:
        raise Exception("login error_6")

