from datetime import datetime
from db.database import Database
from model.account import Account, Transaction


def do_transaction(db: Database, src_account: Account, dst_account_number: int, amount: float):
    with db.do_transaction() as session:
        try:
            if src_account.balance < amount:
                raise ValueError('not enough balance to perform transaction')

            dst_account = db.find_one(Account, 'account_number', dst_account_number)
            if dst_account is None:
                raise ValueError(f"no such account: {dst_account_number}")

            now = datetime.now()

            src_transaction = Transaction()
            src_transaction.amount = amount
            src_transaction.dest_account = dst_account.account_number
            src_transaction.datetime = now
            src_transaction.direction = 'OUT'

            src_account.balance -= amount
            src_account.transactions.append(src_transaction)

            db.update_one(src_account, 'account_number', session=session)

            dst_transaction = Transaction()
            dst_transaction.amount = amount
            dst_transaction.dest_account = src_account.account_number
            dst_transaction.datetime = now
            dst_transaction.direction = 'IN'

            dst_account.balance -= amount
            dst_account.transactions.append(dst_transaction)

            db.update_one(dst_account, 'account_number', session=session)

            session.commit_transaction()
        except Exception:
            session.abort_transaction()
            raise
