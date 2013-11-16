
Дополнения
==========

Меню (buildmenu)
----------------------

Посмтроения меню в объект env.menu

Необходимые элементы в стректуре (structure.json):

* name - имя в пункте меню (если нет то пункта меню не будет)
* navigation - видимость элемента в навигации (True/False)



Навигационные цепочки (breadcrumbs)
----------------------------------

Добавляет в структуру объект structure.item.breadrcumbs.
Массив элементов: [{ "name": <name>, "link": <link> }]



Вид/Деталь (viewdetail)
-----------------------

Формирует подэлементы в меню для формирования view/detail элементов из объекта:
"data": "data.json"

(требуется наличие subitem_template для указания шаблона детального вида)

Добавит в структуру:
structure.item.object_list - список элементов
structure.item.subitem_1 - подэлемент 1
structure.item.subitem_2 - подэлемент 2
...
structure.item.subitem_N - подэлемент 3


пример структуры:

```json
{
    "detail":{
        ...
        "data": "data.json",
        "template": "data_list.html",
        "detail_template": "data_detail.html",
        ...
    }
}
```


Минимизатор изображений (thumbnails)
-----------------------

Ищет и приводит изображение к нужному формату
Формат: из "image.jpg" в "image_H_W.jpg"

```json
{
    "item":{
        "image_field_1": "image_1.jpg",
        "image_field_2": "image_2.jpg",
        "thumbnails": [
            {
                "field": "image_field_1",
                "width": 100,
                "height": 80
            },
            {
                "field": "image_field_2",
                "width": 150,
                "height": 110
            }
        ]
    }
}
```