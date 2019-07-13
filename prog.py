# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 12:41:21 2019

@author: snigd
"""

# program make a simple calculator that can add, subtract, multiply and divide

# this function adds two numbers

def add(x, y):
    return x+y

# This funtion subtracts two numbers
def subtract(x, y):
    return x-y

# This funtion multiplies two numbers
def multiply(x, y):
    return x*y

# This funtion divide two numbers
def divide(x, y):
    return x / y

print("select operation. ")
print("1.ADD")
print("2.Subtract")
print("4.Multiply")
print("5.Divide")

# Take input for the user
choice = input("Enter choice(1/2/3/4):")

num1= int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))
    
elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1, num2))
    
elif choice =='3':
    print(num1, "*",num2,"=", multiply(num1,num2))
    
elif choice =='4':
    print(num1, "*",num2,"=", multiply(num1,num2))
  
else:
    print("Invalid input")
