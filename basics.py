#Installing pip 
# $apt install python3-pip

#Libraries & packages
#module - .py file
#package -collection of modules, package must contain init.py file
#library -collection of packages

#Including numers in strings:
print(f"20 days are {20*24*60} minutes") #f means format, doesn't work in python 2x

#User input
user_input = int(input("How many days you want to calculate?"))

#Defining functions
#Parameters - variables inside function.
#Void -empty functions - they don't return any values (value 'None')
#Hermatisation - packing portion of code in fukction. Generalization - adding a parameter to the function.
def days_to_seconds (value):
    return print(f"{value} days are {value * 24 * 60 * 60} seconds ") #function may not return anything, it can print text only
    
days_to_seconds(user_input)

#If-else conditionals
if 2>1:
    print("Do something.")       #return may be used
elif 2<1:
    print("Do this.")
else:
    print("Do this.")

#Try-except
    try:
        print('Someting')

    except (ValueError):
        print('Error.')

#Lists:
#list[""]

#Sets:
""" Like a list, but without duplicates.
Cannot use index of elements."""
#set{""}

#Dictionaries:

import os

print(os.name)

#For loop works on lists, so we always must use range() function for iterating. Range starts at 0, and ends with last number-1!  

#Classes always have a __init__() function (constructor), that is executed automaticly whenever we create the object from this class.
#Self is a reference to the current instance of the class.
#functions that belongs to the class are called Methods.


'''
Użyte w warunku wartości 0, 0.0 i '' (pusty ciąg tekstowy) są uznawane za False, podczas gdy wszystkie pozostałe są uznawane za True.

Poleceń break  i  continue  można  używać  także  w  pętli for.  Polecenie  continue będzie  kontynuowało  działanie  od  następnej  wartości  licznika  pętli for,  jakby nastąpiło  wykonanie  całej  iteracji  pętli  i  przejście  z  powrotem  na  jej  początek.


# Przyklad przerwania

print("Instrukcja przerwania:")
for i in range(1, 6):
    if i == 3:
        break
    print("Wewnatrz petli.", i)
print("Poza petla.")


# Przyklad wznawiania

print("\nInstrukcja wznowienia:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Wewnatrz petli.", i)
print("Poza petla.")
'''