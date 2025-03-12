import json
from faker import Faker, Factory

fake = Factory.create('uk_UA')
users = []

def create_users(fake,users:list, n=10):
    for _ in range(n):
        user = {}
        user['name'] = fake.name()
        user['phone_number'] = fake.phone_number()
        user['email'] = fake.email()
        user['address'] = fake.address()
        user['birthday'] = fake.date()
        users.append(user)
    to_json(users)


def to_json(users):
    with open ('users.json', 'w', encoding='utf-8') as file:
        json.dump(users, file,indent=4, ensure_ascii=False)
        print('Users were saved.')



if __name__ == '__main__':
    create_users(fake, users, n=10)