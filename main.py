#!/usr/bin/python3
"""
  
"""

from database import *

print("================== Welcome to the CashTracker System ==================")
print("=== V1.01===")


while (1):
    print("1. ADD INCOME")
    print("2. ADD EXPENDITURE")
    print("3. VIEW DATA")
    input = input("What do you wanna do: ")


    # Test for selection input


if (int(input) == 1):
    # Call the class add income for the object income to be creates
    # Pass income as arguement

    print("Income to be being added")

    write_income()
    

elif(int(input) == 2):
    # call class add expenditure
    # Pass income as arguement

    print("Expenditure to be added")

elif(int(input) == 3):
    # This will prompt the view to be used

    print("\nHere is your data")

    read_database()

else:
    print("You enterd the wrong thing")