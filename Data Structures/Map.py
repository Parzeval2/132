#map

values = [5,6,7,8]

def double(x: int | float) -> int | float:
    return x * 2

twice = list(map(double, values))
print(twice)

people_list = [
    ['Josh','Pizza'],
    ['Jane','Chicken'],
    ['jill','salad']
]

def list_to_dictionary(item: list):
    return {'name': item[0], 'favorite_food': item[1]}

people_dict = list(map(list_to_dictionary, people_list))
print(people_dict)

from dataclasses import dataclass
class Person:
    name: str
    favorite_food: str

people = map(lambda item: Person(item[0], item[1]), people_list)
print(list(people))