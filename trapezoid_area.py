# this program calculates the area of a trapezoid
print("This program calculates the area of the trapezoid")

# gathering user input
trap_height = float(input("Enter the height of the trapezoid: "))
first_base = float(input("Enter the length of bottom base: "))
second_base = float(input("Enter the length of the top side: "))

# calculating area
trap_area = 1 / 2 * (first_base + second_base) * trap_height

# printing area
print("The area of the trapezoid is:", trap_area)