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
    print(get_number())


def get_number():
    number = 12
    return number


if __name__ == "__main__":
    start()
