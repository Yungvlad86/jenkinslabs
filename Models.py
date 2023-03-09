from peewee import *

db = SqliteDatabase("data.db")
    
class BaseModel(Model):
    id = PrimaryKeyField(unique = True)

    class Meta:
        database = db
        order_by = "id"


class Client(BaseModel):
    Name = CharField()
    City = CharField()
    Address = CharField()

    class Meta:
        table_name = "CLIENTS"

class Order(BaseModel):
    Client_id = ForeignKeyField(Client)
    Date = DateField()
    Amount = FloatField()
    Description = CharField()

    class Meta:
        table_name = "ORDERS"

