from test import Item

from collections import UserDict

class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data:
            if self.data[key] == value:
                keys.append(key)
        return keys
    

d = LookUpKeyDict()
d['a']= 1
d['b'] = 2
d['cf'] = 109


class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if not employee_id.startswith('01'):
        raise IDException
    else:
        id_list.append(employee_id)
    return id_list


class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append({"id": Contacts.current_id,"name": name, "phone":phone, "email":email,"favorite": favorite})
        #self.contacts.append()
        Contacts.current_id += 1
        return self.contacts

lust = Contacts()
x = {'name': 'Wylie Pope', 'phone': '(692) 802-2949', 'email': 'est@utquamvel.net', 'favorite': True}
y = {'name': 'Cyrus Jackson', 'phone': '(501) 472-5218', 'email': 'nibh@semsempererat.com', 'favorite': False}
print(lust.add_contacts(1,2,3,True))

