import sys
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт

import requests
from PIL import Image

# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:


lon = int(input())
lat = int(input())
delta = "0.002"
address_ll = f"{lon},{lat}"

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

# Долгота и широта:
toponym_longitude, toponym_lattitude = (lon, lat)

delta = "0.005"

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    "ll": ",".join([str(toponym_lattitude), str(toponym_longitude)]),
    "spn": ",".join([delta, delta]),
    "l": "map"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()

