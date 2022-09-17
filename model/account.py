from datetime import datetime

from .base import Model, Column


class Transaction(Model):
    dest_account = Column(int)
    amount = Column(float)
    datetime = Column(datetime)
    direction = Column(str)


class Account(Model):
    account_number = Column(int)
    name = Column(str)
    balance = Column(float)
    transactions = Column(Transaction, is_many=True)
