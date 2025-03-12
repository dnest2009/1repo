from csv import DictWriter
import json


file_json = 'users.json'
file_csv = 'users.csv'

def get_users():
     with open(file_json, 'r', encoding='utf-8') as reader:
          users = json.load(reader)
          return users
     
def write_table():
     users = get_users()
     with open(file_csv, 'w', encoding='utf-8', newline='') as file:
          fieldsnames=users[0].keys()
          writer = DictWriter(file, delimiter=';', fieldnames=fieldsnames)
          writer.writeheader()
          for row in users:
               writer.writerow(rowdict=row)
          print('csv was created')

if __name__ == '__main__':
     write_table()