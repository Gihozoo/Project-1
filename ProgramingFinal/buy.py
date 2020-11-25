from account import Account
Account1 = Account("Christian", "199290877464727", "0780987122", 2000, "1234")


class Buy(Account):
    pass




    def airtime(self):
        phone_number = int(input("What is your phone number?"))
        amount = int(input("How much money do you want to recharge?"))
        print("You want to recharge ", amount, "on the phone number, ", phone_number)
        password = int(input("To confirm, put your password"))
        if password == self.password:
            self.balance -= amount
            print("Your new balance is ", self.balance)
        else:
            print("Wrong password, try again")
