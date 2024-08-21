# Python lists

# collection type
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
"""


# List

food = ["rice", "egg", "Akara"]
print(food)
print(food[-2])
print(food[1])

# range index

print(food[2:5])

# Since this is a list i can change the value of an item on the list


food[2] = "cake"

print(food[2])
print(food)


# I can also loop through lists using for loop

for x in food:
    print(x)


# sets
"""
Remember that you cannot get access an item in a set by it's index because it is unordered
so the only way is to loop through it

"""

my_names = {"Tobenna", "Pascal"}

for x in my_names:
    print(len(x))

# Dictionaries

# my dictionary

my_details = {
    "name": "Tobenna",
    "age": 19,
    "level": 200,
    "DOB": 2005
}
print(my_details)

print(my_details["name"], my_details["age"])


# loop through the dictionary

for x in my_details:
    # print(my_details[x])  
    print(len(x))  