from data import db
import peewee
from datetime import datetime
from utils import tools


class User(peewee.Model):
    __x = property()

    login = peewee.CharField(
        max_length=20,
        unique=True
    )
    hash_pass = peewee.CharField(
        max_length=256
    )
    last_login = peewee.DateTimeField(
        default=datetime.now()
    )

    def is_login(self, password):
        salt = Salt.get(user=self)
        hash_pass = tools.hash256(
            tools.str_to_sort_list(password, salt.value)
        )
        return self.hash_pass == hash_pass

    @__x.setter
    def get_hash(self, value):
        self.salt = Salt()
        self.hash_pass = tools.hash256(
            tools.str_to_sort_list(value, self.pass_salt.value)
        )

        def save(self):
            record_id = super().save()
            try:
                self.pass_salt.user = self
            except AttributeError:
                pass
            else:
                self.pass_salt.save()
            return record_id




    class Meta:
        database = db
        table_name = "users"


class Chat(peewee.Model):
    name = peewee.CharField(
        max_length=20,
        unique=True
    )
    user = peewee.ForeignKeyField(
        User,
        backref="chats"
    )

    class Meta:
        database = db
        table_name = "chats"


class Message(peewee.Model):
    text = peewee.TextField()
    user = peewee.ForeignKeyField(
        User,  # получает ид юсера из табл юсер и связывает
        backref="messages"  # виртуальное поле,кот будет в юсер
    )
    chat = peewee.ForeignKeyField(
        Chat,
        backref="messages"
    )
    create = peewee.DateTimeField(
        default=datetime.now()
    )

    class Meta:
        database = db
        table_name = "messages"


class Salt(peewee.Model):
    salt = peewee.CharField(
        max_length=20,
        default=tools.get_rand_value(20)
    )

    user = peewee.ForeignKeyField(
        User,
        backref="salt",
        unique=True
    )

    @property
    def value(self):
        return self.salt

    class Meta:
        database = db
        table_name = "salt"

    def __str__(self):
        return f"{self.user.login}"


if __name__ == '__main__':
    salt = Salt()
    print(salt.value)
