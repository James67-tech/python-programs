#user should enter their name and ID no. to create a bank account if they dont they can leave by quitting the program.
# If the user is registered they should be able to deposit to and withdraw money from the account which they will be assigned

is_registered = False
balance = 0
idNO = ""
FullName = ""

accNO = ("S001","S002","S003","S004")


print("------------ STANBIC BANK ------------")
print()
print("How may we help you today : ")
print("1. Access Our Services")
print("2. Leave ")
print()
choice = int(input(("Select any of the Two : ")))

if choice == 2:
    print("Thank You for Visiting US!!!!!")
 
elif choice == 1:
    print("We offer the following services : ")
    print()
    print("1. Bank Account Services ")
    print("2. Loans")
    print()
    print("To access our Services you need an Account")
    descision = (input(("Do you want to register (y/n) :"))).lower()
    if not descision.isalpha():
        print("Input y for yes and n for no")
        descision = (input(("Do you want to register (y/n) :"))).lower()
    elif descision == "n":
        print("GoodBye and Thank You for Visiting US!!!!!")
    elif descision == "y" :
        idNO = input("Enter your Original ID Number : ")
        if not idNO.isdigit():
                    print("ID Number should be digits only")
                    idNO = input("Enter your Original ID Number : ")
        else:
            FullName = input("Enter your Full Name : ")
            if not FullName.isalpha:
                print("Full Name should contain letters only")
                FullName = input("Enter your Full Name : ")
            else:
                print("Your Account has been Created ",FullName)
    else :
        print("Invalid Character")
        print("Input y for yes and n for no")
        descision = (input(("Do you want to register (y/n) :"))).lower()
else :
    print("Invalid choice")
    print("Choose between 1 and 2")
    print("1. Access Our Services")
    print("2. Leave ")
    print()
    choice = int(input(("Select any of the Two : ")))           
        
       
        
    
    
    

# while 
# print("We offer the following services : ")
# print("")
# while is_registered == False: