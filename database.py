#!/usr/bin/python3
"""
This Module deifines the Connection to the db.
I am connecting this rn with a text file that will hold the data
Each Data entry in it's own line
The dunctions defined here will be called from the income module.
"""


from fileinput import filename

# from income import Income
Income = __import__('income').Income

def write_income():
    """writes to a utf-8 encoded text file
    """

    print("\n\nIncome here")

    Source = input("Where is the amount From: ")
    Amount = input("Enter Amount: ")

    # Call the class income
    income = Income(Source, Amount)

    print(income.Source)

   

    # Have a Method in the class income to check if Source is valid 

    income.verifySource()


   
    # Check if user enters correct Amount



    with open('filename.txt', 'a', encoding='utf-8') as myFile:
        return myFile.writelines(Source) , myFile.write(Amount)



def read_database():
    """
    The Method reads the contents of the file and print them on the 
    Terminal
    """

    with open('filename.txt', 'r', encoding='utf-8') as myFile:
        print("\n\n", myFile.read())