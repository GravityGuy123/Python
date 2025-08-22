# Projects

# 1a. Build an Email Validator that will take in a user input and check if the email is valid. For it to be a valid email, it must contain '@' and '.'
# 1b. If it's a valid email, print "Valid credentials", otherwise print "Invalid credentials".
# 1c. This should not pass 5 lines of code.


# validate_email = input("Enter your email address: ")
# if validate_email.count("@") == 1 and validate_email.count(".") == 1:
#     print("Valid credentials")
# else:
#     print("Invalid credentials, there must be only one '@' and one '.'")


validate_email = input("Enter your email address: ")
if validate_email.count("@") == 1:
    before_at = validate_email.index("@")
    after_at = validate_email[before_at + 1:]
    if "." in after_at:
        print("Valid Credentials")
    else:
        print("There must be at least one '.' after '@'.")
else:
    print("Invalid Credentials, there must be only one '@'.")



# 2a. Build a valid Password Validator that will check if the password is valid.
# 2b. For it to be a valid password, it should contain at least one uppercase letter, one lowercase letter, one digit and the minimum length should should be at least 8 characters long.
# 2c. If it's a valid password, print "Valid credentials", otherwise print "Invalid credentials".


# validate_password = input("Enter your password: ")
# if len(validate_password) >= 8:
#     if (
#         any(char.isupper() for char in validate_password)
#         and any(char.islower() for char in validate_password)
#         and any(char.isdigit() for char in validate_password)
#     ):
#         print("Valid Credentials")
#     else:
#         print("You password must have at least one uppercase, one lowercase and one digit")
# else:
#     print("Your password must be up to eight characters long")


validate_password = input("Enter your password e.g Abcdefg1: ")
if len(validate_password) >= 8:
    if not any(char.isupper() for char in validate_password):
        print("No uppercase character found")
    elif not any(char.islower() for char in validate_password):
        print("No lowercase character found")
    elif not any(char.isdigit() for char in validate_password):
        print("No digit(s) found")
    else:
        print("Valid Credentials")
else:
    print("Invalid Credentials, your password must be at least eight(8) characters long.")