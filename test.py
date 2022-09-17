import datetime

from db.database import Database
from model.account import Account, Transaction


db = Database()

#account = Account(account_number=554, name='moses', balance=3.11, credit_frame=12, transactions=list())
#print(dir(account))

#transaction = Transaction(dest_account=222, amount=1, datetime=datetime.datetime.now(), direction='IN')
#account.transactions.append(transaction)

#transaction = Transaction(dest_account=222, amount=1, datetime=datetime.datetime.now(), direction='OUT')
#account.transactions.append(transaction)

#db.add(account)
#print(db.get_all(Account))
#print(db.find_one(Account, 'account_number', 555))
