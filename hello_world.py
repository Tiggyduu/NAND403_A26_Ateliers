import sys

a = "string"

print(a)

this_is_a_variable = 1 # OK

thisIsAVariable = 1 # NOT OK

def myWrongFunction(): # WRONG
    print("Wrong!")

def my_good_function(): # OK
    print("Good!")