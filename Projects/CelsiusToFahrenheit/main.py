# Converting from Celsius to Fahrenheit
# °F =(°C × 9 / 5) +32; // 25°C = 77°F

# Converting from Fahrenheit to Celsius
# °C = 5 / 9 x (°F − 32) // 100F = 37.78°C


# temperature = float(input("What is the temperature in Celsius "))
# fahrenheit = ((temperature * (9 / 5)) + 32)
# print(f"The temperature is {fahrenheit}°F")



temperature = input("What is the temperature in Celsius ")
if temperature.isdigit():
    fahrenheit = (temperature * (9 / 5)) + 32
    print(f"The temperature is {fahrenheit}°F")
else:
    temperature = int(temperature)
    fahrenheit = (temperature * (9 / 5)) + 32
    print(f"The temperature is {fahrenheit}°F")
























# temp_choice = input(
#     "Are you converting to Celsius or Fahrenheit, choose C for Celsius or F for Fahrenheit"
# )
# temperature = None

# if temp_choice == "C" or temp_choice == "c":
#     temperature = float(input("What is the temperature in Celsius "))
#     celsius = (5 / 9 * (temperature - 32))
#     print(f"The temperature is {celsius}°C")

# elif temp_choice == "F" or temp_choice == "f":
#     temperature = float(input("What is the temperature in Celsius "))
#     fahrenheit = ((temperature * (9 / 5)) + 32)

# else:
#     print("Entry not recognized. Ensure you typed either C or F")