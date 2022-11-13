class Account:
    def __init__ (self,name: str) -> None:
        """
        this is a function to set the default values
        :param name: holds the account name
        """

        self.__account_name = name
        self.__account_balance = 0




    def deposit(self, amount: float) -> bool:
        """
        this function allows you to deposit money into account balance
        :param amount: amount you want to deposit
        :return: if account deposit was worked or failed
        """
        self.amount = amount
        if self.amount > 0:
            self.__account_balance = self.__account_balance + amount
            return True
        else:
            return False



    def withdraw(self, amount: float) -> bool:
        """
        function that allows you to withdraw from account balance
        :param amount: amount you want to withdraw
        :return: if withdrawl worked or failed
        """
        if (amount <= 0) or (amount > self.__account_balance):
            return False
        else:
            self.__account_balance = self.__account_balance - amount
            return True


    def get_balance(self) -> float:
        """
        function that allows you to check your account balance
        :return: returns account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        function that allows you to check the account name
        :return: the account name
        """
        return self.__account_name

