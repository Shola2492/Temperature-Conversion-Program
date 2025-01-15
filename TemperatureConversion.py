unit = input("Is the temperature in celcius or Fahrenheit (C or F): ")
temp = float(input("Enter your temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 2)
    print(f"The temperature in Fahrenheit is: {temp} ")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 2)
    print (f"The temperature in celcius is: {temp}")
else:
    print(f"{unit} is an invalid unit of measurement")
    