from models.base_model import BaseModel
import peewee as pw
from models.user import User

class Donation(BaseModel):
    receiver_id = pw.ForeignKeyField(User, backref='received_donations', on_delete="cascade")
    sender_id = pw.ForeignKeyField(User, backref="sent_donations", on_delete="cascade")
    amount = pw.DecimalField(decimal_places=2, null=False)