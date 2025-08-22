from typing import TypedDict
class Animal(TypedDict):
    name:str
    type:str
    age:int

#ew_animal : Animal = {'name': 'Leo', 'type': 'Lion', 'age': 5}
# new_animal : Animal = {'name': 'Leo', 'type': 'Lion'}
new_animal : Animal = {'name': 'Leo', 'type': 'Lion', 'age': 5.4}
print(new_animal)