from peewee import *
from config import *

db = PostgresqlDatabase(host=host, user=user, password=password, database=db_name, port=port)


class Article(Model):
    img_url = TextField(null=True)
    title = TextField()
    price = CharField()
    currency = CharField(max_length=1, null=True)
    city = CharField()
    created_at = CharField()
    description = TextField()
    beds = TextField()

    class Meta:
        database = db
