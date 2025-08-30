while True:
    user_temp = input("Convert to (C/F) or Q to quit: ").strip().upper()

    # 1) Exit option
    if user_temp == "Q":
        print("Goodbye!")
        break

    # 2) Basic validation for the choice
    if not user_temp:
        print("Entry cannot be empty.")
        continue
    # if user_temp != "C" and user_temp != "F"
    if user_temp not in ("C", "F"):
        print("You must choose C for Celsius or F for Fahrenheit.")
        continue

    # 3) Do the conversion
    if user_temp == "C":
        raw = input("Temperature in Fahrenheit: ").strip()
        try:
            f = float(raw)  # accepts integers and decimals (e.g., 98.6)
        except ValueError:
            print("Entry must be a valid number.")
            continue
        c = (5 / 9) * (f - 32)
        print(f"{f:.2f}°F = {c:.2f}°C")

    else:  # user_temp == "F"
        raw = input("Temperature in Celsius: ").strip()
        try:
            c = float(raw)
        except ValueError:
            print("Entry must be a valid number.")
            continue
        f = (c * 9 / 5) + 32
        print(f"{c:.2f}°C = {f:.2f}°F")

    print()  # blank line for readability
