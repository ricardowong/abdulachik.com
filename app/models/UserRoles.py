from helpers import BaseModel
from User import User
from Role import Role
from peewee import Model, ForeignKeyField

class UserRoles(BaseModel):
    user = ForeignKeyField(User, related_name='roles')
    role = ForeignKeyField(Role, related_name='users')
    name = property(lambda self: self.role.name)
    description = property(lambda self: self.role.description)