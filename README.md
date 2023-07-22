# Тестовое задание

API для представления структуры компании.


```
python3 -m venv .venv
source ./.venv/bin/activate
python -m pip install -r requirements.txt
python ./src/manage.py migrate
```

Загрузка тестовых данных:
```
python ./src/manage.py loaddata ./src/company/fixtures/sample.json
```
