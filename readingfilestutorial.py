# SHORTCUTS -> CTL+ALT+N = run code in output, right click run code in terminal
# Tutorial https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3
path = 'c:/users\daeme\OneDrive\Desktop\Personal Projects\Python_basics\days.txt'
# line 1 specify the path, I have already created this file and adding some stuff in the file, just like in the tutorial

days_file = open(path, 'r')
'''line 4 set a variable and calls the open () function and pass in the path
variable I created above, the r is a mode and is used for reading'''

days = days_file.read()
# print(days)
# line 10 & 11 i created a variable that reads the file and pass it in the print funtion

'''days = days_file.readline()
# readline will return whats in the first line only, but if i call it again it will then return the second line

days = days_file.readlines()
# readlines return a list of the lines in a file where each item are all on one line'''

# idk why this worked but remember to add \\ infront of the file name when creating a path
new_path = 'C:/Users\daeme\OneDrive\Desktop\Personal Projects\Python_basics\\new_days.txt'
new_days = open(new_path, 'w')  # W is the writing mode
title = 'Days of the Week\n'  # \n is how you create a line break
new_days.write(title)  # writing title to the new_days file
print(title)  # printing it

new_days.write(days)  # writing days variable to the file as well
print(days)  # printing it

days_file.close()
new_days.close()  # Always remeber to close the files
