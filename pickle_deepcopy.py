import pickle
from copy import deepcopy, copy


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        copy_obj = Person(self.name,self.email,self.phone,self.favorite)
        return copy_obj
            
            
class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        copy_obj = Contacts(self.filename, self.contacts)
        return copy_obj
        

    def __deepcopy__(self, memo):
        copy_obj = Contacts(self.filename, self.contacts)
        memo[id(copy_obj)] = copy_obj
        copy_obj.filename = deepcopy(self.filename)
        copy_obj.contacts = deepcopy(self.contacts)
        return copy_obj

'''Завдання виконано успішно! Метод save_to_file класу Contacts працює правильно
Завдання виконано успішно! Метод read_from_file класу Contacts працює правильно
Завдання виконано успішно! Методи __getstate__ і __setstate__ класу Contacts працюють правильно
Завдання виконано успішно! Методи `__copy__` і `__deepcopy__` працюють правильно'''        
        
        
        
        