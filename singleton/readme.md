# Задача:
Реализовать класс-синглтон CurrencyBoard, в котором должны храниться данные о 10 наиболее востребованных валютах (GBP, USD, EUR + 7 выбранных вами).
* метод для получения информации о всех сохраненных в кэше валютах без запроса к сайту;
* метод о запросе курса новой валюты (с получением свежих данных с сервера) и добавлением её в кэш;
* метод класса для принудительного обновления данных о валютах update().
* метод check, вызывая который проверялось бы, когда загружены данные и если прошло больше 5 минут с момента последней загрузки, то запрос к серверу отправлялся.
Решение прокомментировать с помощью docstring, написанные методы покрыть тестами, где это возможно.

# Использование созданного класса:
```
curr = CurrencyBoard()
print("Курс евро:", curr.get_value('R01239'))
print("Курс доллара сша:", curr.get_value('R01235'))

# Добавалем новую валюту
curr.add_code('R01820')
# убеждаемся что кэш обновился
print("Курс доллара японской иены:", curr.get_value('R01820'))
```

# Вывод:
```
python3 money.py
Курс евро: 71,5457
Курс доллара сша: 63,3877
Курс доллара японской иены: 58,8421
```
