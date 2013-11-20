
HERACTOR v.1.0
==============

Установка
---------

Простой путь:

```
pip install heractor
```

Исполняемый модуль:
-------------------

 heract --config=config.json



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
        "static_dir": "static/",
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
* static_dir - путь к статике (для копирования ее в проект)

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
====================

подключения плугинов производится в config.json секция plugins=[]
порядок имеет значения, например для markup необходимо чтоб до этого была выполнена загрузка данных при помощи include


include
-------

Загружает данные из внешних файлов в структуру

```json
{
    ...
    "page":{
        ...
        "include": "data.yaml #contact",
        "include_format": "yaml"
    }
    ...

    "page2":{
        ...
        "include": "data.txt",
        "include_format": "text"
    }

}
```

Параметры:
* include - указывает на объект вставки, для структурных форматов данных (json, yaml ...) вносит изменение прямо в объект структуры
так же можно указать элемент верхнего уровня для вставки только части текста, это позволит хранить в одном файле контент для разных страниц
* include_format - формат данных json, yaml, text
* include_url - тоже что и include только для удаленной загрузки (в разработке)


markdown
--------

Генерирует разметку HTML из структурного текста в форматах reS, md и тп

```json
{
    ...
    "page":{
        ...
         "markdown": ["include"]
    }
    ...
}
```

Параметры:
* markdown - список полей к которым нужно применить markdown


breadcrumbs
-----------

Плугин для построения "хлебного пути"

не требует настроек

создает дополнительный элемент в структуре

```json
{
    "page":{
        "breadcrumbs":[
            { "name": "page_1", "path": "/path/to/page_1.html" },
            { "name": "page_2", "path": "/path/to/page_2.html" },
            { "name": "page_3", "path": "/path/to/page_3.html" }
        ]
    }
}
```

последняя страница это текущая



structure
---------

Дополнение для построения обратных ссылок на любую страницу сайта

Параметры:
slug - уникальное имя страницы во всей структуре, не обязательный, будет браться из key

расширяет структуру global объектом pages:

```
pages.<slug>.slug
pages.<slug>.name
pages.<slug>.path

```

Пример использования в шаблоне:

```html
<a href="{{ pages.about.path }}">{{ pages.about.name }}</a>
```

buildmenu
---------

Компонент построения меню из структуры

```json
{
    "index":{
        "name":"Главная",
    },
    "content":{
        "name":"Контент",
        "folder": "cnt",
        "subitems":{
            "about":{
                "name":"О Нас"
            },
            "hidden":{
                "name":"Скрыытая",
                "navigation": false
            }

        }
    }
}
```

Параметры:
* name - имя отражающиеся в меню (если нет то title, если нет то key)
* navigateion - (true/false) показывать ли в навигации
* folder - папка для подэлементов



listviewdetail
--------------

Компонент построения подмножества элементов

```json
{
    ...
    "users": {
        "template": "user_list.html",
        "object_list_data": "objects.json",
        "object_list_item": {
            "navigation": false,
            "subtitle": "Детальный вид",
            "template": "user_detail.html"
        }
    }
    ...
}
```

Параметры:

* object_list_data - откуда брать данные для элементов
* object_list_data_format - формат данных (по умолчанию json-array)
* template - шаблон для построения данных
* object_list_item - шаблон элемента детального вида

расширение структуры корневого элемента:
object_list - список объектов

расширение структуры дочерних элементов:

```json
"parent":{
    "name": "users",
    "path": "../users.html"
}
```


Пример шаблона list

```html
<table class="table">
    <thead>
        <tr><th>#</th> <th>Name</th> <th>Age</th> <th>Email</th> <th>Company</th> <th></th> </tr>
    </thead>
    <tbody>
    {% for object in object_list %}
        <tr>
            <td>{{ object.id }}</td>
            <td>{{ object.name }}</td>
            <td>{{ object.age }}</td>
            <td>{{ object.email }}</td>
            <td>{{ object.company }}</td>
            <td><a href="{{ object.detail_path }}" class="btn">Детально</a></td>
        </tr>
    {% endfor %}
    </tbody>
</table>
```


Пример шаблоноа detail

```html

{{ id }}<br/>
{{ name }}<br/>
{{ age }}<br/>
{{ email }}<br/>
{{ company }}<br/>
<a href="{{ parent.path }}" class="btn">Назад</a>
```


thumbnail
---------

Для создания превью изображений можно использовать imagemagick

Установка:

```
apt-get install imagemagick
brew imagemagick
```

Использование:
```
convert -thumbnail 200 abc.png thumb.abc.png
convert -thumbnail x200 abc.png thumb.abc.png
```

Снип:
```bash
#!/bin/bash
FILES="$@"
for i in $FILES
do
    echo "Prcoessing image $i ..."
    /usr/bin/convert -thumbnail 200 $i thumb.$i
done
```





Скоро!
======

Дополнения:

* blog - построение listviewdetail из каталога статей
* pagination - постраничное листание для данных object_list




blog
----

Построение listviewdetail из каталога статей

```json
{

    ...
    "blog":{
        "name":"Главная",
        "blog_folder":"../blog/",
        "object_list_item": {
            "markdown":["text"]
        }
    },

```

Параметры:
* blog_folder - указывает местоположение статей блога
(расшерение файлов должно быть .txt, .md, .rst, .html, json, yaml)

Для текстовых форматов, таких как .txt, .md, .rst, .html данные попадают в объект "text" в каждом дочернем элементе,
Для структурных данных, попадают в соответствующее поле

В корневом элементе все объекты попадают в object_list

Makefile's
==========

Примеры Makefile для быстрой работы и публикации.

```Makefile

HERACT=./heractor/heract
CONFIG=./example/config.json

build:
    $(HERACT) --config=$(CONFIG) --section=main

releaase:
    $(HERACT) --config=$(CONFIG) --section=release

```

