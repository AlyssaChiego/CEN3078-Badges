#---------------------------------------------------------
# File: main.py
# Author(s): Alyssa Chiego
# Class: CEN 3078 Y5S2 2023 : Computer Security
# Purpose: adds two numbers given by the user together
# Audit: 3.25.25 AC
#---------------------------------------------------------

num1 = input("Please enter a number: ")
num2 = input("Please enter another number: ")

if num1 > 0 and num2 > 0:
    print(num1 + num2)
else:
    print("Input not valid.")