

# Temperature conversion
temperature = input("Enter the temperature value: ")
if not temperature.replace('.', '', 1).isdigit():
    print("Invalid temperature value. Please enter a valid number.")
else:
    temperature = float(temperature)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit not in ['C', 'F']:
        print("Invalid unit of measurement. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    else:
        if unit == 'C':
            converted_temperature = (temperature * 9/5) + 32
            print(f"{temperature}°C is equivalent to {converted_temperature:.2f}°F.")
        else:
            converted_temperature = (temperature - 32) * 5/9
            print(f"{temperature}°F is equivalent to {converted_temperature:.2f}°C.")