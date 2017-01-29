print("""
This program takes temperature in(°F)
  and returns temperature in(°C)
""")
# gathering user input and converting into float
fahrenheight_temp = float(input("Enter temperature in (°F): "))

# converting from fahrenheight to celsius
celsius_conversion = (fahrenheight_temp - 32) * 5 / 9

# degree
degree = "°"

# printing output
print("The temperature in (°C) is: ", degree + str(celsius_conversion))

