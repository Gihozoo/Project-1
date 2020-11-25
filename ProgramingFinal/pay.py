from account import Account


class Pay(Account):
    pass

    def make_payment(self):
        code = input("put the code of the uder you want to pay")
        amount = int(input("How much money do you want to send"))
        password = int(input("You are going to transfer "
                             "", amount, " to ", code, " To confirm input your password"))
        if password == self.password:
            self.balance -= amount
            print("Your new balance is ", self.balance)
        else:
            print("Wrong password, try again")
