# - Calculate your age based on the current year and your birth year

# currentYear = input("Enter current year: ")
# birthYear = input("Enter birth year: ")


def calculateAge(currentYear:int,birthYear:int):
    age:int = currentYear - birthYear
    return print("My Age is :",age)



#  - Write a program that calculates the area of a rectangle using length and width variables.


def calculateRectangleArea(length:float,width:float):
    area:float = length * width
    return print("Area of Rectangle: " ,area)


#  - Write a program that calculates the area of a circle.

def CalculateCircleArea(radius:float):
    pi:float = 3.14
    area:float = pi * radius**2
    return print("Area of Circle: ",area)


#  - Write a program that calculates the area of the cube. formula = 6a**2


def calculateCubeArea(surfaceArea:float):
    area:float = 6 * surfaceArea**2
    print("Area of Cube: ",area)


#  - Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.

def convert_temperature(temperature: int):
    celsius = (temperature - 32) * 5 / 9
    fahrenheit = (temperature * 9 / 5) + 32
    print("Temperature in Celsius:", celsius)
    print("Temperature in Fahrenheit:", fahrenheit)



#  - Convert a given number of seconds into minutes and seconds using variables.
def convert_seconds(total_seconds):
    minutes = total_seconds // 60  
    seconds = total_seconds % 60   
    
    print( f"{minutes} minutes and {seconds} seconds")


#  - Write a program that calculates the percentage.



def calculatePercentage(value:float,totalValue:float):
    percentageValue = value * 100 / totalValue
    print("Percentage Value: ",percentageValue)



# - Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)
    
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")
    
    return bmi


# - Write a program that calculates the volume of a cylinder using the formula .


def calcualateCubeVolume(a:int):
    volumeCube:int = a ** 3
    print("Volume of Cube: ",volumeCube)
    


# Function calls
print(calculateAge(2024,2001))
print ("---------------------------------------")


calculateRectangleArea(10,4)
print ("---------------------------------------")


CalculateCircleArea(2)
print ("---------------------------------------")


calculateCubeArea(6)
print ("---------------------------------------")


calculatePercentage(997,1100)
print ("---------------------------------------")


calculate_bmi(80, 2)
print ("---------------------------------------")

convert_temperature(100)
print ("---------------------------------------")

convert_seconds(60)
print ("---------------------------------------")

calcualateCubeVolume(10)
print ("---------------------------------------")







