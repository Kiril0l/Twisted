from playhouse.postgres_ext import PostgresqlExtDatabase

db = PostgresqlExtDatabase(
    "mega_chat",
    user="postgres",
    host="localhost",
    port=5432,
    password="1926734850"
)
from data import models
db.connect()
db.create_tables([models.User, models.Message, models.Chat, models.Salt])
db.close()
