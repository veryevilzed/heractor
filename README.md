
HERACTOR v.1.0
==============

Исполняемый модуль:
-------------------

 heract.py --config=config.json


Конфигурационный фаил (config.json):
------------------------------------

Формат:

```json
{
    "section": {
        "key": "value"
    }
}
```

Пример файла (config.json)

```json
{
    "main":{
        "path": "../example/",
        "templates": "./templates/",
        "out": "./out/",
        "structure": "./structure.json",
        "plugins": [
            "heractor.plugins.buildmenu.build",
            "heractor.plugins.breadcrumps.build"
        ],
        "global": {
            "static": "/static/"
        }
    },
    "production": {
        "base": "main"
    },
    "debug": {
        "base": "production"
    }
}
```

main, production, debug - секции файла включаются при сборке выбором --section=main

Параметры:

* global - набор глобальных констант, будет доступен в каждом шаблоне, можно вынести пути к статике, заголовки и т.п.
* base - берет настройки из другой секции и дополняет/перекрывает своими
* path - путь к корню сайта, чтоб не указывать полные пути (не обязательно)
* templates - путь к каталогу с шаблонами (может быть задан как массив)
* out - пусть куда будет построен сайт
* structure - путь к карте сайта, параметрам страниц
* plugins - список дополнений расширяющих шаблоны ( см. /heractor/plugins )


Конфигурационный фаил (structure.json):
---------------------------------------

```json
{
    "index": {
        "template": "index.html",
        "name": "Главная",
        "navigation": true,
        "title": "My First Static Site",
        "subtitle": "Главная",
        "subitems": {
            "about": {
                "template": "about.html",
                "name": "Главная",
                "navigation": true,
                "subtitle": "О нас",
                "include": "data.json about",
                "include_format": "json"
            },
            "contact": {
                "template": "contact.html",
                "subtitle": "Контактная информация",
                "name": "Главная",
                "navigation": true
            }
        },
        "hidden": {
                "template": "hidden.html",
                "subtitle": "Скрытая страница",
                "name": "Скрытая",
                "navigation": false
        }
    }
}
```

Параметры:

Элемент это имя раздела (index.html, about.html, contact.html, hidden.html)

* template - имя шаблона
* skip - пропустить сборку этого раздела
* name - имя страницы (используется в дополнениях таких как menu)
* navigation - показывать ли в навигации
* include - добавить данные из файла (для структурных форматов можно указывать группу "data.json about"
* include_format - формат данных (json, yaml, rest)
* title / subtitle - костанты для шаблонов
* folder_name - имя каталога для subitems ( по умолчанию берется key )

Структура сайта:

```
index.html
hidden.html
index/about.html
index/contact.html
```


Фаил данных (data.yaml):
------------------------

```yaml
about:
  subtitle: О нас из YAML
  text: |
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Fusce pretium, purus sed faucibus porttitor,
    nulla felis ultrices est, at ornare diam magna quis lacus.
contact:
  subtitle: Контакты из YAML
  text: >
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Fusce pretium, purus sed faucibus porttitor.
```

Дополнения (plugins)
--------------------

* Wait