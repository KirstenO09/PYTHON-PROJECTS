#
# Python:   3.12
#
# Author:   Kirsten Osborne
#
# Purpose:  The Tech Academy - Python Course, Creating our first program together.
#           Demonstrating how to pass variables from function to function
#           while producing a functional year.
#
#           Remember, funciton_name(variable) _means that we pass in the varable.
#           return variable _means that we are returning the variable back to the
#           calling function.



def start():
    print("Hello {}!".format(get_name()))


def get_name():
    name = input("What is your name? ") 
    return name


if __name__ == "__main__":
    start()
