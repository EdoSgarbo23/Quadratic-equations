# 31/01/2025 Created by: Sgarby bro

# This program is a quadratic equation solver
import math
print("Insert a quadratic equation: ")
print("The quadratic equation has to be in the form ax^2 + bx + c = 0 ")
print("Insert a: ")
a = float(input())
print("Insert b: ")
b = float(input())
print("Insert c: ")
c = float(input())

print("Your equation is: ", a, "x^2 + ", b, "x + ", c)

print("Calculating Δ: ")
delta = b * b - 4 * a * c
print("Δ = ", delta)

if delta >= 0 :  
    print("Calculating solutions: ")
    x_1 = (-b + delta)/ (2 * a)
    x_2 = (-b - delta)/ (2 * a)

    if x_1 == x_2:
        print("This equation has two equal solutions: ")
        print("x = ", x_1)
    else :
        print("This equation has two different solutions: ")
        print("x = ", x_1)
        print("x = ", x_2)
else : 
    print("This equation has not a real solution! ")
    print("This is because Delta < 0")

# This program was created using python. It is a simple calculator of solutions of a quadratic equation using the quadratic formula.
# I have created this program to solve an everyday struggle in school hope you enjoy using this simple calculator as much as i do :)
# Remember to not use this tool to cheat on math tests (wink wink) ;)
