# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from instaparser.items import InstaparserItem
import re
import json
from urllib.parse import urlencode
from copy import deepcopy


class InstagramSpider(scrapy.Spider):
    # атрибуты класса
    name = 'instagram'
    allowed_domains = ['instagram.com']
    start_urls = ['https://instagram.com/']
    insta_login = 'insta_opt'
    insta_pwd = '#PWD_INSTAGRAM_BROWSER:10:1594675566:AWlQAGsBrzrbrjzIZ1tbjYwlW0LqXcpKBa+Uc3nXJQPcT08gK1qx' \
                'DR5qTwdVmUF4hMja/bFtZr6UT0vr+p6cR3ATeYpX86UVA7NeN2+G5aeTjioI42uhldF93K7htGeYmHMAIJCoIe8yDQ=='
    inst_login_link = 'https://www.instagram.com/accounts/login/ajax/'
    parse_user = 'kmemescluster'  # Пользователь, у которого собираем посты. Можно указать список

    graphql_url = 'https://www.instagram.com/graphql/query/?'
    posts_hash = 'eddbde960fed6bde675388aac39a3657'  # hash для получения данных о постах с главной страницы
    followers_hash = 'c76146de99bb02f6415203be841dd25a' # hash для получения подписчиков

    def parse(self, response: HtmlResponse):  # Первый запрос на стартовую страницу
        csrf_token = self.fetch_csrf_token(response.text)  # csrf token забираем из html
        yield scrapy.FormRequest(  # заполняем форму для авторизации
            self.inst_login_link,
            method='POST',
            callback=self.user_parse,  # метод который будет обрабатывать полученные значения
            formdata={'username': self.insta_login, 'enc_password': self.insta_pwd},
            headers={'X-CSRFToken': csrf_token}  # передаём csrf токен
        )

    # после авторизации мы попадаем на свою страницу
    def user_parse(self, response: HtmlResponse):
        j_body = json.loads(response.text)  # Преобразуем респонс в джейсон
        if j_body['authenticated']:  # Проверяем ответ после авторизации, чтобы понять удачно ли прошла авторизация
            yield response.follow(
                # переходим на желаемую страницу пользователя. Сделать цикл для кол-ва пользователей больше 2-ух
                f'/{self.parse_user}',
                # т.к. скрапи прекрасно работает с относительными ссылками - этого достаточно для перехода
                callback=self.user_data_parse,  # след. шаг
                cb_kwargs={'username': self.parse_user}
                # можем передавать любые значения. Это важно передавать именно так, а не брать из общего
                # глобального списка потому что мы можем перебирать это в цикле и у вас будут лететь айтемы
                # в абсолютно неопределённом порядке потому что асинхронно, поэтому надо передавать явно.
                # Поэтому мы передаём этот username в следующий метод user_data_parse явно
            )

    # принимаем username из предыдущего метода user_parse и
    # на руках будет иметь имя пользователя с которым работаем в данном методе
    def user_data_parse(self, response: HtmlResponse, username):
        user_id = self.fetch_user_id(response.text, username)  # Получаем id пользователя методом fetch_user_id
        variables = {'id': user_id,  # Формируем словарь для передачи даных в запрос
                     'first': 12}  # 12 постов. Можно больше (макс. 50)

        url_posts = f'{self.graphql_url}query_hash={self.posts_hash}&{urlencode(variables)}'
        # graphql+query_hash: Формируем ссылку для получения данных о постах.  urlencode кодирует параметры

        yield response.follow(
            url_posts,
            callback=self.user_posts_parse,
            cb_kwargs={'username': username,
                       'user_id': user_id,
                       'variables': deepcopy(variables)}
        )    # variables ч/з deepcopy во избежание гонок

    def user_posts_parse(self, response: HtmlResponse, username, user_id,
                         variables):  # Принимаем ответ. Не забываем про параметры от cb_kwargs
        j_data = json.loads(response.text)
        # здесь get это не get-запрос, а метод get у словаря. идём на 4 уровня в глубину.
        page_info = j_data.get('data').get('user').get('edge_owner_to_timeline_media').get('page_info')
        if page_info.get('has_next_page'):  # Если есть следующая страница
            variables['after'] = page_info['end_cursor']  # Новый параметр для перехода на след. страницу
            url_posts = f'{self.graphql_url}query_hash={self.posts_hash}&{urlencode(variables)}'
            yield response.follow(
                url_posts,
                callback=self.user_posts_parse,
                cb_kwargs={'username': username,
                           'user_id': user_id,
                           'variables': deepcopy(variables)}
            )
        posts = j_data.get('data').get('user').get('edge_owner_to_timeline_media').get('edges')  # Сами посты
        for post in posts:  # Перебираем посты, собираем данные
            item = InstaparserItem(
                user_id=user_id,
                photo=post['node']['display_url'],
                likes=post['node']['edge_media_preview_like']['count'],
                post=post['node']  # на всякий на будущее закидываем всю ноду в post, вдруг понадобятся данные
            )
        yield item  # В пайплайн



    def followers_parse(self, response:HtmlResponse, username, variables):
        j_data = json.loads(response.text)
        followers_info = j_data.get('data').get('user').get('edge_follower_by')
        if followers_info.get('has_next_page'): # Если есть следующая страница
            variables['after'] = followers_info['end_cursor']  # Новый параметр для перехода на след. страницу
            url_followers = f'{self.graphql_url}query_hash={self.followers_hash}&{urlencode(variables)}'
            yield response.follow(
                url_followers,
                callback=self.followers_parse,
                cd_kwargs={'followers_name': }
            )
        followers = j_data.get('data').get('user').get('edge_owner_to_timeline_media').get('edges')  # Сами подписчики
        




    # Получаем токен для авторизации
    def fetch_csrf_token(self, text):
        matched = re.search('\"csrf_token\":\"\\w+\"', text).group()
        return matched.split(':').pop().replace(r'"', '')

    # Получаем id желаемого пользователя. Т.к. в ответе id не представлен. id нужно вытаскивать из html
    def fetch_user_id(self, text, username):
        matched = re.search(
            '{\"id\":\"\\d+\",\"username\":\"%s\"}' % username, text
        ).group()
        return json.loads(matched).get('id')
