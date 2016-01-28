from app.models import BaseModel
from app.models.User import User
from app.models.Role import Role
from peewee import Model, ForeignKeyField

class UserRoles(BaseModel):
    user = ForeignKeyField(User, related_name='roles')
    role = ForeignKeyField(Role, related_name='users')
    name = property(lambda self: self.role.name)
    description = property(lambda self: self.role.description)