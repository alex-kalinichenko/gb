from bs4 import BeautifulSoup as bs
import requests
from pymongo import MongoClient


def get_salary(s):
    def get_currency(s):
        s_len = len(s)
        cur = ''
        i = 0
        while i < s_len:
            a = s[i]
            if '0' <= a <= '9':
                i += 1
            else:
                cur = cur + a
                i += 1
        return cur
    if s.startswith('от'):
        s = s.replace('от', '')
        cur = get_currency(s)
        s_min = int(s.replace(cur, ''))
        s_max = 'NA'
    elif s.startswith('до'):
        s = s.replace('до', '')
        cur = get_currency(s)
        s_max = int(s.replace(cur, ''))
        s_min = 'NA'
    elif s.find('-') >= 5:
        pos = s.find('-')
        s_min = int(s[:pos])
        s_max = s[pos + 1:]
        cur = get_currency(s_max)
        s_max = int(s_max.replace(cur, ''))
    else:
        s_min = 'NA'
        s_max = 'NA'
        cur = 'NA'
    return s_min, s_max, cur


site = 'https://hh.ru/search/vacancy?'
areas = ['area=2', 'area=1']
search = 'data+scientist'  # data+scientist  python
headers = {'User-Agent': 'Chrome/80.0.4150.1', 'Accept': '*/*'}
items = []

i = 1
for area in areas:
    link = site + area + '&st=searchVacancy&text=' + search + '&fromSearch=true'
    next_page = '#'
    while next_page:
        try:
            response = requests.get(link, headers=headers, timeout=5).text
        except requests.exceptions.RequestException:
            print('General Error')

        soup = bs(response, 'lxml')
        if area == 'area=2':
            city = 'Spb'
        else:
            city = 'Msk'
        for tag in soup.find_all('div', {'class': 'vacancy-serp-item'}):
            vacancy = tag.find('a', {'class': 'bloko-link HH-LinkModifier'})
            salary = tag.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})
            if salary:
                salary = salary.get_text().replace(" ", "").replace("\xa0", "")  # неразрывный пробел в зп
                s_min, s_max, cur = get_salary(salary)
            else:
                s_min, s_max, cur = 'NA', 'NA', 'NA'
            company = tag.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'})
            if not company:
                company = tag.find('div', {'class': 'vacancy-serp-item__meta-info'})
            print(i, city, vacancy.get_text(), s_min, s_max, cur, company.get_text(strip=True), vacancy['href'])

            item = {'search': search, 'position': vacancy.get_text(), 'site': 'hh.ru', 'city': city,
                    'company': company.get_text(strip=True), 'min_salary': s_min, 'max_salary': s_max,
                    'currency': cur, 'link': vacancy['href']}
            items.append(item)
            i += 1
            salary = ''
        next_page_link = soup.find('a', {"data-qa": "pager-next"})
        if next_page_link:
            next_page = next_page_link['href']
        else:
            next_page = ''
        link = 'https://hh.ru' + next_page

client = MongoClient('localhost', 27017)
db = client['vacancy']
vac = db.vac
vac.insert_many(items)
