from models.base_model import BaseModel
import peewee as pw
from models.user import User

class Following(BaseModel):
    user = pw.ForeignKeyField(User, backref='to_user', on_delete="cascade")
    follower = pw.ForeignKeyField(User, backref='from_user', on_delete="cascade")
    approved = pw.BooleanField(default=True)
