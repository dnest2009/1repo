# #   #функція фільтрації

# # ages = [5, 12, 17, 18, 24, 32]

# # def myFunc(x):
# #   if x < 18:
# #     return False
# #   else:
# #     return True

# # adults = filter(myFunc, ages)

# # for x in adults:
# #   #print(x)

# # #функція map
# # def myfunc(a):
# #   return len(a)

# # x = map(myfunc, ('apple', 'banana', 'cherry'))

# # #print(x)

# # #convert the map into a list, for readability:
# # print(list(x))

# # #range
# # x = range(6)
# # for n in x:
# #   #print(n)

# # #reversed
# # alph = ["a", "b", "c", "d"]
# # ralph = reversed(alph)
# # for x in ralph:
# #   #print(x)

# # def factorial(n):
# #     if n == 0: # базовий випадок
# #         return 1
# #     else:
# #         return n * factorial(n-1) # рекурсивний випадок

# # #print(factorial(32)) # виведе 120

# # #def factorial(n):
# #     print("Виклик функції factorial з n = ", n)
# #     if n == 1:
# #         print("Базовий випадок, n = 1, повернення 1")
# #         return 1
# #     else:
# #         result = n * factorial(n-1)
# #         print("Повернення результату для n = ", n, ": ", result)
# #         return result

# # #print(factorial(5))

# # num = int(input("Enter a number: "))

# # if num > 0:
# #     if num % 2 != 0:
# #         result = "Positive odd number"
# #     elif num % 2 = 0:
# #         result = "Positive even number"
# # elif num < 0:
# #     result = "Negative number"  
# # else:
# #     result = "It is zero"

# # def discount_price(price, discount:float):
# #     def apply_discount():
# #         nonlocal price
# #         return price*(1-discount)
# #     return apply_discount()
# # print (f"{discount_price(100,0.2)} ваша ціна")

# # def format_string(string:str, length:int):
# #     if len(string)>=length:
# #         return string
# #     else:
# #         string=" " * ((length - len(string))//2) + string
# #         return string
# # print (f"{format_string("cod",15)}")
    
# # def first(size,*args):
# #     list=[*args]
# #     return size+len(list)
# # def second(size,**kwargs):
# #     dict=[*kwargs]
# #     return size+len(dict)

# # print(first(10,2,4,5,7,8))
# # print(second(152,a="2",b="2",ddd=21,hhhhh="111"))

# import datetime
# # now = datetime.datetime.now()
# # print(now)

# from datetime import datetime

# # current_datetime = datetime.now()

# # print(current_datetime.year)
# # print(current_datetime.month)
# # print(current_datetime.day)
# # print(current_datetime.hour)
# # print(current_datetime.minute)
# # print(current_datetime.second)
# # print(current_datetime.microsecond)
# # print(current_datetime.tzinfo)

# import datetime

# # Створення об'єктів date і time
# # date_part = datetime.date(2023, 12, 14)
# # time_part = datetime.time(12, 30, 15)

# # Комбінування дати і часу в один об'єкт datetime
# # combined_datetime = datetime.datetime.combine(date_part, time_part)

# # print(combined_datetime)  # Виведе "2023-12-14 12:30:15"


# # Створення об'єкта datetime з конкретною датою
# # specific_date = datetime.datetime(year=2020, month=1, day=7)

# # print(specific_date)  # Виведе "2020-01-07 00:00:00"

# # from datetime import datetime

# # Створення об'єкта datetime
# # now = datetime.now()

# # # Отримання номера дня тижня
# # day_of_week = now.weekday()

# # # Поверне число від 0 (понеділок) до 6 (неділя)
# # print(f"Сьогодні: {day_of_week}")  
# # from datetime import datetime

# # # Створення об'єкта datetime
# # now = datetime.now()

# # # Отримання ISO календаря
# # iso_calendar = now.isocalendar()

# # print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")
# # from datetime import datetime, timezone, timedelta

# # utc_time = datetime.now(timezone.utc)

# # # Створення часової зони для Східного часового поясу (UTC-5)
# # eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# # # Перетворює час UTC в час Східного часового поясу
# # print(eastern_time)  

# # import time

# # current_time = time.time()
# # print(f"Поточний час: {current_time}")

# # import time
# # import datetime
# # now = datetime.datetime.now()
# # current_time = time.time()
# # current_datetime = datetime.now()
# # a= current_datetime.hour
# # b= current_datetime.minute
# # # print(f"Поточний час: {current_time}")

# # readable_time = time.ctime(current_time)
# # # print(f"Читабельний час: {readable_time}")

# # import time
# # from datetime import datetime

# # current_datetime = datetime.now()

