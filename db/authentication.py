from typing import Optional

from model.account import Account
from db.database import Database


class Authentication(object):

    def __init__(self, database: Database):
        self._database = database
        self._logged_account = None

    @property
    def current_account(self) -> Optional[Account]:
        if self._logged_account is None:
            return None

        return self._database.find_one(Account, 'account_number', self._logged_account)

    def login(self, account_number: int) -> Account:
        if self.current_account is not None:
            raise AssertionError('account logged in already')

        account = self._database.find_one(Account, 'account_number', account_number)
        if account is None:
            raise KeyError("No such account!")

        self._logged_account = account_number
        return account

    def logout(self):
        self._logged_account = None
