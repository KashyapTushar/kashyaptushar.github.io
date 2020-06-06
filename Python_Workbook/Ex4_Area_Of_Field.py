# Exercise 4:Area of a Field


def area_of_field():
    # Read input from the user
    length = float(input("enter length of the field in feet:"))
    width = float(input("enter width of the field in feet:"))
    acre_to_feet = 43560
    area = (length * width) / acre_to_feet
    print("Area of the field  is :", area)


area_of_field()    
