from datetime import datetime
from collections import UserList
import json
"""
MessageSystem(messages)
- додати метод який буде діставати усі чати з нашої системи

При серіалізації буде проблема що кожен користувач буде окремою сутністю. 
можна до кожного користувача додати унікальний ідентифікатор
"""
MESSAGES_JSON_FILE = "messages.json"

class User:
    id = 0

    def __init__(self, first_name:str, last_name: str, phone_number: str):
        User.id += 1
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.id = User.id
    
    def to_json(self) -> dict:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,

        }

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.phone_number} {self.id}"
    
    def __repr__(self):
        return str(self)

class Message:
    def __init__(self,content:str, author: User, recepient: User):
        self.content = content
        self.author = author
        self.recepient = recepient
        self.sending_time = datetime.now()
        self.receiving_time = None

    def is_message_read (self) -> bool:
        return self.receiving_time is not None
    
    def mark_message_as_read (self):
        self.receiving_time = datetime.now()

    def to_json(self) -> dict:
        return {
            "content": self.content,
            "sending_time": str(self.sending_time),
            "receiving_time": str(self.receiving_time),
            "author": self.author.to_json(),
            "recepient": self.recepient.to_json()}
    
    def __str__(self):
        return f"Message from [{self.author}] to [{self.recepient}] | '{self.content}' {self.sending_time} \n"

    def __repr__(self):
        return str(self)
    
    def __lt__(self,other) -> bool:
        return self.sending_time < other.sending_time



class MessageSystem(UserList):
    def __init__(self,messages:list[Message]=[]):
        super().__init__(messages)

    def get_all_chats(self, user:User) -> list[User]:
        user_set = set()
        # перебрати усі повідомлення які є в нашій системі
        for message in self: #self.date
            #В повідомленні потрібно дістати інформацію про відправника та отримувача
            author, recepient = message.author, message.recepient
            # перевірити коли користувач є автором
            if user == author:
                user_set.add(recepient)
            #перевірити коли користувач є отримувачем
            if user == recepient:
                user_set.add(author)
            #перевірити коли корустувач є автором та отримувачем
        return list(user_set)
    
    def save_to_file(self):
        with open(MESSAGES_JSON_FILE, 'w') as json_file:
            json.dump(self.data, json_file, default = lambda o: o.to_json(), indent=4 )

    def read_from_json(self):
        # id_set = set () # {1,2,3,4}
        # user_set = set() #{....., .....,......}
        #Прочитати json файл
        #перебрати кожне повідомленнЯ
            #дістати автора та отримувача з повідомлення
            #дістати їх id
            #зробити перевірку чи такий користувач вже був:
                #якщо був то дістаємо з переліку
                #якщо не був то створбємо нового та додаємо до переліку
        users_dict = {}
        message_list = []
        with open(MESSAGES_JSON_FILE) as json_file:
            json_data = json.load(json_file)
            for message_dict in json_data:
                author = None
                recepient = None
                author_id, recepient = message_dict['author']['id'], message_dict['recepient']['id']
                if author_id in users_dict:
                    author = users_dict[author_id]
                else:
                    author_dict = message_dict['author']
                    author = User(author_dict['first_name'],author_dict['last_name'], author_dict['phone_number'])
                    author.id = author_dict['id']
                    users_dict[author_id] = author
                message_list.append(Message(message_dict['content'], author, None))
        return message_list
    
    
    def get_messages_between_users (self, user_one: User, user_two: User) -> list[Message]:
        messages_set = set ()
        # Перебрати усі повідомлення
        for message in self:
            # дістати інформацію про відправника та отримувача
            author, recepient = message.author, message.recepient
            # Перевірити чи user_one є автором та user_two є отримувачем
            if author == user_one and recepient == user_two:
                messages_set.add(message)
            # Перевірити чи user_one є автором та user_two є отримувачем
            if author == user_two and recepient == user_one:
                messages_set.add(message)
        return sorted(list(messages_set))

   
    

user_john = User ('John', 'Doe', '1234567890')
user_jane = User ('Jane', 'Doe', '9876543210')
user_jack = User ('Jack', 'Doe', '9876543210')

message_one = Message ('Hello, Jane', user_john, user_jane)
message_two = Message ('Hello, John', user_jane, user_john)
message_three = Message ('How are you doing?', user_john, user_jane)
message_four = Message("to do: finish",user_john,user_john)
message_five = Message('How do you do? I am Jack', user_jack, user_john)
messages = [message_one, message_two, message_three, message_four, message_five]
message_system = MessageSystem(messages)
#print(message_system.get_all_chats(user_john))

#print (message_system.get_messages_between_users(user_john,user_jane))
# message_system.save_to_file()
# print(messages)
# print(user_jack)
# print(user_jane)
# print(user_john)
print(message_system.read_from_json())