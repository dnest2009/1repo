# """Завжди, коли потрібно зберегти інформацію для подальшого використання в зрозумілій комп'ютеру формі, робимо серіалізацію.
#  Найочевидніший приклад — це збереження даних у текстовий файл. Ти можеш зберегти, наприклад, перелік витрат у текстовий файл:"""
# expenses = {"hotel": 150, "breakfast": 30, "taxi": 15, "lunch": 20}
# file_name = "expenses.txt"
# with open(file_name, "w") as fh:
#     for key, value in expenses.items():
#         fh.write(f"{key}|{value}\n")

# """Якщо потім знадобиться завантажити цей перелік назад у Python, завжди є змога це зробити:"""
# file_name = "expenses.txt"
# expenses = {}
# with open(file_name, "r") as fh:
#     raw_expenses = fh.readlines()
#     for line in raw_expenses:
#         key, value = line.split("|")
#         expenses[key] = int(value)
# print(expenses)
# """Python надає декілька модулів для серіалізації, найпопулярнішими з яких є pickle і json.
# вбудований пакет pickle дозволяє працювати з вбудованими типами (словники, списки, кортежі, рядки, множини та ін.) і навіть з нескладними класами;
# формат JSON підтримується Python і з невеликими обмеженнями дозволяє працювати з рядками, числами, списками, кортежами та словниками.
# Обидва ці методи мають свої переваги та обмеження. Pickle має високу гнучкість і дозволяє серіалізувати складні об'єкти, але може бути небезпечним 
# при десеріалізації даних зі сторонніх джерел. JSON є більш обмеженим у типах даних, які можуть бути серіалізовані, але забезпечує кращу 
# багатоплатформову сумісність і безпеку.

# Упакування у byte-рядки та розпакування із byte-рядків
# Метод dumps запаковує в byte-рядок об'єкт, а метод loads потім розпаковує назад з byte-рядка в об'єкт. Ці методи потрібні, 
# коли ми хочемо контролювати, що робити з byte представленням, наприклад, відправити його мережею або прийняти з мережі."""
# import pickle

# # Об'єкт для серіалізації
# my_data = {"key": "value", "num": 42}

# # Серіалізація об'єкта в байтовий рядок
# serialized_data = pickle.dumps(my_data)
# # Виведе байтовий рядок
# print(serialized_data)  

# # Десеріалізація об'єкта з байтового рядка
# deserialized_data = pickle.loads(serialized_data)
# # Виведе вихідний об'єкт Python
# print(deserialized_data)

# """Упакування у файл та розпакування з файлу"""
# # Об'єкт для серіалізації
# my_data = {"key": "value", "num": 100}
# # Серіалізація об'єкта в файл
# with open("data.pickle", "wb") as file:
#     pickle.dump(my_data, file)

# # Десеріалізація об'єкта з файлу
# with open('data.pickle', 'rb') as file:
#     deserialized_data = pickle.load(file)
# # Виведе вихідний об'єкт Python
# print(deserialized_data)

# """Робота з класами користувача
# Ви можете зберігати об'єкти для подальшого використання, але є важлива умова. Самі класи та функції pickle зберігати не вміє і, якщо вам потрібно
# розпакувати упакований об'єкт класу, то сам клас повинен бути оголошений раніше у коді.
# """
# class Human:
#     def __init__(self, name):
#         self.name = name

# bob = Human("Bob")
# with open("instance.pickle", "wb") as file:
#     pickle.dump(bob, file)


# class Human:   # Важливо, щоб клас Human був визначений у скрипті, який виконує десеріалізацію, із тією ж структурою та в тому ж просторі імен, що й у скрипті, який виконав серіалізацію."""
#     def __init__(self, name):
#         self.name = name

# with open("instance.pickle", "rb") as file:
#     loaded_instance = pickle.load(file)

# print(loaded_instance.name)

# """JSON
# Серіалізація (або "запис") перетворює об'єкти Python у рядок у форматі JSON. Це виконується за допомогою методу json.dumps() для перетворення об'єктів
#  у рядок JSON.
# Метод dumps запаковує в byte-рядок об'єкт, loads розпаковує (десеріалізує) з byte-рядка в об'єкт. Ці методи потрібні, коли ми хочемо контролювати, 
# що робити з byte представленням, наприклад, відправити його мережею або прийняти з мережі."""
# import json

# # Python об'єкт (словник)
# data = {'name': "Дмитро Нестеренко", "age": 30, "isStudent": True}

# # Серіалізація у файл
# with open("data.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)

# # Десеріалізація з файлу
# with open("data.json", "r", encoding="utf-8") as f:
#     data_from_file = json.load(f)
#     print(data_from_file)

# json_string = json.dumps(data)
# print(json_string)
# unpacked_some_data = json.loads(json_string)
# print(unpacked_some_data)

