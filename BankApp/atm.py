from cardDetails import cardDetails

def print_menu():
    ### Print options for the user
    print("Please choose from one of the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

def deposit(cardDetails):
    try:
        deposit = float(input("How much money would you deposit:"))
        cardDetails.set_balance(cardDetails.get_balance() + deposit)
        print("Thank you for your money. Your new balance is:", str (cardDetails.get_balance()))
    except:
        print("Invalid input")

def withdraw(cardDetails):
    try:
        withdraw = float(input("How much money would you like to withdraw:"))
        ##Check if user has enough money
        if(cardDetails.get_balance() < withdraw):
            print ("Insufficent balance :(")
        else:
            cardDetails.setbalance(cardDetails.get_balance() - withdraw)
            print("You're good to go ! Thank you :)")
    except:
        print("Invalid input")

def check_balance(cardDetails):
    print("Your current balance is:", cardDetails.get_balance())

    if __name__ == "__main__":
        current_user = cardDetails("","","","","")

        ### Create a repo of cardDetails
        list_of_cardDetails = []
        list_of_cardDetails.append(cardDetails("47589673923215748", 2345, "Jacob", "Macon", 180.51))
        list_of_cardDetails.append(cardDetails("47589673950215748", 2345, "Daniel", "Bacon", 170.51))
        list_of_cardDetails.append(cardDetails("47589673960215748", 2345, "Joshua", "Racon", 186.51))
        
        ### Prompt user for debit card number
        debitCardNum = ""
        while True:
            try:
                debitCardNum = input("Enter debit card:")
                ### Check against repo
                debitMatch =[Detail for Detail in list_of_cardDetails if Detail.cardNum == debitCardNum]
                if(len(debitMatch)> 0):
                    current_user = debitMatch[0]
                    break
                else:
                    print("Card number not recognized. Please try again.")
            except:
                print("Card number not recognized. please try again.")
        ### Prompt for PIN
        while True:
            try:
                userPin = int(input("Please enter your pin:").strip())
                if(current_user.get_pin() == userPin):
                    break
                else:
                    print("Invalid PIN. please try again.")
            except:
                print("Invalid PIN. please try again.")

        ## Print options
        print("Welcome", current_user.get_firstname(), " :)")
        option = 0
        while(True):
            print_menu()
            try:
                option = int(input())
            except:
                print("Invalid input. Please try again.")
            if(option == 1):
                deposit(current_user)
            elif(option == 2):
                withdraw(current_user)
            elif(option ==3):
                check_balance(current_user)
            elif(option ==4):
                break
            else:
                option = 0
        
        print("Thank you. Have a nice day :)")