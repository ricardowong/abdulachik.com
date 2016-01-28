from app.models import BaseModel
from peewee import CharField, TextField
from flask.ext.security import RoleMixin

class Role(BaseModel, RoleMixin):
    name = CharField(unique=True)
    description = TextField(null=True)