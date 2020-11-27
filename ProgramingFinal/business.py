from account import Account


class Business(Account):
    """This class is a child class that inherits the characteristics from the main clas
    s account. the difference is that
    in this account all the transactions are free"""

    pass

    def b_transfer(self):
        """" In this method the user inputs the amount of money they want to withdraw and then
        the password and the money is reduced from their balance and does not remove the transaction fee.

        :return= amount transferred, account transferred too and the new balance"""

        account = input("Which account do you want to transfer money to\n"
                        "put their phone number")
        amount = int(input("How much money do you want to send"))
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            print("You are going to transfer ", amount, " to ", account, ".")
            password = int(input('Enter your password to confirm.'))
            if password == self.password:
                self.balance -= amount
                print("You have successfully transferred", amount, " to ", account, ".\n"
                                                                                    "your new balance is ",
                      self.balance)
            else:
                print("Wrong password, try again")

    def b_withdraw(self):
        """" In this method, the program asks the user to input the phone number of the recipient of the cash,
         input the amount(by also checking if the amount doesn’t exceed what they have in the account),
         confirm the transfer by input the password and finally getting
         the confirmation message that the money has been transferred detailing the remaining amount
         and this is done for free.

         :return= the amount withdrawn and the remaining balance"""
        amount = int(input("Enter the amount to withdraw:"))
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            print("You are going to withdraw ", amount, ".")
            password = int(input('Enter your password to confirm.\n'))
            if password == self.password:
                self.balance -= amount
                print("You have successfully withdrew", amount, "\n"
                      "your new balance is ", self.balance)