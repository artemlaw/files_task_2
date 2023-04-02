def main_run():
    cook_book = {
        'Омлет': [
            {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
            {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
            {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        ],
        'Утка по-пекински': [
            {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
            {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
            {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
            {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
        ],
        'Запеченный картофель': [
            {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
            {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
            {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}
        ],
        'Фахитос': [
            {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
            {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
            {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
            {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
            {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
        ]
    }

    def get_shop_list_by_dishes(dishes, person_count):
        shop_list_by_dishes = {}
        ingredients = []
        for dish in dishes:
            ingredients += cook_book[dish]

        for ingredient in ingredients:
            if ingredient['ingredient_name'] in shop_list_by_dishes:
                shop_list_by_dishes[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list_by_dishes[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                }
        return shop_list_by_dishes

    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


if __name__ == '__main__':
    main_run()
