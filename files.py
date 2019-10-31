# SHORTCUTS -> CTL+ALT+N = run code in output, right click run code in terminal

path = 'c:/users\daeme\OneDrive\Desktop\Personal Projects\Python_basics\days.txt'
# line 1 specify the path

days_file = open(path, 'r')
'''line 4 set a variable and calls the open () function and pass in the path
variable I created above, the r is a mode and is used for reading'''

days = days_file.read()
print(days)
# line 10 & 11 i created a variable that reads the file and pass it in the print funtion

'''days = days_file.readline()
# readline will return whats in the first line only, but if i call it again it will then return the second line

days = days_file.readlines()
# readlines return a list of the lines in a file where each item are all on one line'''

title = 'Days of the Week\n'
new_path = 'c:/users\daeme\OneDrive\Desktop\Personal Projects\Python_basics\new_days.txt'
new_days = open(new_path, 'W')


'''f = open("c:\VSStuff//delete.txt", "a")
# line 12 open/create a file to this path (I can change the path if i want, this path I got from the video and I created a VSStuff folder)
# Then I can go to this temp file and open it up and sure enough my delete.txt file is there!

f.write("Did this work? ")
# line15 writes this to the file using dot notation (.write)
# lines 12-this one I got from the how to open and read from a files saved in python bookmarks on chrome
f.close()

fname = "c:\VSStuff//delete.txt"
count = 0
with open(fname, 'r') as f:
    for line in f:
        count += 1
print("Total number of lines is:", count)
# Lines 20-this one is how to count the lines in a file

with open("c:\VSStuff//delete.txt", 'r') as f:
    f_contents = f.read()
    print(f_contents)'''
