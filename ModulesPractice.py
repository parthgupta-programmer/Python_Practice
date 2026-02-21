# Lesson 5.1: Importing Modules

#  Assignment 1: Importing and Using Modules
# Import the `math` module and use it to calculate the square root of 25 and the sine of 90 degrees.

# import math
# print(math.sqrt(25),math.sin(math.radians(90)))

# Assignment 2: Aliasing Modules
# Import the `datetime` module with an alias and use it to print the current date and time.

# import datetime as dt
# now=dt.datetime.now()
# print(now.date(), now.time())

# Assignment 3: Importing Specific Functions
# Import the `randint` function from the `random` module and use it to generate a random integer between 1 and 100.

# from random import randint
# print(randint(1,100))

# Assignment 4: Importing Multiple Functions
# Import the `sqrt` and `pow` functions from the `math` module and use them to calculate the square root of 16 and 2 raised to the power of 3.

# from math import sqrt,pow
# print(sqrt(16),pow(2,3))

#  Assignment 5: Handling Import Errors
# Write code that attempts to import a non-existent module and gracefully handles the import error by printing an error message.

# try:
#     import library
# except(Exception):
#     print("Module does not exist !!")
# finally:
#     print("Module error handled successfully!!")

# Lesson 5.2: Standard Library Overview

# Assignment 6: Working with the `os` Module
# Use the `os` module to create a new directory, list the contents of the current directory, and remove the newly created directory.

# import os
# os.mkdir('New_Directory')
# print(os.listdir())
# os.rmdir('New_Directory')

# if not os.path.exists('New_Directory'):
#     os.mkdir('New_Directory')

# Prevents error if folder already exists.

# Assignment 7: Working with the `sys` Module
# Use the `sys` module to print the Python version currently in use and the command-line arguments passed to the script.

# import sys
# print(sys.version,sys.argv)


# Assignment 8: Working with the `math` Module
# Use the `math` module to calculate the greatest common divisor (GCD) of two numbers and the factorial of a number.

# import math
# print(math.gcd(4,12),math.factorial(5))

# Assignment 9: Working with the `datetime` Module
# Use the `datetime` module to print the current date, calculate the date 100 days from today, and determine the day of the week for a given date.

# import datetime as dt
# now=dt.datetime.now()
# given_date=dt.datetime.strptime('1956-08-19',"%Y-%m-%d") # strptime() converts string to datetime
# print(now.date(),now.date()+dt.timedelta(days=100),given_date.strftime("%A")) # strftime("%A") gives day name

# Assignment 10: Working with the `random` Module
# Use the `random` module to generate a list of 5 random numbers between 1 and 50 and shuffle the elements of a list.

# import random
# l=[]
# for i in range(5):
#     l.append(random.randint(1,50))
# random.shuffle(l)
# print(l)

# Cleaner Version

# import random

# l = [random.randint(1,50) for _ in range(5)]
# random.shuffle(l)
# print(l)




