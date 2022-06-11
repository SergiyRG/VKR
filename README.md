## Инструкция
1. Скачайте архив с проектом OnlineLearn
2. Поместите папку с проектом по адресу: C:\OnlineLearn
3. Откройте консоль Windows Сmd
2. Создайте виртуальное окружение: python -m venv myvenv и активируйте: myvenv\Scripts\activate
3. Установите все необходимые пакеты: pip install -r requirements.txt
4. Создайте файл миграций: python manage.py makemigrations и добавьте файл миграции в БД: python manage.py migrate
5. Запустите проект с помощью команды: python manage.py runserver