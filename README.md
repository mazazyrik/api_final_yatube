# Как запустить проект:

## Клонировать репозиторий и перейти в него в командной строке:

```
git clone ...
cd kittygram
```

**Cоздать и активировать виртуальное окружение:**

```
python3 -m venv env
source env/bin/activate
```

**Установить зависимости из файла requirements.txt:**
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```

**Запустить проект:** 

python3 manage.py runserver

# Примеры запросов и ответов:
```
/api/v1/posts/ Response:{

"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": 
[

    {}
]
}
```
```
/api/v1/posts/ Post data:{ "text": "string", "image": "string", "group": 0 } Response:{

"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```
```
api/v1/jwt/create/ Post data:{

"username": "string",
"password": "string"
} Response:{

"refresh": "string",
"access": "string"
}
```