def read_ingredient_list(file, count):
    ingredient_list = []
    for i in range(0, count):
        ingredient = file.readline().strip().split(' | ')
        cookbook_dict = {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]}
        ingredient_list.append(cookbook_dict)
    return ingredient_list


def read_cookbook(filename):
    with open(filename, encoding='utf8') as cookbook_file:
        cookbook = {}
        dish_title = cookbook_file.readline().strip()
        while dish_title:
            ingredient_count = int(cookbook_file.readline().strip())
            ingredient_list = read_ingredient_list(cookbook_file, ingredient_count)
            cookbook[dish_title] = ingredient_list
            cookbook_file.readline()
            dish_title = cookbook_file.readline().strip()

        return cookbook


def get_shop_list_by_dishes(dishes, person_count):
    cookbook = read_cookbook('cookbook.txt')
    shop_list = {}
    for dish in dishes:
        if dish in cookbook:
            for ingredient in cookbook[dish]:
                if not ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                'quantity': ingredient['quantity'] * person_count}
                else:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return shop_list


print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
