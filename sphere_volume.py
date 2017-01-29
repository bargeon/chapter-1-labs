# calculate volume of sphere
import random

print("This program calculates the volume of a sphere")

# gathering input
sphere_radius = float(input("Enter the radius of the sphere: "))
pi = 3.14

# calculating the volume of the sphere 
sphere_volume = 4 * (pi * (sphere_radius ** 3) / 3)

# printing the output
print("The volume of the sphere is:", str(sphere_volume) + "in³")