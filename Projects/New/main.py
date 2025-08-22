# validate_email = input("Enter your email address ")
# if "@" not in validate_email or "." not in validate_email:


# validate_email = input("Enter your email address ")
# if validate_email.count("@") == 1:
#     before_at = validate_email.index("@")
#     after_at = validate_email[before_at + 1:]
#     if "." in after_at:
#         print("Valid Credentials")
#     else:
#         print("There must be a '.' after '@'.")
# else:
#     print("Invalid Credentials, there must be exactly one '@'.")



validate_email = input("Enter your email address: ")
if validate_email.count("@") != 1:
    print("There must be exactly one '@' in you email.")
elif "." not in validate_email:
    print("There must be atleast one '.' in your email.")
else:
    if validate_email.count("@") == 1:
        print(f"Your email: {validate_email.lower()} is valid")



validate_password = input("Enter your password e.g Abcdefg1 ")
if len(validate_password) >= 8:
    if not any(char.isupper() for char in validate_password):
        print("There must be atleast one uppercase character")
    elif not any(char.islower() for char in validate_password):
        print("There must be atleast one lowercase character")
    elif not any(char.isdigit() for char in validate_password):
        print("There must be atleast one one digit")
    else:
        print("Valid Credentials")
else:
    print("Invalid Credentials, there must be atleast 8 characters.")





# validate_email = input("Enter your email address ")
# if "@" in validate_email:
#     if validate_email.count("@") != 1:
#         print("There must be exactly one '@'.")
# elif
#     print("There must be an '@' in your email address.")
# elif "." not in validate_email:
#     print("There must be atleast one '.' in your email address.")
# else:
#     print("Valid Credentials")










# NSS(China), NIA (Nigeria), KGB(Russia), 