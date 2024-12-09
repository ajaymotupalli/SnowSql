# To read a file : 

f = open("D:\SnowFlake\Python_Prac\HelloEveyone.txt", "r")
print(f.read())

# (OR) We can read CSV files also :

f = open("D:\SnowFlake\Python_Prac\Book1.csv", "r")
print(f.read())

# --------------------------------------------------------
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

f = open("D:\SnowFlake\Python_Prac\HelloEveyone.txt", "r")
print(f.read(5))

# --------------------------------------------------------

# To read a file line by line:

f = open("D:\SnowFlake\Python_Prac\HelloEveyone.txt", "r")
print(f.readline())

# --------------------------------------------------------

# By looping through the lines of the file, you can read the whole file, line by line :

f = open("D:\SnowFlake\Python_Prac\HelloEveyone.txt", "r")
for line in f:
   print(line)

# --------------------------------------------------------

# It is a good practice to always close the file when you are done with it.

f = open("D:\SnowFlake\Python_Prac\HelloEveyone.txt", "r")
print(f.readline())
f.close()

# --------------------------------------------------------

# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

# Example :- Open the file "D:\SnowFlake\Python_Prac\HelloEveyone.txt" and append content to the file :

# f = open("D:\SnowFlake\Python_Prac\HelloEveyone.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# open and read the file after the appending:
f = open("D:\SnowFlake\Python_Prac\HelloEveyone.txt", "r")
print(f.read())

# --------------------------------------------------------

# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:

# Example :- Remove the file "D:\SnowFlake\Python_Prac\HelloEveyone.txt.txt":

import os
os.remove("D:\SnowFlake\Python_Prac\HelloEveyone.txt")

# --------------------------------------------------------

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

# Example:- Check if file exists, then delete it:

import os
if os.path.exists("D:\SnowFlake\Python_Prac\HelloEveyone.txt"):
  os.remove("D:\SnowFlake\Python_Prac\HelloEveyone.txt")
else:
  print("The file does not exist")

# --------------------------------------------------------

# Delete Folder
# To delete an entire folder, use the os.rmdir() method:

# Example:- Remove the folder "myfolder":

import os
os.rmdir("myfolder")

# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------

# CSV (Comma Separated Values) format is the most common import and export format for spreadsheets and databases. 
# It is one of the most common methods for exchanging data between applications and popular data format used in Data Science. 
# It is supported by a wide range of applications. 
# A CSV file stores tabular data in which each data field is separated by a delimiter(comma in most cases).
# To represent a CSV file, it must be saved with the .csv file extension.

# Reading and Writing CSV Files in Python

# Reading FROM CSV Files in Python

# Syntax:    csv.reader(csvfile, dialect='excel', **fmtparams)

import csv

with open("D:\SnowFlake\Python_Prac\Book1.csv", mode= "r") as file :
    csvfile = csv.reader(file)
    for row in csvfile :
        print(row)

# (OR)

import pandas as pd 

f = pd.read_csv("D:\SnowFlake\Python_Prac\Book2.csv")
print(f)

# --------------------------------------------------------

# Writing TO CSV Files in Python

# Syntax:    csv.writer(csvfile, dialect='excel', **fmtparams)

import csv 

columns = ["NAME","AGE","BLOOD GROUP"]
rows = [["AJAY","25","O+"],["SRINU","24","A+"],["RAVI","21","B-"],["SUBBU","22","AB+"]]

filename = "D:\SnowFlake\Python_Prac\Book2.csv"

with open(filename, mode = "w") as fileName :
    filewriter = csv.writer(fileName)
    filewriter.writerow(columns)
    filewriter.writerows(rows)

# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------

# Python RegEx

# LINK (https://www.w3schools.com/python/python_regex.asp)

#     A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

#     RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module
#     Python has a built-in package called re, which can be used to work with Regular Expressions.

# Note:(Import the re module:)

# RegEx in Python
#   When you have imported the re module, you can start using regular expressions:

# Example:  Search the string to see if it starts with "The" and ends with "Spain":

import re

    #Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

# --------------------------------------------------------

# RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match:

# Function	Description
# 1)findall	Returns a list containing all matches
# 2)search    Returns a Match object if there is a match anywhere in the string
# 3)split	    Returns a list where the string has been split at each match
# 4)sub       Replaces one or many matches with a string

# --------------------------------------------------------

# 1) The findall() Function
# The findall() function returns a list containing all matches.

# Example
# Print a list of all matches:

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
# The list contains the matches in the order they are found.

# If no matches are found, an empty list is returned:

# Example:  Return an empty list if no match was found:

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

# --------------------------------------------------------

# 2) The search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.

# If there is more than one match, only the first occurrence of the match will be returned:

# Example:   Search for the first white-space character in the string:

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


# If no matches are found, the value None is returned:

# Example:   Make a search that returns no match:

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

# --------------------------------------------------------

# 3) The split() Function
# The split() function returns a list where the string has been split at each match:

# Example:   Split at each white-space character:

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# You can control the number of occurrences by specifying the maxsplit parameter:

# Example:   Split the string only at the first occurrence:

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# --------------------------------------------------------

# 4) The sub() Function
# The sub() function replaces the matches with the text of your choice:

# Example:   Replace every white-space character with the number 9:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


# You can control the number of replacements by specifying the count parameter:

# Example:   Replace the first 2 occurrences:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------

# LAMBDA FUNCTIONS :/

# Python Lambda

#     A lambda function is a small anonymous function.

#     A lambda function can take any number of arguments, but can only have one expression.

# Syntax:-     lambda arguments : expression

# The expression is executed and the result is returned:

# Example:   Add 10 to argument a, and return the result:

x = lambda a : a + 10
print(x(5))

# --------------------------------------------------------

# Lambda functions can take any number of arguments:

# Example:   Multiply argument a with argument b and return the result:

x = lambda a, b : a * b
print(x(5, 6))

# --------------------------------------------------------

# Example:   Summarize argument a, b, and c and return the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# --------------------------------------------------------

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
  return lambda a : a * n

# --------------------------------------------------------

# Use that function definition to make a function that always doubles the number you send in:

# Example

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# --------------------------------------------------------

# Or, use the same function definition to make both functions, in the same program:

# Example

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------


# Decorators in Python

# Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. 
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. 
# But before diving deep into decorators let us understand some concepts that will come in handy in learning the decorators.

# First Class Objects

# In Python, functions are first class objects which means that functions in Python can be used or passed as arguments.

# Properties of first class functions:
    
# A function is an instance of the Object type.
# You can store the function in a variable.
# You can pass the function as a parameter to another function.
# You can return the function from a function.
# You can store them in data structures such as hash tables, lists, …

# Consider the below examples for better understanding.

# Example 1: Treating the functions as objects. 


def shout(text): 
    return text.upper() 
print(shout('Hello')) 
yell = shout 
print(yell('Hello'))

# Output:

# HELLO
# HELLO

# In the above example, we have assigned the function shout to a variable. 
# This will not call the function instead it takes the function object referenced by a shout and creates a second name pointing to it, yell.

# --------------------------------------------------------

# Nested Function
# We can include one function inside another, known as a nested function. For example,

def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(6)
print(result)

# Output: 11
# Here, we have created the inner() function inside the outer() function.

# --------------------------------------------------------

# Pass Function as Argument
# We can pass a function as an argument to another function in Python. For Example,

def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 4, 6)
print(result)

# Output: 10

# --------------------------------------------------------