import requests
import json
from config import keys

class ConvertExc(Exception):
    pass

class ConvertCurrency:
    @staticmethod
    def convert(quote: str, base: str, amout: str):
        if quote == base:
            raise ConvertExc(f'Невозможно перевести одинаковые валюты: {quote}')
        try:
            key_quote = keys[quote]
        except KeyError:
            raise ConvertExc(f'Не удалось обрабодать валюту: {quote}\nСписок всех валют: /values')

        try:
            key_base = keys[base]
        except KeyError:
            raise ConvertExc(f'Не удалось обрабодать валюту: {base}\nСписок всех валют: /values')
        try:
            amout = float(amout)
            amout2 = amout
        except ValueError:
            raise ConvertExc(f'Не удалось обрабодать количество: {amout}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={key_quote}&tsyms={key_base}')
        total_base = json.loads(r.content)[keys[base]]
        summ = total_base * amout

        return summ