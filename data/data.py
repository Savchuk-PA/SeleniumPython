from enum import Enum


class MainPageData:
    CATALOG_LINK_NAME = ['Электроника', 'Бытовая техника', 'Одежда', 'Обувь', 'Аксессуары', 'Красота', 'Здоровье',
                         'Товары для дома', 'Строительство и ремонт', 'Автотовары', 'Детские товары',
                         'Хобби и творчество', 'Товары для взрослых', 'Спорт и отдых', 'Продукты питания',
                         'Бытовая химия и личная гигиена', 'Канцтовары', 'Зоотовары', 'Книги', 'Дача, сад и огород']

    DICT_CATALOG_LINK_URL = {'Электроника': 'https://kazanexpress.ru/category/Elektronika-10020',
                            'Бытовая техника': 'https://kazanexpress.ru/category/Bytovaya-tekhnika-10004',
                            'Одежда': 'https://kazanexpress.ru/category/Odezhda-10014',
                            'Обувь': 'https://kazanexpress.ru/category/Obuv-10013',
                            'Аксессуары': 'https://kazanexpress.ru/category/Aksessuary-10003',
                            'Красота': 'https://kazanexpress.ru/category/Krasota-10012',
                            'Здоровье': 'https://kazanexpress.ru/category/Zdorove-10009',
                            'Товары для дома': 'https://kazanexpress.ru/category/Tovary-dlya-doma-10018',
                            'Строительство и ремонт': 'https://kazanexpress.ru/category/Stroitelstvo-i-remont-10016',
                            'Автотовары': 'https://kazanexpress.ru/category/Avtotovary-10002',
                            'Детские товары': 'https://kazanexpress.ru/category/Detskie-tovary-10007',
                             'Хобби и творчество': 'https://kazanexpress.ru/category/Khobbi-i-tvorchestvo-10008',
                             'Товары для взрослых': 'https://kazanexpress.ru/category/Tovary-dlya-vzroslykh-10017',
                             'Спорт и отдых': 'https://kazanexpress.ru/category/Sport-i-otdykh-10015',
                             'Продукты питания': 'https://kazanexpress.ru/category/Produkty-pitaniya-1821',
                             'Бытовая химия и личная гигиена': 'https://kazanexpress.ru/category/Bytovaya-khimiya-i-lichnaya-10005',
                             'Канцтовары': 'https://kazanexpress.ru/category/Kanctovary-10010',
                             'Зоотовары': 'https://kazanexpress.ru/category/Zootovary-10019',
                             'Книги': 'https://kazanexpress.ru/category/Knigi-10011',
                             'Дача, сад и огород': 'https://kazanexpress.ru/category/Dacha-sad-i-ogorod-10006'}

    DICT_CATALOG_LINK_POSITION_NUMBER = {'Электроника': 0,
                                         'Бытовая техника': 1,
                                         'Одежда': 2,
                                         'Обувь': 3,
                                         'Аксессуары': 4,
                                         'Красота': 5,
                                         'Здоровье': 6,
                                         'Товары для дома': 7,
                                         'Строительство и ремонт': 8,
                                         'Автотовары': 9,
                                         'Детские товары': 10,
                                         'Хобби и творчество': 11,
                                         'Товары для взрослых': 12,
                                         'Спорт и отдых': 13,
                                         'Продукты питания': 14,
                                         'Бытовая химия и личная гигиена': 15,
                                         'Канцтовары': 16,
                                         'Зоотовары': 17,
                                         'Книги': 18,
                                         'Дача, сад и огород': 19}

    CATALOG_COUNT_LINK = 20


class SearchData:
    MANUFACTURERS_NAME = ["Samsung", "Xiaomi", "iPhone"]


class Error:
    text_elements_wrong = "The wrong name in the list"
    search_element_wrong_title = "The element does not contain a substring"
    count_element_wrong = "Wrong count element in list Web elements"
    element_not_visible = "element not is displayed"

