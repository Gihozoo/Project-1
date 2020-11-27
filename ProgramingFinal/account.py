#author: Barezi Julien and Gihozo Landelin

class Account:
    """ This class is the parent class for the other two accounts (customer and business accounts)
    It has the init function that creates the account and it has five instant variables which are
    name, id number, phone number, balance, and password. It also has two methods which are buy and check balance."""

    def __init__(self, name, idnumber, phonenbr, balance, password):


        self.name = name
        self.idnumber = idnumber
        self.phonenbr = phonenbr
        self.balance = balance
        self.password = password

        print("A new account is created under the name , self.name,  your account balance\n"
              "is , self.balance")

    def buy(self):
        """In this method, the user is able to pay for different things such as electricity and airtime.
        the program asks the user which of the two the user want and after the user checking the program
        asks them to input their information and the transaction is made.

        :return= your balance after removing money you used in paying"""

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
        """"  In this method, the user is shown the amount of money s/he has on their account
         after inputting their password.

          :return= available balance"""

        print("Your balance is", self.balance)

    def deposit(self):
        """" In this method, the user is asked the amount of money s/he wants to deposit,
         and then s/he is given a confirmation message that the money has been deposited
         detailing the current balance too.

         :return = money you deposited plus the amount that was on your account before"""

        amount = int(input('Enter the amount to deposit:'))

        self.balance += amount
        print("Your New Balance ", self.balance)

    def create_account(self):
        name = input("What is your name?")
        idnumber = int(input('input your id number'))
        balance = int(input("What is your initial deposit"))
        password = int(input("What is your password( a password should be four numbers)"))
        phoneNumber = int(input("What is your phone number"))