from account import Account


class Customer(Account):
    """"This class inherits from the account class. The difference between the customer account
    and the business account is that in the customer account transactions require some transaction
    fees while for the business class all transactions are free."""

    pass

    def c_transfer(self):
        """In this method the user is going to transfer money to another account

         :return= the amount you transferred and the remaining balance"""
        account = input("Which account do you want to transfer money to\n"
                        "put their phone number")
        amount = int(input("How much money do you want to send"))
        amount2 = amount * 0.03
        amount3 = amount + amount2
        if amount3 > self.balance:
            print("Insufficient Balance!")
        else:
            print("You are going to transfer ", amount, " to ", account, "the transaction fee is"
                  , amount2, ".")
            password = int(input('Enter your password to confirm.'))
            if password == self.password:
                self.balance -= amount3
                print("You have successfully transferred", amount, " to ", account, ".\n"
                                                                                    "your new balance is ",
                      self.balance)
            else:
                print("Wrong password, try again")

    def c_withdraw(self):
        """"In this method the user inputs the amount of money they want to withdraw and then the password
         and the money is deducted from their balance plus the transaction fee.

         :return= It returns the amount withdrawn from your account and the
         remaining balance"""
        amount = int(input("Enter the amount to withdraw:"))
        amount2 = amount * 0.05
        amount3 = amount + amount2
        if amount3 > self.balance:
            print("Insufficient Balance!")
        else:
            print("You are going to withdraw ", amount, " the transaction fee is "
                  , amount2, ".")
            password = int(input('Enter your password to confirm.'))
            if password == self.password:
                self.balance -= amount3
                print("You have successfully withdrew", amount, "\n"
                      "your new balance is ", self.balance)

    def payment(self):
        """"In this method, the user is asked to input the code of the business they want the money to,
         then the password and the money are reduced from their account.

         :return= the amount of money paid and the remaining balance"""
        code = int(input("Enter the code of the business you want to pay"))
        amount = input("Enter the amount of money you want to pay")
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            print("You are going to pay", amount, " to ", code, ".")
            password = int(input("Enter your password to confirm"))
            if password == self.password:
                self.balance -= amount
                print("You have successfully paid", amount, " to ", code, ".\n"
                      "your new balance is ", self.balance)
            else:
                print("Wrong password, try again")