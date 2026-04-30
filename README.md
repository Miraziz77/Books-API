# 📚 Books API

REST API для управления каталогом книг. Проект реализован на Django и Django REST Framework.

## 🚀 Возможности

* 📖 Просмотр списка книг
* 🔍 Фильтрация и поиск
* ➕ Добавление новых книг
* ✏️ Редактирование данных
* ❌ Удаление книг
* 👤 Регистрация и авторизация пользователей (JWT)
* 📂 Категории и авторы
* 🖼 Загрузка изображений книг

---

## 🛠 Технологии

* Python 3.12+
* Django
* Django REST Framework
* Django Filter
* requests
* Djoser
* SimpeJWT
* Python-dotenv
* DRF-YASG
* SQLite
* Docker
* docker-compose

---

## 📦 Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/Miraziz77/Books-API.git
cd Books-API
```

---

### 2. Запуск через Docker (рекомендуется)

```bash
docker-compose up --build
```

После запуска:

* API будет доступен: http://localhost:8000/
* Swagger документация: http://localhost:8000/swagger/

---

### 3. Запуск без Docker

#### Установка зависимостей

```bash
pip install -r requirements.txt
```

#### Применение миграций

```bash
python manage.py migrate
```

#### Создание суперпользователя

```bash
python manage.py createsuperuser
```

#### Запуск сервера

```bash
python manage.py runserver
```

---

## 🔐 Аутентификация

Используется JWT:

* Получение токена: `/api/token/`
* Обновление токена: `/api/token/refresh/`

---

## 📚 API эндпоинты

Примеры:

* `GET /api/books/` — список книг
* `POST /api/books/` — создать книгу
* `GET /api/books/{id}/` — получить книгу
* `PUT /api/books/{id}/` — обновить
* `DELETE /api/books/{id}/` — удалить

---

## 📁 Структура проекта

```
Books-API/
│
├── config/          # настройки проекта
├── api/             # приложения (books, users и т.д.)
├──   parsing_json/    # скрипты парсинга книг
├── docker-compose.yml
├── requirements.txt
└── manage.py
```

---

## 📥 Загрузка данных

В проекте есть скрипт для парсинга книг:

```bash
python manage.py shell
```

И затем вызвать соответствующий скрипт из `parsing_json`.

---

## 🧪 Тестирование API

Для тестирования можно использовать:

* Swagger UI
* Postman

---

## 👨‍💻 Автор

Miraziz

GitHub: https://github.com/Miraziz77
