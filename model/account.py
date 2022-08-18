from datetime import datetime

from .base import Model, Column


class Transaction(Model):
    dest_account = Column('Account')
    amount = Column(float)
    datetime = Column(datetime)


class Account(Model):
    account_number = Column(int)
    name = Column(str)
    balance = Column(float)
    credit_frame = Column(float)
    transactions = Column(Transaction, is_many=True)
