# item_price = 300
# quantity = 3
# total = f"{item_price * quantity}"
# print(total)

# radius = 5
# pi = 3.14159

# # Area of a circle = pi * radius ** 2
# area = pi * radius**2
# print(f"Area of circle: {area:.2f}")
# # :.2f winds the float point to 2 significant figures


# print(f"Float: {0.1 + 0.2}")


# # Creating complex numbers
# z1 = 3 + 4j
# z2 = complex(2, -1)  # 2 - 1j

# print(f"Z1 real: {z1.real}")  # 3.0 (real part)
# print(f"Z1 Imag: {z1.imag}")  # 4.0 (imaginary part)
# print(f"Absolute: {abs(z1)}")  # 5.0 (magnitude)

# Converting from Celsius to Fahrenheit
# °F =(°C × 9 / 5) +32; // 25°C = 77°F

# Converting from Fahrenheit to Celsius
# °C = 5 / 9 x (°F − 32) // 100F = 37.78°C

user_temp = input("Which temperature are you converting to? C for Celsius or F for Fahrenheit: ")
user_temp = user_temp.upper()

while not user_temp or user_temp != "C" and user_temp != "F":
    if not user_temp:
        print("Entry cannot be empty.")
    elif user_temp != "C" and user_temp != "F":
        print("You must choose C for Celsius and F for Fahrenheit")
    else:
        if user_temp == "C":
            print("Finding the temperature in Celsius")
            temperature = input("What is the temperature in Fahrenheit: ")
            if not temperature.isdigit():
                print("Entry must be a valid number.")
            else:
                temperature = float(temperature)
                celsius = ((5 / 9) * (temperature - 32))
                print(f"The temperature is {celsius}°C")
        else:
            print("Finding the temperature in Fahrenheit")
            temperature = input("What is the temperature in Celsius: ")
            if not temperature.isdigit():
                print("Entry must be a valid number.")
            else:
                temperature = float(temperature)
                fahrenheit = ((temperature * 9 / 5) + 32)
                print(f"The temperature is {fahrenheit}°F")
    user_temp = input(
        "Which temperature are you converting to? C for Celsius or F for Fahrenheit: ")
    user_temp = user_temp.upper()