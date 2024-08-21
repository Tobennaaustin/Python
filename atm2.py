print("Welcome")

user_details = {
    "name": "Tobenna",
    "pin": "2024",
    "balance": 20000
}

user_name = input("Enter username: ")
pin = input("Enter PIN: ")

if user_name == user_details["name"] and pin == user_details["pin"]:
    print("Login successful")
    print("Welcome", user_name, "!")
    
    while True:
        choice = ['withdraw', 'Transfer', 'Buy Airtime', 'check balance', 'Exit']
        for i,  choice in enumerate(choice, 1):
            print(f"press {i}: {choice}")

        choice = int(input("Enter choice: "))
        if choice == 1:
            amount = int(input("Enter amount to withdraw: "))
            if amount > user_details["balance"]:
                print("You don't have enough money!!!")
            else:
                user_details["balance"] -= amount
                print("Withdraw successful")
                print("Remove card")
        
        elif choice == 2:
            account_number = input("Enter account number: ")
           
            bank_choice= ['GTBank', 'Opay', 'palmpay', 'First Bank']
            for i, bank_choice in enumerate(bank_choice, 1):
                print(f"{i}:{bank_choice}")
            bank_choice = int(input("Enter bank: "))
            amount = int(input("Enter amount to transfer: "))
            if amount > user_details["balance"]:
                print("Insufficient Funds")
            else:
                user_details["balance"] -= amount
                print("Transfer successful")
                
        
        elif choice == 3:
            phone_number = input("Enter Phone Number: ")

            airtime_choice = ['MTN', 'GLO', 'AIRTEL']
            for i, airtime_choice in enumerate(airtime_choice, 1):
                print(f"{i}:{airtime_choice}")
            airtime_choice = int(input("Enter choice: "))
            amount = int(input("Enter amount to buy: "))
            if amount > user_details["balance"]:
                print("You don't have enough money to buy airtime!")
            else:
                user_details["balance"] -= amount
                print("Airtime purchase successful")
                
        
        elif choice == 4:
            print("Your balance is:", user_details["balance"])
            
        
        elif choice == 5:
            meassage = ['Goodbye!', 'Remove Card']
            for i in meassage:
                print(i)
            break
        
        else:
            print("Invalid choice. Please try again.")
else:
    print("Login failed")
