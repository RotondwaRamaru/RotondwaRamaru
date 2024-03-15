#ATM
print("Get Cash ATM")

restart = ('Y')
chances = 3
Balance = 7542.12

while chances >= 0:
    pin = int(input('Enter your Pin: '))
    if pin ==(1234):
        print("Correct\n")
        while restart not in ("n", "NO", "no", "N"):
            print("Press 1 for Balance\n")
            print("Press 2 for Withdrawals\n")
            print("Press 3 to pay in\n")
            print("Press 4 to Return")
            option = int(input("Choose Function"))
            if option == 1:
                print("Your Balance is \n",
                      "R", Balance, "\n")
                restart = input("Would you like to go back to Start Menu?")
                if restart in("n", "NO", "no", "N"):
                    print("Thank You, Goodnye!")
                    break
            elif option == 2:
                    option2 = ('Y')
                    withdrawl = float(input("How muvh would you like to get:"))
                    if withdrawl in [50,100,150,200]:
                        balance = Balance - withdrawl
                        print("Your remaining balance is: R", balance)
                        restart = input("Would you like to go back to Start Menu?")
                        if restart in("n", "NO", "no", "N"):
                            print("Thank You, Goodnye!")
                            break
                    elif withdrawl != [50,100,150,200]:
                        print("Invalid Transaction, Please Try  again!")
                        restart = "Y"
                    elif withdrawl == 1 :
                        withdrawl = float(input("Please Enter Desired Amount: "))

            elif option == 3:
                Pay_in = float(input("How much would you like to pay in? "))
                balance = Balance + Pay_in
                print("\nYour Balance is now R", balance)
                restart = input("Would you like to  go back? ")
                if restart in("n", "NO", "no", "N"):
                    print("Thank You, Goodnye!")
                    break  
            elif option == 4:
                print("Please Wait for card to return...\n")
                print("Thank You for your service")
                break
            else:
                print("Please Enter a correct number. \n")
                restart = ("Y")
    elif pin != ('1234'):
        print("Incorrect Password")
        chances = chances - 1
        if chances == 0:
            print("\nNo More Tries")
            break
                