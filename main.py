#does a triangle with given sides exist?

side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))
#condition for the triangle to exist is that the sum of any two of its sides is greater than the third
if side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
    print("The triangle with given sides exist")
else:
    print("The triangle with given sides does not exist")

