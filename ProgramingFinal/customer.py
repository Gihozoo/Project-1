from account import Account


class Customer(Account):
    pass

    def c_transfer(self):
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