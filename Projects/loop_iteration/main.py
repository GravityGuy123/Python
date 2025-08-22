import random as r

web_dev = ["Edu", "Gravity", "Chioma", "Mega-Pips", "Ifenna"]
dev_list = []  # Empty list to store objects

for st in web_dev:
    randomAge = r.randint(20, 100)
    student_age = {st: randomAge}
    dev_list.append(student_age)
    print(student_age)

print("\nFinal List:", dev_list)
