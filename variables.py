# Python variables
# Variables are containers for storing data values.
# Unlike other programming languages, Python has no command for declaring a variable.

x = 5
y = "John"
print(x, y)


# Variables do not need to be declared with any particular type and can even change type after they have been set.

age = 19 # age is of type int
Name = "Tobenna" # x is now of type str
print(age, Name)


#Assign Value to Multiple Variables
#Python allows you to assign values to multiple variables in one line:

name, Age, level = "Tobenna", 19, 300
print("Student Info:" + "Name:", name,  "Age:", Age, "Level:", level)




# Global Variables
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.


Student_name = "Tobenna" #This is a global variable

def myfunc():
  print("My name is " + Student_name)

myfunc()


# Create a variable inside a function, with the same name as the global variable

New_name = "Tedd-Austin"

def myfunc():
  New_name = "Pascal"
  print("My new name is " + New_name)

myfunc()

print("My new name is " + New_name)


#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

#To create a global variable inside a function, you can use the global keyword.

#Create a variable inside a function, with the same name as the global variable

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)