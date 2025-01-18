import getpass

# Persistent storage for user accounts
Store_of_Usernames_and_Passwords = {}

print('''
Welcome to Mail.
You have 3 Options:
A. Sign In
B. Sign Up
C. Sign Out
Please enter the option's letter (A, B, or C) to proceed.
''')

choice = ''
while choice != "C":
    choice = input("Enter your choice (A, B, or C): ").upper()

    if choice == 'B':
        # Sign Up
        user = input('Enter your username (we will automatically add "@mail.org"): ')
        user = user.lower() + "@mail.org"

        if user not in Store_of_Usernames_and_Passwords:
            print(f"{user} will be your email.")
            passw = getpass.getpass('Set your password: ')
            Store_of_Usernames_and_Passwords[user] = passw
            print("Your account has been created successfully!\n")
        else:
            print("This email address is already registered. Please try another username.\n")

    elif choice == "A":
        # Sign In
        User_Name = input("Hi! Please enter your Email Address: ").lower()
        Pw = getpass.getpass("Enter your Password: ")

        if User_Name in Store_of_Usernames_and_Passwords:
            if Store_of_Usernames_and_Passwords[User_Name] == Pw:
                print(f"Welcome, {User_Name}!\n")
            else:
                print("Incorrect password. Please contact our helpline to reset your password.\n")
        else:
            print("Email not found in our database. Please use option 'B' to create an account.\n")

    elif choice == "C":
        # Sign Out
        print("Thank you for using our service. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter A, B, or C.\n")
