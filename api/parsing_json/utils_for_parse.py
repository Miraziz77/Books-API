import os
import requests
from typing import List, Optional, Union
from dotenv import load_dotenv
from django.conf import settings

load_dotenv()

URL_FOR_GET_JSON_FILE = os.getenv('URL_FOR_GET_JSON_FILE', default='url')


def print_info(
        without_isbn: List,
        duplicate_isbn: List,
        duplicate_book: List
) -> None:

    if without_isbn:
        print("Следующие книги не имеют ISBN:")
        for book in without_isbn:
            print(book)
        print('\n')

    if duplicate_isbn:
        print("Следующие книги могут иметь дубликаты ISBN:")
        for book in duplicate_isbn:
            print(book)
        print('\n')

    if duplicate_book:
        print("Следующие книги имеют дубли:")
        for book in duplicate_book:
            print(book)
        print('\n')


def check_keywords(keyword: str, item: dict) -> Optional[Union[str, int]]:

    if keyword == 'publishedDate':
        if 'publishedDate' in item:
            return item['publishedDate'].get('$date', None)
        return None

    return item.get(keyword, None)


def download_picture(url: str) -> None:
    images_dir = os.path.join(settings.BASE_DIR, 'api', 'parsing_json', 'images')
    os.makedirs(images_dir, exist_ok=True)

    filename = os.path.join(images_dir, os.path.basename(url))

    if os.path.exists(filename):
        print(f"Изображение '{filename}' уже существует.")
        return

    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)
    else:
        print(f"Ошибка загрузки изображения: {url}")


def download_json() -> None:
    file_path = os.path.join(settings.BASE_DIR, 'api', 'parsing_json', 'books.json')

    response = requests.get(URL_FOR_GET_JSON_FILE)

    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Файл сохранён: {file_path}")
    else:
        print("Ошибка загрузки JSON:", response.status_code)