
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
        "navigation": True,
        "title": "My First Static Site",
        "subtitle": "Главная",
        "subitems": {
            "about": {
                "template": "about.html",
                "name": "Главная",
                "navigation": True,
                "subtitle": "О нас",
                "include": "data.json about",
                "include_format": "json"
            },
            "contact": {
                "template": "contact.html",
                "subtitle": "Контактная информация",
                "name": "Главная",
                "navigation": True
            }
        },
        "hidden": {
                "template": "hidden.html",
                "subtitle": "Скрытая страница",
                "name": "Скрытая",
                "navigation": False
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


Фаил данных (data.json):
---------------------------------------

```json
{
    "about":{
        "title": "About",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce pretium, purus sed faucibus porttitor,
                 nulla felis ultrices est, at ornare diam magna quis lacus.
                 Phasellus vitae vehicula tellus. Nunc blandit lorem porttitor, consectetur odio in, suscipit elit.
                 Aenean id urna facilisis, ullamcorper nibh nec, dapibus lacus. Sed ut lacus in sem gravida laoreet.
                 Proin justo erat, tincidunt vitae purus vitae, tempus adipiscing ipsum. Etiam mattis urna eu est
                 facilisis tempor. Praesent tristique nisl at dignissim condimentum. Praesent dictum suscipit dignissim.
                 Mauris fringilla nulla felis, nec dictum arcu hendrerit in. Integer malesuada placerat ante, et
                 pulvinar ligula molestie in. Ut lacus diam, aliquet id ante vel, sollicitudin scelerisque tortor.
                 Aenean mi turpis, vulputate id aliquet at, malesuada a justo. Aenean sem lacus, vulputate non enim
                 eget, porta congue odio. Sed ullamcorper neque eu vestibulum volutpat."
    },
    "contact":{
        "title": "Contact",
        "text": "Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
                 Nam velit libero, congue vel augue vitae, tincidunt dapibus nunc. Ut molestie neque at nisl
                 vestibulum rutrum et sed dui. Integer luctus est non blandit volutpat. Nam eu blandit sem.
                 Nullam quis feugiat augue. Fusce a dictum lectus. Fusce iaculis a ipsum eget vulputate. Sed
                 consectetur nisl dapibus, bibendum est eu, lobortis diam. Etiam viverra sem nec lacus molestie
                 eleifend. Vivamus nibh quam, iaculis nec blandit et, sollicitudin sed felis. In eu felis vestibulum,
                 pretium sapien ut, convallis arcu."

    }
}
```