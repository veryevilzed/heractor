

Дополнения
==========


Build Menu (buildmenu)
----------------------

Посмтроения меню в объект env.menu

Необходимые элементы в стректуре (structure.json):

* name - имя в пункте меню (если нет то пункта меню не будет)
* navigation - видимость элемента в навигации (True/False)


Навигационные цепочки (breadcumbs)
----------------------------------

Добавляет в структуру объект structure.item.breadcumbs.
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
        "detail_template": "data_detail.html"
        ...
    }
}
```


