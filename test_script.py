#!/usr/bin/python3
from models.base_model import BaseModel

User = BaseModel()
print(User.id)
print(User.created_at)
print(User.updated_at)
