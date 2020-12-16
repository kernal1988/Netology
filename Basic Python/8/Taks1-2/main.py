from pprint import pprint
with open('recipes.txt', encoding='utf-8') as f:
  cook_book = {}
  ingredients_dict = {}
  while True:
    ingredient_list = []
    food = f.readline().strip()
    if not food:
      break
    for i in range(int(f.readline().strip())):
      ingredient = f.readline().strip().split('|')
      ingredient_list.append({'ingridient_name':ingredient[0],'quantity':ingredient[1],'measure':ingredient[2]})
    f.readline().strip()
    cook_book[food] = ingredient_list
print(" Задание 1 ")
pprint(cook_book)

def get_shop_list_by_dishes (dishes, person_count):
  all_ingridients_dict = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      ingridients_dict = {}
      one_ingridient = ingridient['ingridient_name']
      ingridients_dict['measure'] = ingridient['measure']
      ingridients_dict['quantity'] = int(ingridient['quantity']) * person_count
      all_ingridients_dict[one_ingridient] = ingridients_dict
  pprint(all_ingridients_dict)
print(" Задание 2 ")
get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)