print("Welcome")

user_details ={
     "name": "Tobenna",
     "pin": "2024",
     "balance": 20000
}
user_name = input("Enter username: ")
pin = input("Enter PIN: ")
if user_name == user_details["name"] and pin == user_details["pin"] :       
        print("Login successful")
        print("Welcome ", user_name,"!")
        print("Press 1: Withdraw")
        print("Press 2: Transfer")
        print("Press 3: Buy Airtime")
        print("Press 4: Check balance")
        print("Press 5: Exit")
        choice = eval(input("Enter choice: "))
        if choice == 1:
            eval(input("Enter amount: "))
            if choice > user_details["balance"]:
                 print("You don't have enough money!!!")
            else:
                 print("withdraw successful")
                 print("Remove card")
                 
        elif choice == 2:
            input("Enter account number: ")
            print("1.Gt bank" "\n"
                  "2.Opay" "\n"
                  "3. Zeinth bank" "\n"
                  "4.First bank" "\n")
            choice = eval(input("Enter bank: "))
            choice = eval(input("Enter amount: "))
            if choice > user_details["balance"]:
                 print("Insufficient Funds")
            else:     
                 print("withdraw successful")
                 print("Remove card")
                         
            
        elif choice == 3:
            input("Enter Phone Number: ")
            print("1.MTN" "\n"
                  "2.Airtel" "\n"
                  "3.GLO" "\n") 
            choice = eval(input("Enter choice: "))
            choice = eval(input("Enter amount: "))
            if choice > user_details["balance"]:
                 print("You no get money and you wan buy card?")
            else:
                 print("Transfer successful")
                 print("Remove card")
            
        elif choice == 4:
            choice = int(input("Enter pin: "))
            
            print("Your Balancs is: ", user_details["balance"])
            print("Remove Card")
           
            
        elif choice == 5:
            print("Goodbye!")
        else:
            print("Invalid choice")
else: 
    print("Login failed")
