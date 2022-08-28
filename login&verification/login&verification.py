# [name here] 3/08/2022
# [purpose]

# Libraries/Imports
import random
from time import sleep
global active_user

# Print out accounts from accounts.txt


def view_all_users():
    # Open file and print out all the text
    file = open("accounts.txt", "r")
    print("\n=== List of Accounts ===")
    for x in file:
        print("- ", x)
    print("========================")

# Menu for when user logs in


def admin_menu():
    global active_user
    command = None
    # Loop menu display if command is not selected or invalid
    while command == None:
        print("Logged in as:", active_user)
        command = input("\nView Users(V) or Exit(X): ")
        if command.upper() == "V":
            view_all_users()
            admin_menu()
        elif command.upper() == "X":
            print("\n== Returned to menu ==")
            main()
        else:
            print("invalid input")
            admin_menu()
            command = None
    command = None


# Login functionality with user verification against account.txt


def login():
    global active_user
    active_user = None
    print("Attempting Login:")
    username = input("\nplease enter your username: ")
    password = input("please enter your Password: ")
    file = open("accounts.txt", "r")
    # Goes through account.txt and compares username and password to input line by line
    for x in file:
        retreived_values = x.split(" ", 1)
        if username.strip() == retreived_values[0].strip() and password.strip() == retreived_values[1].strip():
            # Saves and opens Admin menu
            active_user = retreived_values[0].strip()
            print("\n== Login Successful")
            admin_menu()
            break
    if active_user == None:
        # Return to main menu if user doesnt exist
        print("User doesn't exist, consider registering it.")
        print("\n== Returned to menu ==")
        main()

# Builds up password choices and concatenates randomly chosen characters into a password


def password_generator():
    choices = ""
    print("\n==Password Requirements==")
    option = None
    # Loop menu display while option is not selected or invalid and add to generator choices if option is required.
    # Repeat for each Requirement(numbers,letters and special characters)
    while option == None:
        option = input("Do you require numbers?(Y)")
        if option.upper() == "Y":
            choices += "0123457890123456789"
        elif option.upper() == "N":
            ""
        else:
            print("  Invalid input, try again.")
            option = None
    option = None
    while option == None:
        option = input("Do you require letters?(Y/N)")
        if option.upper() == "Y":
            choices += "ABCDEFGHIJKLMNOPQRSTUVQXYZ"
        elif option.upper() == "N":
            ""
        else:
            print("  Invalid input, try again.")
            option = None
    option = None
    while option == None:
        option = input("Do you special characters?(Y)")
        if option.upper() == "Y":
            choices += "!@#$%^&*!@#$%^&*"
        elif option.upper() == "N":
            ""
        else:
            print("  Invalid input, try again.")
            option = None
    option = None
    if choices == "":
        print("Password doesn't have any requirements")
        return ""
    else:
        num_of_characters = None
        while num_of_characters == None:
            num_of_characters = input("How many characters? ")
            # Generate and concat a new character by the num_of_characters required in the password.
            if num_of_characters.isdigit():
                generatedPass = ""
                for x in range(int(num_of_characters)):
                    generatedPass += random.choice(choices)
                return generatedPass
            else:
                print("  Input not a number, try again.")
                num_of_characters = None

# Writes new account details into the accounts.txt file


def save_password(username, password):
    # Open the file and write in new account details
    file = open("accounts.txt", "a")
    file.write("\n"+username+" "+password)
    file.close()
    print("==Account successfully saved==")
    print("your account is:", username, password)

# Registers new user accounts into the system


def register():
    print("Attempting Register:")
    # If user inputs doesn't reference an account in account.txt then create that account.
    username = input("\nplease enter your username: ")
    file = open("accounts.txt", "r")
    User_exists = False
    for x in file:
        # Split the retreived account details and verify if the username has been used
        retreived_values = x.split(" ", 1)
        if username.strip() == retreived_values[0].strip():
            print("you seem to already have an account")
            User_exists = True
            break
    # If username doesn't exist get the password
    if User_exists == False:
        password = input(
            "please enter your Password or Generate Password(G): ")
        if password.upper() == "G":
            # Auto generate a password if user requests it
            password = password_generator()
            save_password(username, password)
        elif(password == ""):
            print("Please try again")
        else:
            confirm_password = input("Confirm your password: ")
            if confirm_password == password:
                save_password(username, password)
    else:
        print("\n")
    main()

# Main option menu to access login and registration


def main():
    command = input("Login(L) ,Register(R) or Exit(X): ")
    if command.upper() == "L":
        login()
    elif command.upper() == "R":
        register()
    elif command.upper() == "X":
        print("Closing Application...")
        sleep(2)
        print("Exited...")
    else:
        print("invalid input\n")
        main()


# Beginning of application
print("\n== Welcome to the System! ==")
print("Please Select an option...")
main()
