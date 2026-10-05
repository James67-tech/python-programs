#A while loop to prompt a user to create a username and password. Loop continues as long as the user enters empty strings for either the username or password.

username = input("Enter your username: ")


while username =="":
    print("Username cannot be empty. Please enter a valid username.")
    username = input("Enter your username: ")
    
    if not username == "":
        password = input("Create your password: ")
        while password == "":
            print("Password cannot be empty. Please enter a valid password.")
            password = input("Create your password: ")
            break
        print("Account created successfully!")
        print ("Username:", username)
        print ("Password:", password)

            