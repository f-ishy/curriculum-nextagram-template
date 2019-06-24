from models.base_model import BaseModel
import peewee as pw
from models.user import User

class Following(BaseModel):
    user = pw.ForeignKeyField(User, backref='idols', on_delete="cascade")
    follower = pw.ForeignKeyField(User, backref='followers', on_delete="cascade")
    approved = pw.BooleanField(default=True)
