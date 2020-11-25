#author: Barezi Julien and Gihozo Landelin

class Account:
    def __init__(self, name, idnumber, phonenbr, balance, password):
        # idnumber = input("What is you id number?\n")
        # name = input("What are the names on your id\n")
        # phonenbr = input("What is you phone number?\n")
        # balance = input("What is your initial deposit?\n"
        #                 "It should be 2000Rwf minimum\n")
        # password = int(input("Create your password\n"
        #                      "It should be composed of 4 numbers\n"))

        self.name = name
        self.idnumber = idnumber
        self.phonenbr = phonenbr
        self.balance = balance
        self.password = password

        print("A new account is created under the name , self.name,  your account balance\n"
              "is , self.balance")

    def buy(self):
        option = input("If you want to buy cash power, press 1\n"
                       "If you want to buy airtime, press 2")
        if option == "1":
            cash_power_number = int(input("What is your cashpower number?"))
            amount = int(input("How much money do you want to recharge?"))
            print("You want to recharge ", amount, "on the account number, ", cash_power_number)
            password = int(input("To confirm, put your password"))
            if password == self.password:
                self.balance -= amount
                print("Your new balance is ", self.balance)
            else:
                print("Wrong password, try again")
        elif option == "2":
            phone_number = int(input("What is your phone number?"))
            amount = int(input("How much money do you want to recharge?"))
            print("You want to recharge ", amount, "on the phone number, ", phone_number)
            password = int(input("To confirm, put your password"))
            if password == self.password:
                self.balance -= amount
                print("Your new balance is ", self.balance)
            else:
                print("Wrong password, try again")

        else:
            print("Wrong input, try again!")

    def enquiry(self):
        print("Your balance is", self.balance)

    def deposit(self):
        amount = int(input('Enter the amount to deposit:'))

        self.balance += amount
        print("Your New Balance ", self.balance)