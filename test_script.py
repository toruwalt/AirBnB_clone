#!/usr/bin/python3
from models.base_model import BaseModel

User = BaseModel("Adam", 89)
print(User)
print(User.id)
print(User.name)

User.name = "My First Name"
User.my_number = 89
print(User.id)
print(User.name)
print(User.my_number)
print(User.created_at)
print(User.updated_at)
