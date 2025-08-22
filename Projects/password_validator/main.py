# Create Password
create_password = input("Create a password: ")

while (
    not create_password
    or len(create_password) < 8
    or create_password.isalpha()
    or create_password.isnumeric()
):
    if not create_password:
        print("Entry cannot be empty.")
    elif len(create_password) < 8:
        print("Your password must be atleast eigth (8) characters long.")
    elif create_password.isalpha():
        print("Your password cannot contain alphabets only.")
    else:
        print("Your password cannot contain numbers only.")
    create_password = input("Create a password: ")
print("Password created successfully.")

# Enter Password

enter_password = input("Enter your password: ")

while not enter_password or enter_password != create_password:
    if not enter_password:
        print("Entry cannot be empty.")
    else:
        print("Incorrect password, try again.")
    enter_password = input("Enter your password: ")
if enter_password == create_password:
    print("Access Granted")
