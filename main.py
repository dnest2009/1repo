# print("Hello World")
# print('hello git')
# class Parent:
#   def __init__(self, txt):
#     self.message = txt

#   def printmessage(self):
#     print(self.message)

# class Child(Parent):
#   def __init__(self, txt):
#     super().__init__(txt)

# x = Child("Hello, and welcome!")

# x.printmessage()

import time
from datetime import date
today = date.today()
print(today)
today = today.replace(year=today.year + 1)
print(today)