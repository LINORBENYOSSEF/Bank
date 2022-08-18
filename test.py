import datetime

from db.database import Database
from model.account import Account, Transaction


db = Database()

account = Account(account_number=123, name='moses', balance=3.11, credit_frame=12, transactions=list())
print(dir(account))

transaction = Transaction(dest_account=222, amount=1, datetime=datetime.datetime.now())
print(dir(transaction))
account.transactions.append(transaction)

db.add(account)
print(db.get_all(Account))
