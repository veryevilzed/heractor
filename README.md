
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
        "root": "file:///Users/name/src/heract/example/out/",
        "out": "out/",
        "templates": "templates/",
        "static_root": "static/",
        "structure": "../example/structure.json",
        "global": {
            "static": "file:///Users/name/src/heract/example/static/",
            "root": "file:///Users/name/src/heract/example/out/",
            "title": "Supper Static Site"
        },
        "plugins": [
            "plugins.buildmenu.build",
            "plugins.structure.build",
            "plugins.breadcrumbs.build",
            "plugins.include.build",
            "plugins.markdn.build"
        ]
    }
}
```

main, production, debug - секции файла включаются при сборке выбором --section=main

Параметры:

* global - набор глобальных констант, будет доступен в каждом шаблоне, можно вынести пути к статике, заголовки и т.п.
* base - берет настройки из другой секции и дополняет/перекрывает своими (не реализовано)
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
        "slug": "index_page",
        "name": "Главная",
        "navigation": false,
        "title": "My First Static Site",
        "subtitle": "Главная",
        "folder": "sub",
        "subitems": {
            "about": {
                "template": "about.html",
                "name": "О Нас",
                "navigation": true,
                "subtitle": "О нас",
                "include": "data.yaml #about",
                "include_format": "yaml"
            },
            "contact": {
                "template": "about.html",
                "subtitle": "Контактная информация",
                "name": "Контакты",
                "navigation": true,
                "include": "data.yaml #contact",
                "include_format": "yaml"
            }
        }
    },
    "hidden": {
        "template": "about.html",
        "subtitle": "Скрытая страница",
        "name": "Скрытая",
        "navigation": false,
        "include": "../README.md",
        "include_format": "text",
        "markdown": ["include"]
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
* folder - имя каталога для subitems ( по умолчанию берется key )
* include - загружает данные из файла
* include_format - формат данных
* markdown - поля на которые нужно наложить markdown


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

см. /heractor/plugins