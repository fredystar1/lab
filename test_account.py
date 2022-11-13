import pytest
from account import *


class Test:
    def setup_method(self):
        self.p1 = Account("John")
        self.p2 = Account("James")

    def test___init__(self):
        assert self.p1.get_name() == "John"
        assert self.p1.get_balance() == 0
        assert self.p2.get_name()== "James"
        assert self.p1.get_balance() == 0


    def test_deposit(self):
        assert self.p1.deposit(0.00) is False
        assert self.p1.deposit(-10.00) is False
        assert self.p1.deposit(10.00) is True
        assert self.p1.get_balance() == 10

        assert self.p2.deposit(0.00) is False
        assert self.p2.deposit(-10.00) is False
        assert self.p2.get_balance() == 0


    def test_withdraw(self):
        assert self.p1.deposit(10.00) is True
        assert self.p1.withdraw(0.00) is False
        assert self.p1.withdraw(-10.00) is False
        assert self.p1.withdraw(2.00) is True
        assert self.p1.get_balance() == 8


        assert self.p2.withdraw(0.00) is False
        assert self.p2.withdraw(-10.00) is False
        assert self.p2.withdraw(2.00) is False
        assert self.p2.get_balance() == 0