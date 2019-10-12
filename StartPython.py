'''print("Deja")
CLT + ALT + N can also run your code'''

'''students_count = 1000
print(students_count)

name = "Deja"
print(len(name))

print(name[0])  # To get a certain index
print(name[0:3])'''  # slice a string

'''first = "deja"
last = "ameringer"
full = f"{first} {last}"  # formatted string but still a lil confused
print(full)

# dotnotation methods
print(full.title())  # capatizle the first letter
print(full.strip())  # to remove white space'''

'''x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")
# the above take in an input (x) then adds 1 to to it'''

# not sure what import means yet but below is how to get an input and return a repsonse
'''import datetime
now = datetime.datetime.now()
x = input("Type okay to ask Siri what is the date and time:")
print("The current date and time is: ")
print(now.strftime("%b-%d-%Y %H:%M"))'''
# datetime.now() to get current date and time. Then strftime() method creates a string representing date and time in another format

# Tuples are similar to lists but they are immutable - which means they cannot be changed after creation
import this
my_tuple = ("Deja", "Ameringer", 27, "Associate Engineer")
print(my_tuple)

# Dictionaries are a type of associative array (an object) implemented using hash tables containing key/value pairs. They are unordered.
my_dict = {"Key 1": "Value 1", "name": "Deja Ameringer", "pi": 3.14}
print(my_dict["name"])
# key being name and its value is Deja Ameringer
