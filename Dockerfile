FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

# установка netcat (нужен для проверки БД)
RUN apt-get update && apt-get install -y netcat-openbsd

# делаем файл исполняемым
RUN chmod +x entrypoint.sh

# запуск НЕ manage.py напрямую
CMD ["/app/entrypoint.sh"]