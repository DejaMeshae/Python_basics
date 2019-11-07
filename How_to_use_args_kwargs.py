# following this tutorial https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3
'''def multiply(x, y):
    print(x, y)  # line 2 and 3 is a typical method that takes in 2 arguments


# in line 7, I call the method and pass in 2 argument and run code I get "12" as 3*4=12
multiply(3, 4)'''
# multiply(3, 4, 7) #if I try to pass in 3 arguments i will get an error as only 2 can be passed in
# So if i need to use more than 2 arugments I use args
# lines 10-15 shows the multiply method again put with args and a for loop


def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)


multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)
# lines 13-23 so now when I run the code the muliply method takes in multiple arguments
