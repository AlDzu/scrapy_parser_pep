# Асинхронный парсер PEP на базе фреймворка Scrapy.
## Парсер документации Python

### Как запустить проект:
Чтобы развернуть проект, вам потребуется:
1) Клонировать репозиторий GitHub (не забываем создать виртуальное окружение и установить зависимости):
```python
git clone https://github.com/AlDzu/scrapy_parser_pep
```

2) Cоздать и активировать виртуальное окружение:
```python
python3 -m venv venv
source venv/bin/activate
```
3) Установить зависимости:
```python
python3 -m pip install --upgrade pip
pip install -r requirements.txt

## Примеры команд
Получение информации нововведениях в python:
```
scrapy crawl pep
```
Результат будет выведен в два файла формата .csv:
Файлы со списком PEP
Файлы со сводкой по статусам


Автор: Дзюба А.А.