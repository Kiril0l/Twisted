from data import db
import peewee
from datetime import datetime
from utils import tools


class User(peewee.Model):

    login = peewee.CharField(
        max_lenght=20,
        unique=True
    )
    hash_pass = peewee.CharField(
        max_lenght = 256
    )
    last_login = peewee.DateTimeField(
        default = datetime.now()
    )


    class Meta:
        database = db
        table_name = "users"

class Message(peewee.Model):
    text = peewee.TextField()
    user = peewee.ForeignKeyField(
        User,  #получает ид юсера из табл юсер и связывает
        backref="messages"           #виртуальное поле,кот будет в юсер
    )
    chat = peewee.ForeignKeyField(
        "Chat",
        backref="messages"
    )
    create= peewee.DateTimeField(
        default=datetime.now()
    )

    class Meta:
        database = db
        table_name = "messages"

class Chat(peewee.Model):
    name = peewee.CharField(
        max_lenght = 20,
        unique=True
    )
    user = peewee.ForeignKeyField(
        User,
        backref = "chats"
    )
    class Meta:
        database = db
        table_name ="chats"

class Salt(peewee.Model):
    salt = peewee.ChatField(
        max_lenght=20,
        default = tools.get_rand_value(20)
    )

    user = peewee.ForeignKeyField(
        User,
        backref = "salt",
        unique=True
    )

    @property
    def value(self):
        return self.salt

    class Meta:
        database = db
        table_name = "salt"

if __name__ == '__main__':
    salt = Salt()
    print(salt.value)
