import math

num = int(input("Input the number of a sides: "))
a = int(input("input the lenght of sides: "))

area = (num * a**2) / (4 * math.tan(math.pi / num))

print("Area:",area)