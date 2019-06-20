from __future__ import annotations
from urllib.request import urlopen
from xml.etree import ElementTree as ET
from datetime import datetime, timedelta
import json

def json_decorator(func):
    """
    декоратор для конвертации в json 
    """
    def wrapper(self):
        return json.dumps(func(self), sort_keys=True, indent=4, ensure_ascii=False)
    return wrapper

class CurrencyBoard:
    _instance = None

    def __new__(aclass, *args, **kwargs):
        """
        Реализация "Одиночки"
		"""
        if not isinstance(aclass._instance, aclass):
            aclass._instance = object.__new__(aclass, *args, **kwargs)
        return aclass._instance

    def __init__(self):
        """
        Инициализация
        """
        self.codes = ['R01239', 'R01235', 'R01035', 'R01815']
        self.cache = self.get_currencies()
        self.update()

    def get_currencies(self):
        """
        Получение курса валют
        """
        cur_res_str = urlopen("http://www.cbr.ru/scripts/XML_daily.asp")
        result = {}
        cur_res_xml = ET.parse(cur_res_str)
        root = cur_res_xml.getroot()
        valutes = root.findall('Valute')
        for el in valutes:
            valute_id = el.get('ID')
            if str(valute_id) in self.codes:
                valute_cur_val = el.find('Value').text
                result[valute_id] = valute_cur_val
        return result

    @json_decorator
    def get_values(self):
        """
        Метод для получения всех курсов валют
        """   
        return self.cache

    def update(self):
        """
        Метод форсированого обновления
        """
        self.cache.clear()
        self.cache = self.get_currencies()
        self.updateTime = datetime.now()

    def check(self):
        """
        Метод для обновления по прошествии 5 минут с последнего обновления
        """
        if datetime.now() >= timedelta(minutes=5) + self.updateTime:
            self.update()

    def get_value(self, code):
        """
        Метод для получения курса валюты по коду
        """ 
        return self.cache[code]

    def add_code(self, code):
        """
        Метод для добавления нового курса валюты
        """ 
        self.codes = self.codes + [code]
        self.update()

curr = CurrencyBoard()
print("Курс евро:", curr.get_value('R01239'))
print("Курс доллара сша:", curr.get_value('R01235'))

# Добавалем новую валюту
curr.add_code('R01820')
# убеждаемся что кэш обновился
print("Курс доллара японской иены:", curr.get_value('R01820'))

# выводим в виде джейсон файла
print('json:')
print(curr.get_values())