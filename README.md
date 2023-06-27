# 28.1-Final
Итоговый проект по автоматизации тестирования

Задание:

- Протестировать требования.
- Разработать тест-кейсы (не менее 15). Необходимо применить несколько техник тест-дизайна.
- Провести автоматизированное тестирование продукта (не менее 20 автотестов). Заказчик ожидает по одному автотесту на каждый написанный тест-кейс.
- Оформить описание обнаруженных дефектов. 

Для тестирования сайта была произведена проверка требований, данных заказчиком, составлены тест-кейсы для проверки соответсвия требованиям форм авторизации, регистрации, формы "Забыл пароль", формы восстановления пароля. 
При проверках использовались ручные и автоматизированные тесты, с помощью которых были найдены некоторые баги и составлены баг-реопрты. Автотесты написаны на языке программирования Python в среде Pycharm с использованием selenium и pytest.

Для тестирования страницы авторизации сайта были использованы техники тест-дизайна:

- классы эквивалентности,
- таблица принятия решений

Тесты настроены на запуск через терминал python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests.py

settings.py - регистрационные данные для позитивных тестов авторизации tests.py - набор автотестов

Объект тесирования: форма регистрации/авторизации сайта: https://b2c.passport.rt.ru

Ссылка на тестирование требований, тест-кейсы, баг-репорты:
https://docs.google.com/spreadsheets/d/1SgZuXdQVVRI21SaUnvgwqwXxbm9i2AF3-qKgx4IwyKM/edit?usp=sharing
