import json
import os
import django

from django.conf import settings

from .utils_for_parse import (
    print_info,
    download_json,
    download_picture,
    check_keywords
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from ..models import Book, Category, Author


def parse_json() -> None:
    file_path = os.path.join(settings.BASE_DIR, 'api', 'parsing_json', 'books.json')

    with open(file_path, 'r') as f:
        data = json.load(f)

    images_dir = os.path.join(settings.BASE_DIR, 'api', 'parsing_json', 'images')
    os.makedirs(images_dir, exist_ok=True)

    keywords = [
        'title', 'isbn', 'pageCount', 'publishedDate', 'thumbnailUrl',
        'shortDescription', 'longDescription', 'status', 'authors'
    ]

    without_isbn = []
    duplicate_isbn = []
    duplicate_book = []

    count = 0

    for item in data:

        values_for_db = {
            keyword: check_keywords(keyword, item)
            for keyword in keywords
        }

        # image
        if values_for_db.get('thumbnailUrl'):
            download_picture(values_for_db['thumbnailUrl'])

        # categories
        categories = []
        if not item.get('categories'):
            cat, _ = Category.objects.get_or_create(title="Новинки")
            categories.append(cat)
        else:
            for name in item.get('categories', []):
                cat, _ = Category.objects.get_or_create(title=name)
                categories.append(cat)

        # authors
        authors = []
        for name in item.get('authors', []):
            author, _ = Author.objects.get_or_create(name=name)
            authors.append(author)

        title = values_for_db['title']
        isbn = values_for_db['isbn']

        # проверка дублей
        if isbn:
            exists = Book.objects.filter(isbn=isbn).first()
            if exists:
                if exists.title == title:
                    print(f"Книга '{title}' уже существует.")
                    continue

                duplicate_isbn.append(
                    f'Книга 1: {title}\n'
                    f'Книга 2: {exists.title}\n'
                    f'ISBN: {isbn}'
                )
                continue
        else:
            exists = Book.objects.filter(title=title).first()
            if exists:
                print(f"Книга '{title}' уже существует.")
                without_isbn.append(title)
                continue
            without_isbn.append(title)

        # создание книги (НО БЕЗ save + bulk_create вместе)
        book = Book.objects.create(
            title=title,
            isbn=isbn,
            pagecount=values_for_db['pageCount'],
            publisheddate=values_for_db['publishedDate'],
            thumbnailurl=values_for_db['thumbnailUrl'],
            shortdescription=values_for_db['shortDescription'],
            longdescription=values_for_db['longDescription'],
            status=values_for_db['status']
        )

        if categories:
            book.categories.add(*categories)

        if authors:
            book.authors.add(*authors)

        count += 1
        print(f'Книга {title} добавлена')
        print(f'Обработано: {count}')
        print('__________________')

    print(f'\nКниг всего обработано: {count}\n')
    print_info(without_isbn, duplicate_isbn, duplicate_book)


if __name__ == "__main__":
    download_json()
    parse_json()