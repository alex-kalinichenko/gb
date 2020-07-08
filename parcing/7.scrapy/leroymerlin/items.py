# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Compose    # Подключаем обраотчики


def cleaner_photo(value):       # Функция для изменения ссылок фотографий
    # if value[:2] == '//':       # обязательно проверять, что пришло и если не то,
    #     return f'http:{value}'  # возвращать то что пришло без изменений,чтобы scrapy не ломался
    return value


def cleaner_price(price):
    price = int(price[0].replace(' ', '').replace('.00', ''))
    # print('cleaner_space', type(price), price)
    return price


class LeroymerlinItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()  # Применяем обработчики
    name = scrapy.Field(output_processor=TakeFirst())  # output процессор. его мы вызываем. Извлечение строки из листа
    photos = scrapy.Field(input_processor=MapCompose(cleaner_photo))  # Map в Питоне применяет функцию к каждому
    # элементу последовательности. Здесь аналогично: берётся список который прилетает на этапе парсинга
    # и обрабатывается каждый элемент списка, т.к. нет экстрактов. В скобках указываем функцию, а не
    # выхываем т.е. без ()
    # у кажого поля есть пара - инпут и отпут процессор. инпут применяется на этапе сбора,
    # аутпут процессор применяется на этапе yield
    price = scrapy.Field(output_processor=Compose(cleaner_price))
