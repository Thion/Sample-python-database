from peewee import *
from os import path

db_connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(db_connection, "eMobilis.db"))

# Create a table for users
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db
User.create_table(fail_silently=True)

class Product(Model):
    name = CharField()
    qtty = CharField()
    Price = CharField()

    class Meta:
        database = db

Product.create_table(fail_silently=True)


class Employee(Model):
    name = CharField()
    regnumber = CharField()
    worktype = CharField()

    class Meta:
        database = db


class School_Admin(Model):
    name = CharField()
    age = CharField()
    gender = CharField()
    email = CharField()
    password = CharField()

    class Meta:
        database = db