# # # print(current_datetime.year)
# # # print(current_datetime.month)
# # # print(current_datetime.day)
# # # print(current_datetime.hour)
# # # print(current_datetime.minute)
# # # print(current_datetime.second)
# # # print(current_datetime.microsecond)
# # # print(current_datetime.tzinfo)
# # import random
# # start_time = time.perf_counter()
# # for _ in range(10):
# #   x= random.randint(1, 10)
# #   cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]
# #   random.shuffle(cards)
# #   #print(cards)
# #   weights = [10, 9, 8,2,1,1,1,1,1]
# #   chosen_card = random.choices(cards, weights, k=2)
# #   chosen_card2= random.sample(cards, 2)
# #   time.sleep(0)
  
# # print(f"{current_datetime.hour}:{current_datetime.minute}:{current_datetime.second} число:{x} колода: {cards} карта1 {chosen_card} карта2 {chosen_card2}")
# # time.sleep(0.1)
# # end_time = time.perf_counter()
# # execution_time = end_time - start_time
# # print(f"Час виконання: {execution_time} секунд")

# # url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
# # _, query = url_search.split('?')
# # print(query)

# # obj_query = {}
# # for el in query.split('&'):
# #     key, value = el.split('=')
# #     obj_query.update({key: value.replace('+', ' ')})
# # print(obj_query)


# # trantab = str.maketrans("x", "9", "n")

# # str = "This is string example"
# # print(str.translate(trantab))
# # import time
# # symbols = "0123456789ABCDEF"
# # code = [
# #         '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
# #         '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
# #         ]

# # MAP = {}

# # for s, c in zip(symbols, code):
# #     MAP[ord(s)] = c
# #     MAP[ord(s.lower())] = c

# # result = "ABBA".translate(MAP)
# # print(result)
# # time.sleep(0.1)
# # morze_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
# #               'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
# #               'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
# #               'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
# #               'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
# #               '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
# #               '8': '---..', '9': '----.'}

# # Перетворення ключів словника на Unicode коди
# # table_morze_dict = {}
# # for k, v in morze_dict.items():
# #     table_morze_dict[ord(k)] = v

# # string = "Hello world it\"s me"

# # result = ""

# # for ch in string:
# #     result = result + ch.upper().translate(table_morze_dict)

# # print(result)
# # time.sleep(0.2)
# # for i in range(8):
# #     s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
# #     print(s)
# # time.sleep(0.2)
# # #width = 0.1
# # for num in range(24,30):
# #     print(f'{num} {num**2:^1} {num**5:^1}')

# # import re

# # text = "Python example@example.com. ff@gmail.com \n FFF rgjrjjijglij@hu.ii"
# # pattern = r"\w+@\w+\.\w+"
# # #pattern = r"(\w+)@(\w+\.\w+)"
# # match = re.search(pattern, text)
# # match = re.findall(pattern, text)
# # print(match)

# # # #if match:
# # #     print("Знайдено:", match.group(1))
# # #     print("Знайдено:", match.group(2))
# # #     #print(match.string)
# # #     #print (match.span())
# # # #else:
# # #     print("Не знайдено.")

# from datetime import datetime, date

# def string_to_date(date_string):
#     return datetime.strptime(date_string, "%Y.%m.%d").date()

# def date_to_string(date):
#     return date.strftime("%Y.%m.%d")

# def prepare_user_list(user_data):
#     prepared_list = []
#     for user in user_data:
#         prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
#     return prepared_list

# def get_upcoming_birthdays(users, days):
#     upcoming_birthdays = []
#     today = date.today()
#     for user in users:
#         birthday_this_year = user.get("birthday").replace(year=today.year)
#         if 0 <= ( birthday_this_year - today).days < days:
#             upcoming_birthdays.append({"name": user["name"], "congratulation_date": date_to_string( birthday_this_year)})
#     return upcoming_birthdays

# users = [
#     {"name": "Sarah Lee", "birthday": "1957.03.30"},
#     {"name": "John Doe", "birthday": "1985.03.28"},
#     {"name": "Jane Smith", "birthday": "1990.03.27"},
#     {"name": "John Doe", "birthday": "1985.01.23"},
# ]
# prepare_user_list(users)
# get_upcoming_birthdays = get_upcoming_birthdays(prepare_user_list(users),70)
# print (get_upcoming_birthdays)





users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "Sarah Lee", "birthday": "1957.3.23"},
    {"name": "Jonny Lee", "birthday": "1958.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}]
from datetime import datetime, date, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    for user in prepare_user_list(users):
        birthday_this_year = user["birthday"].replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            if 0 <= (birthday_this_year - today).days <= days: 
                congratulation_date_str = date_to_string(adjust_for_weekend(birthday_this_year))
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
        else:
            if 0 <= (birthday_this_year - today).days <= days: 
                congratulation_date_str = date_to_string(adjust_for_weekend(birthday_this_year))
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
    return upcoming_birthdays

get_upcoming_birthdays = get_upcoming_birthdays(users,7)
print (get_upcoming_birthdays)