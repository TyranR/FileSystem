from pprint import pprint

def create_recipe_dic():
    """
    Создание словаря рецептов
    :return: возвращаем созданный словарь
    """
    cook_book = {}
    with open('recipes.txt', encoding='utf8') as f:
        for line in f:
            recipe_name = line.strip()
            recipe_list = []
            ingridient_count = int(f.readline().strip())
            while ingridient_count:
                ingridient_line = f.readline().strip()
                ingridient_list = ingridient_line.split('|')
                ingridient_name = ingridient_list[0].rstrip()
                quantity = int(ingridient_list[1])
                measure = ingridient_list[2].lstrip()
                ingridient_dic = {'ingridient_name':ingridient_name, 'quantity':quantity, 'measure':measure}
                recipe_list.append(ingridient_dic)
                cook_book[recipe_name] = recipe_list
                ingridient_count -= 1
            f.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    """
    Функция, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
    """
    final_dict = {}
    for recipe in dishes:
        for ingridients in cook_book[recipe]:
            test_ingridient = ingridients['ingridient_name']
            if final_dict.get(test_ingridient):
                print(f"{test_ingridient} уже есть")
                new_quantity = final_dict[test_ingridient]['quantity']
                new_quantity += ingridients['quantity'] * person_count
                final_dict[ingridients['ingridient_name']] = {'measure': ingridients['measure'], \
                                                              'quantity': new_quantity}
            else:
                final_dict[ingridients['ingridient_name']] = {'measure':ingridients['measure'], \
                                                              'quantity':ingridients['quantity'] * person_count}
    return final_dict



def guest_coming(cook_book):
    """
    Ввод от пользователя списка блюд и кол-во персон
    """
    dishes = []
    person_count = int(input("Введите кол-во персон: "))
    for recipe in cook_book:
        dishes.append(recipe)
    # Список блюд на выбор гостей решил не давать, основной принцип как раньше, пусть едят всё)
    # Тут если что его можно передать руками
    return dishes, person_count

cook_book = create_recipe_dic()
dishes, person_count = guest_coming(cook_book)
final_dict = get_shop_list_by_dishes(dishes, person_count)
pprint(final_dict)
