print("-------- STANBIC BANK --------")
print()
print("WELCOME TO OUR BANK FN")

FullName = ""
is_good = True
balance = 10000

choice = (input("Would you like to open an account (y/n) : ")).lower()
print()

# Create the User Account
while is_good:
    FullName = input("Enter your FullName : ")
    
    
    if not FullName.isalpha() :
        print("FullName cannot contain special characters and numbers")

        
    else:
        idNo = input("Enter your ID Number : ")
        if not idNo.isdigit():
            print("ID Number must be Numbers only")
            
        else :
           print("Account for ",FullName," created Successfully !!!!")
           go = True
           print()
           
    
    
    
    while go :
        action = (input("Would you like to deposit or withdraw (d/w) or quit(q) ?")).lower()
        
        if action == "d":
            amount = float(input("Enter amount to deposit : "))
            if amount > 0:
                balance += amount
                print("Deposit Successful !!!")
                print("New Account Balance is : ",balance)
            else:
                print("Invalid Amount")
                
        elif action == "w":
                amount = float(input("Enter amount to withdraw : "))
            
                if amount < 0 :
                    print("Invalid amount")
                elif amount > balance :
                    print("Amount greater than balance")
                else :
                    print("Withdraw Successful !!!")
                    print("New Account Balance is : ",balance)
        elif action == "q" :
            go = False
            print("Goodbye!!!!")
                
            
            
            
                
