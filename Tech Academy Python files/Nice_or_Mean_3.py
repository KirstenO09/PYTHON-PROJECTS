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
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "Female"
    get_info(f_name,l_name,age,gender)


def get_info():
    print("My name is {} {}. I am {} yearold {}.".format(f_name,l_name,age,gender))

if __name__ == "__main__":
    start()
