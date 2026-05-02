#!/bin/sh

echo "Ждём базу данных..."
sleep 5

echo "Применяем миграции..."
python manage.py migrate

echo "Собираем статику..."
python manage.py collectstatic --noinput

echo "Проверяем наличие данных..."

python manage.py shell <<EOF
from api.models import Book
from api.parsing_json.parsing_json import parse_json, download_json

if Book.objects.count() == 0:
    print("База пустая. Загружаем данные...")
    download_json()
    parse_json()
else:
    print("Данные уже есть. Пропускаем парсинг.")
EOF

echo "Запускаем сервер..."
gunicorn config.wsgi:application --bind 0.0.0.0:8000