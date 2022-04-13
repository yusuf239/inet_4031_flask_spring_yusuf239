# inspiration code for Python Unit Testing Project

import math

def surfaceArea(rad):
    surfaceArea = 4 * math.pi * rad * rad
    return surfaceArea

def volume(rad):
    volume = 4/3 * math.pi * rad * rad * rad

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME AND SURFACE AREA OF SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius :"))
    
    print("\nThe Volume of a Sphere = ", volume(radius))
    print("\nThe Surface Area of a Sphere = ", surfaceArea(radius))

if __name__ == '__main__':
    prompt()
