Проект:

requirments.txt

python manage.py runserver 8000<br>
celery -A google_sheets beat<br>
celery -A google_sheets worker<br>

1 раз в час обновляется и записывается в базу, курс валют<br>
1 раз в минуту обновляется и записываются в базу гугл таблицы

'print'ы всунул для тестирования в очереди задач. можно убрать.

#TODO
- docker
- запуск таски обновления базы при открытии страницы у пользователя ("onload")
- деплой на сервере