# """Для читання даних з CSV файлу можна використовувати функцію csv.reader, що повертає об'єкт, який ітерує по рядках файлу."""
# import csv
# # Дані для запису
# rows = [
#     ["name", "age", "specialty"],
#     ["Василь Гупало", 30, "Математика"],
#     ["Марія Петренко", 22, "Фізика"],
#     ["Олександр Коваленко", 20, "Інформатика"],
# ]
# # Відкриваємо файл для запису
# with open("data.csv", "w", newline="", encoding="utf-8") as csvfile:
#     # Створюємо об'єкт writer
#     writer = csv.writer(csvfile, delimiter=",")
#     # Записуємо рядки даних За допомогою writer.writerows(rows) можна записати кілька рядків одразу. Якщо потрібно записати один рядок, можна використати writer.writerow(row).
#     writer.writerows(rows)


# # Відкриваємо CSV файл
# with open("data.csv", newline="", encoding="utf-8") as csvfile:
#     # Створюємо об'єкт reader
#     reader = csv.reader(csvfile, delimiter=",")
#     # Проходимося по кожному рядку у файлі
#     for row in reader:
#         print("|".join(row))

# """Модуль csv також надає класи csv.DictReader і csv.DictWriter, які дозволяють працювати з рядками як зі словниками. Це зручно, коли у файлі CSV є заголовки стовпців."""
# # Запис у CSV файл зі словників
# with open("students.csv", "w", newline="", encoding="utf-8") as csvfile:
#     fieldnames = ["name", "age", "specialty"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({"name": "Олег Олегов", "age": 23, "specialty": "Історія"})
#     writer.writerow({"name": "Анна Сергіївна", "age": 22, "specialty": "Біологія"})

# # Читання з CSV файлу в словники
# with open("students.csv", newline="", encoding="utf-8") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row["name"], row["age"], row["specialty"])

# my_list = [1, 2, 3]

# def square_list(x: list):
#     for i, el in enumerate(x):
#         x[i] = el**2
#     return x

# new_list = square_list(my_list)
# print(new_list)
# print(my_list)

# my_list = [1, 2, 3]

# def square_list(x: list):
#     return [el**2 for el in x]

# new_list = square_list(my_list)
# print(new_list)
# print(my_list)

# """Коли викликається pickle.dump() або pickle.dumps() для серіалізації об'єкта, Python шукає метод __getstate__ у класі об'єкта. Якщо метод існує, він використовується для 
# отримання стану об'єкта для серіалізації. При десеріалізації, за допомогою pickle.load() або pickle.loads(), Python шукає метод __setstate__ у класі. Якщо метод існує, він 
# використовується для відновлення стану об'єкта з даних, отриманих під час десеріалізації."""
# class Robot:
#     def __init__(self, name, battery_life):
#         self.name = name
#         self.battery_life = battery_life
#         # Цей атрибут ми не збираємось серіалізувати
#         self.is_active = False  

#     def __getstate__(self):
#         state = self.__dict__
#         # Видаляємо is_active з серіалізованого стану
#         del state['is_active']
#         return state

#     def __setstate__(self, state):
#         # Відновлюємо об'єкт при десеріалізації
#         self.__dict__.update(state)
#         # Задаємо значення is_active за замовчуванням
#         self.is_active = False  

# # Створення об'єкта Robot
# robot = Robot("Robo1", 100)

# # Серіалізація об'єкта
# serialized_robot = pickle.dumps(robot)

# # Десеріалізація об'єкта
# deserialized_robot = pickle.loads(serialized_robot)

# print(deserialized_robot.__dict__)


# """Створення глибоких копій об'єктів Python"""

# import copy

# class MyClass:
#     def __init__(self, value):
#         self.value = value

#     def __copy__(self):
#         print("Викликано __copy__")
#         return MyClass(self.value)

#     def __deepcopy__(self, memo=None):
#         print("Викликано __deepcopy__")
#         return MyClass(copy.deepcopy(self.value, memo))

# # Поверхневе копіювання
# obj = MyClass(5)
# obj_copy = copy.copy(obj)
# obj_copy.value = 10

# # Глибоке копіювання
# obj_deepcopy = copy.deepcopy(obj)
# obj_deepcopy.value = 20
# print(obj.value, obj_copy.value, obj_deepcopy.value)


# class UserSettings:
#     def __init__(self, preferences, large_data_reference):
#         self.preferences = preferences
#         self.large_data_reference = large_data_reference

#     def __deepcopy__(self, memo):
#         print("Кастомізоване глибоке копіювання для UserSettings")
#         # Припустимо, що preferences - це невеликий словник, який можна безпечно скопіювати,
#         # а large_data_reference - це посилання на великий об'єкт даних, яке ми не хочемо дублювати.
#         new_preferences = copy.deepcopy(self.preferences, memo)
#         # Передаємо посилання на ті ж великі дані замість їх копіювання
#         new_obj = UserSettings(new_preferences, self.large_data_reference)
#         return new_obj

# # Створення екземпляра UserSettings
# original_settings = UserSettings({"language": "uk"}, large_data_reference="LargeDataID")

# # Глибоке копіювання з кастомізованою логікою
# settings_copy = copy.deepcopy(original_settings)


import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0
        self.is_unpacking = False
        

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

    def __setstate__(self, state):
        state['is_unpacking'] = True
        self.__dict__.update(state)
        
        
            
        
contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]
persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()

print(persons.count_save)  # 0
print(first.count_save)  # 1
print(second.count_save)  # 2
print(third.count_save)  # 3
