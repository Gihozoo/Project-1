from account import Account
from customer import Customer
from business import Business

#creating accounts
account1 = Customer("Christian", "199290877464727", "0780987122", 2000, 1234)
account2 = Business("Kenny", "19920010877490827", "0788978742", 25000, 4321)

cont = "y"

#starting a loop so that the user can be allowed to do more than one operation


while cont != "n":

    #Asking the user which account they have because there are two different types and each has its functions

    what = int(input("What is the type of your account\n"
                     "1: customer Account\n"
                     "2: business Account"))

#If they choose one we call methods from customer
    if what == 1:
        query = int(input("What do you want to do""\n"
                          "1: deposit money""\n"
                          "2: Withdraw money""\n"
                          "3: check balance""\n"
                          "4: Transfer money\n"
                          "5: buy electricity or airtime\n"
                          "6: pay a business\n"
                          "7: create account\n"))

        if query == 1:
            account1.deposit()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")
        elif query == 2:
            account1.c_withdraw()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

        elif query == 3:
            account1.enquiry()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

        elif query == 4:
            account1.c_transfer()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

        elif query == 5:
            account1.buy()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

        elif query == 6:
            account1.payment()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

        elif query == 7:
            account1.create_account()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")
#If they choose 2 we use methods from the business class
    elif what == 2:
        query = int(input("What do you want to do""\n"
                          "1: deposit money""\n"
                          "2: Withdraw money""\n"
                          "3: check balance""\n"
                          "4: Transfer money\n"
                          "5: buy electricity or airtime\n"))

        if query == 1:
            account2.deposit()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")
        elif query == 2:
            account2.b_withdraw()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

        elif query == 3:
            account2.enquiry()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")

        elif query == 4:
            account2.b_transfer()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")
        elif query == 5:
            account2.buy()
            cont = input("Do you want to do another operation?\n"
                         "y: yes\n"
                         "n: no\n")