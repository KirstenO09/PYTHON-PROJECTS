Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
4
4
+ 5
5
4
4
num1 = 4
num1
4
type(num1)
<class 'int'>
num2 = 5
num2
5
type(num2)
<class 'int'>
num3 = num1 + num2
num3
9

================================ RESTART: Shell ================================
num1 = 1
num2 = 2


print(num1 + num2)
3
num1 = 1.2
num2 = 2.1
print(num1 + num2)
3.3

================================ RESTART: Shell ================================
myString = "hello world"
myString
'hello world'
len(myString)
11
myString[0]
'h'
myString[1]
'e'
fName = "Kirsten"
lName = "Osborne"
print(fName + lName)
KirstenOsborne
print(fName + " " + lName)
Kirsten Osborne
print("Hello {} {}, welcome to Python!".format(fName,lName))
Hello Kirsten Osborne, welcome to Python!

== RESTART: D:/Python/Tech Academy Python files/String_Variable_Challenges.py ==
multi
6
STRING
strip
True
Hello World!
The "Lions" is Detroit's football mascot.

================================ RESTART: Shell ================================
num1 = 1.2
num2 = 2.1
num1 = "one"
print(num1 + num2)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(num1 + num2)
TypeError: can only concatenate str (not "float") to str
num1 = "1"
print(num1 + num2)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(num1 + num2)
TypeError: can only concatenate str (not "float") to str
print(int(num1) + num2)
3.1

====== RESTART: D:/Python/Tech Academy Python files/Operators_Challenge.py =====
5
7
True
False
False
True
2

================================ RESTART: Shell ================================
myList = [2,3,4]
len(myList)
3
for i in myList:
    print(i)

2
3
4
myList[2]
4
myList[0]
2
myList.append(5)
for i in myList:
    print(i)

2
3
4
5
len(myList)
4
print(myList)
[2, 3, 4, 5]

======== RESTART: D:/Python/Tech Academy Python files/List_Challenge.py ========
apple
banana
orange
lemon
strawberry
['apple', 'banana', 'orange', 'lemon', 'strawberry', 'pineapple', 'spinach', 'broccoli', 'carrots', 'Peas', 'Corn']
['strawberry', 'spinach', 'pineapple', 'orange', 'lemon', 'carrots', 'broccoli', 'banana', 'apple', 'Peas', 'Corn']

============================ RESTART: D:/Python/Tech Academy Python files/Tuples_Challenge.py ===========================
Traceback (most recent call last):
  File "D:/Python/Tech Academy Python files/Tuples_Challenge.py", line 1, in <module>
    myTuple = (red, red, blue, green, pink, red, blue, purple, purple, orange)
NameError: name 'red' is not defined

============================ RESTART: D:/Python/Tech Academy Python files/Tuples_Challenge.py ===========================
red
red
blue
green
pink
red
blue
purple
purple
orange
3

============================= RESTART: D:/Python/Tech Academy Python files/Sets_Challenge.py ============================
{'football', 'swimming'}

============================= RESTART: D:/Python/Tech Academy Python files/Sets_Challenge.py ============================
{'volleyball', 'basketball', 'soccer', 'football', 'baseball', 'hockey'}
{'volleyball', 'basketball', 'soccer', 'baseball', 'gymnastics', 'track'}
{'volleyball', 'basketball', 'soccer', 'swimming', 'football', 'baseball', 'hockey'}
{'volleyball', 'basketball', 'soccer', 'swimming', 'football', 'baseball'}
{'football', 'swimming'}

===================================================== RESTART: Shell ====================================================
myDictionary = {'index1': 1,'index2': 2, 'index3': 355}
myDictionary
{'index1': 1, 'index2': 2, 'index3': 355}
myDictionary{'index2'}
SyntaxError: invalid syntax
myDictionary['index2']
2
dic_users = {'em_1234': {'fname': 'Bob', 'lname': 'Smith', 'phone': '123-456-7890'}, 'em_1235': {'fname': 'Mary', 'lname': 'Jones', 'phone': '152-364-5764'}}
print(dic_users['em_1235'])
{'fname': 'Mary', 'lname': 'Jones', 'phone': '152-364-5764'}
print(dic_users['em_1235']['phone'])
152-364-5764
print('User: {} {}\nPhone: {}'.format(dic_users['em_1235']['fname'],dic_users['em_1235']['lname'], dic_users['em_1235']['phone']))
User: Mary Jones
Phone: 152-364-5764

===================================================== RESTART: Shell ====================================================
i = 0
for i in range(10):
    print("{} iteration through the loop.".format(i))
    i += 1

0 iteration through the loop.
1 iteration through the loop.
2 iteration through the loop.
3 iteration through the loop.
4 iteration through the loop.
5 iteration through the loop.
6 iteration through the loop.
7 iteration through the loop.
8 iteration through the loop.
9 iteration through the loop.
i = 0
while i < 10:
    print("{} iteration through the loop.".format(i))
    i += 1

0 iteration through the loop.
1 iteration through the loop.
2 iteration through the loop.
3 iteration through the loop.
4 iteration through the loop.
5 iteration through the loop.
6 iteration through the loop.
7 iteration through the loop.
8 iteration through the loop.
9 iteration through the loop.

=============================== RESTART: D:/Python/Tech Academy Python files/Functions.py ===============================
I love the color red
I love the color blue
I love the color green
I love the color pink
I love the color teal
I love the color black
>>> 
=============================== RESTART: D:/Python/Tech Academy Python files/Functions.py ===============================
KIRSTEN loves the color red
KIRSTEN loves the color blue
KIRSTEN loves the color green
KIRSTEN loves the color pink
KIRSTEN loves the color teal
KIRSTEN loves the color black
>>> 
=============================== RESTART: D:/Python/Tech Academy Python files/Functions.py ===============================
KIRSTEN loves the color black
>>> 
=============================== RESTART: D:/Python/Tech Academy Python files/Functions.py ===============================
KIRSTEN loves the color red
KIRSTEN loves the color blue
KIRSTEN loves the color green
KIRSTEN loves the color pink
KIRSTEN loves the color teal
KIRSTEN loves the color black
>>> go = True
>>> 
========================== RESTART: D:/Python/Tech Academy Python files/Functions_and_Loops.py ==========================
What is your name? Bob
Bob loves the color red
Bob loves the color blue
Bob loves the color green
Bob loves the color pink
Bob loves the color teal
Bob loves the color black
>>> 
========================== RESTART: D:/Python/Tech Academy Python files/Functions_and_Loops.py ==========================
What is your name? Sally
Sally, you may not use this software
