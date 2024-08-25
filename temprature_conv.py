def convert_temperature(temperature, unit):
  """Converts temperature between Celsius and Fahrenheit.

  Args:
    temperature: The temperature value to convert.
    unit: The unit of measurement for the temperature (either "C" or "F").

  Returns:
    The converted temperature value.
  """

  if unit == "C":
    fahrenheit = (temperature * 9/5) + 32
    return fahrenheit
  elif unit == "F":
    celsius = (temperature - 32) * 5/9
    return celsius
  else:
    return "Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit."

if __name__ == "__main__":
  temperature = float(input("Enter the temperature value: "))
  unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ")
  converted_temperature = convert_temperature(temperature, unit)
  print("Converted temperature:", converted_temperature)