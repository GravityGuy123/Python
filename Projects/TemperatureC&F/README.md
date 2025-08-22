# Temperature Converter (Python)

A simple Python program that converts temperatures between **Celsius (°C)** and **Fahrenheit (°F)**.  
The program runs in a loop, allows multiple conversions, validates input, and supports an **exit option**.

---

## 🚀 Features
- Convert **Fahrenheit → Celsius**.
- Convert **Celsius → Fahrenheit**.
- Handles integers and decimals (e.g., `100`, `36.6`, `-40`).
- Input validation (rejects empty or non-numeric entries).
- Option to quit anytime by typing **Q**.

---

## 📖 Usage

1. Run the program:
   ```bash
   python converter.py
   ```

2. Follow the prompt:
   - Type **C** to convert *Fahrenheit → Celsius*.
   - Type **F** to convert *Celsius → Fahrenheit*.
   - Type **Q** to quit.

3. Example interaction:
   ```
   Convert to (C/F) or Q to quit: C
   Temperature in Fahrenheit: 98.6
   98.60°F = 37.00°C

   Convert to (C/F) or Q to quit: F
   Temperature in Celsius: 0
   0.00°C = 32.00°F

   Convert to (C/F) or Q to quit: Q
   Goodbye!
   ```

---

## 📝 Code Overview

- **Main loop:** Runs continuously until the user types `Q`.
- **Validation:** Ensures input is not empty, must be `C`, `F`, or `Q`.
- **Conversion formulas:**
  - Celsius = `(5/9) * (Fahrenheit - 32)`
  - Fahrenheit = `(Celsius * 9/5) + 32`
- **Error handling:** Uses `try/except` so non-numeric inputs don’t crash the program.

---

## 📂 File Structure
```
converter.py   # Main program file
README.md      # Documentation
```

---

## ✅ Requirements
- Python 3.x installed on your system.

---

## 💡 Future Improvements
- Add support for Kelvin conversion.
- Provide option for one-time conversion without loop.
- Add GUI for easier use.

---
