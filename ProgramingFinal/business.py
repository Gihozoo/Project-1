from account import Account

class Business(Account):
    pass

    def b_transfer(self):
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