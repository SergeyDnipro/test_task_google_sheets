Проект:

requirments.txt

python manage.py runserver 8000
celery -A google_sheets beat
celery -A google_sheets worker

1 раз в час обновляется и записывается в базу, курс валют
1 раз в минуту обновляется и записываются в базу гугл таблицы

#TODO
- docker
- запуск таски обновления базы при открытии страницы у пользователя ("onload")
- деплой на сервере


