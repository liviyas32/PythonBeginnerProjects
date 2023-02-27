
"""Program for a simple Calculator that performs addition, substraction, multiplication, division, square, cube, cuberoot, inverse, power, square root"""
import functools
import math
import time
import os

# defining a function for performing addition operation
def addition():
    add = lambda x,y : x+y
    num = list(map(float, input("Enter the numbers seperated by space for addition: ").split()))
    Sum = functools.reduce(add,num)
    return Sum


# defining a function for performing subtraction operation
def subtraction():
   sub = lambda x,y : x-y
   ans = list(map(float,input("Enter the numbers separated by space for subtraction: ").split()))
   subtract = functools.reduce(sub,ans)
   return subtract


# defining a function for performing multiplication operation
def multiplication():
    mul = lambda x,y : x*y
    multi = list(map(float,input("Enter the numbers separated by space for multiplication: ").split()))
    func = functools.reduce(mul,multi)
    return func


# defining a function for performing division operation
def division():
    div = lambda x,y : x/y
    val = list(map(float,input("Enter the numbers separated by space for division: ").split()))
    divis = functools.reduce(div,val)
    return divis

# defining a function for performing square operation
def square():
    sq = lambda x : x**2
    value = list(map(float,input("Enter the numbers separated by space for to return square: ").split()))
    answer = list(map(sq,value))
    return answer

# defining a function for performing square root operation
def square_root():
    sqr = lambda x : math.sqrt(x)
    values = list(map(float,input("Enter the numbers separated by space for to return square root: ").split()))
    answers = list(map(sqr,values))
    return answers

# defining a function for performing power operation
def power():
    numb1 = float(input("Enter first number to return power: "))
    numb2 = float(input("Enter second number to return power: "))
    soln = pow(numb1,numb2)
    return soln


# defining a function for performing cube operation
def cube():
    cubes = lambda x : x**3
    number = list(map(float,input("Enter the numbers separated by space for to return cube: ").split()))
    solution = list(map(cubes,number))
    return solution


# defining a function for performing inverse operation
def inverse():
    inv = lambda x : 1/x
    numbers = list(map(float,input("Enter the numbers separated by space for to return inverse: ").split()))
    solutions = list(map(inv,numbers))
    return solutions

# defining a function for performing cuberoot operation
def cube_root():
    cuberoot = lambda x : x**(1/3)
    cube_numbers = list(map(float,input("Enter the numbers separated by space for to return cube root: ").split()))
    cube_solutions = list(map(cuberoot,cube_numbers))
    return cube_solutions

# defining a function for performing exit operation
def exit():
    Exit = "\nThanks for using the calculator.\nExiting now, Bye!"
    return Exit

while True:
    print("\nChoose the operation you want to perform:")
    print("\n\t1 for Addition")
    print("\n\t2 for Subtraction")
    print("\n\t3 for Multiplication")
    print("\n\t4 for Division")
    print("\n\t5 for Square")
    print("\n\t6 for Square root")
    print("\n\t7 for Cube")
    print("\n\t8 for Cube root")
    print("\n\t9 for Power")
    print("\n\t10 for Inverse")
    print("\n\t0 fo Exit")

    operation = int(input("Choose the operation: "))

    if operation == 1:
        sol = addition()
        print("The answer is ",sol)
        time.sleep(2)
        os.system("cls")

    elif operation == 2:
        sol = subtraction()
        print("The answer is ",sol)
        time.sleep(2)
        os.system("cls")

    elif operation == 3:
        sol = multiplication()
        print("The answer is ",sol)
        time.sleep(2)
        os.system("cls")

    elif operation == 4:
        sol = division()
        print("The answer is ",sol)
        time.sleep(2)
        os.system("cls")

    elif operation == 5:
        sol = square()
        print("The answer is ",sol)
        time.sleep(2)
        os.system("cls")

    elif operation == 6:
        sol = square_root()
        print("The answer is ",sol)
        time.sleep(2)
        os.system("cls")

    elif operation == 7:
        sol = cube()
        print("The answer is ",sol)
        time.sleep(2)

    elif operation == 8:
        sol = cube_root()
        print("The answer is ",sol)
        time.sleep(2)
        os.system("cls")

    elif operation == 9:
        sol = power()
        print("The answer is ",sol)
        time.sleep(2)
        os.system("cls")

    elif operation == 10:
        sol = inverse()
        print("The answer is ",sol)
        time.sleep(2)
        os.system("cls")

    elif operation ==0:
        print(exit())
        break

    else:
        print("Sorry!\nYou have chosen invalid operation!\nTry again using correct operation!")
        break

