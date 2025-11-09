current_users = ["DevDemon", "Edu-Crypt", "megapips", "DevDiva", "Paragon123", "John173"]
print(f"\nCurrent Users: {current_users}\n")

new_users = ["Raone", "KD_Banger", "BiteCruncher", "edu-crypt", "Paragon123", "JOHN", "MegAPiPs", "Badest-X"]
print(f"New Users: {new_users}\n")

# Using list comprehension to generate an independent copy
check_current_users = list(value.lower() for value in current_users)

for new_user in new_users:
   
    if new_user.lower() in check_current_users:
        print(f"{new_user} is taken enter a new username")
    else:
        print(f"{new_user} is available")
        current_users.append(new_user)

print(f"Current Users: {current_users}")