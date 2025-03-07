from re import findall

import requests
from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bs4 import BeautifulSoup
from loader import cursor, Bot
import json
from aiogram import types
def parse_website(url, class_name, inner_class_name):
    response = requests.get(url)
    if response.status_code != 200:
        print(f'ошибка запроса: {response.status_code}')
    soup = BeautifulSoup(response.text, 'html.parser')
    parser_data = []
    elements = findall(class_= class_name)
    for element in elements:
        text = element.get_text(strip=True)
        img_tag = element.find('img')
        img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else None
        inner_element = element.find(class_=inner_class_name)
        inner_text = inner_element.get_text(strip=True) if inner_element else None
        link_url = element.get('href') if element.has_attr('href') else None
        link_url = link_url.split('?')[0]
        parser_data.append(text, img_url, inner_text, link_url)
        return parser_data
async def parser_update(user_id, bot: Bot, url):
    cursor.execute('SELECT id FROM data WHERE id=(?) )', [user_id])
    class_names = "styles_wrapper__5FoK7"
    inner_class_name = "styles_secondary__MzdEb"
    result = parse_website(url, class_names, inner_class_name)[:5]
    old_result = '7745791475.json'

