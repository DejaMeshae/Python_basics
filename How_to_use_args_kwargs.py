# following this tutorial https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3
# With *args you can create more flexible code that accepts a varied amount of non-keyworded arguments within your function

'''def multiply(x, y):
    print(x, y)  # line 2 and 3 is a typical method that takes in 2 arguments


# in line 7, I call the method and pass in 2 argument and run code I get "12" as 3*4=12
multiply(3, 4)'''
# multiply(3, 4, 7) #if I try to pass in 3 arguments i will get an error as only 2 can be passed in
# So if i need to use more than 2 arugments I use args


'''def multiply(*args):
    z = 1
    for num in args:
        z *= num
    print(z)


multiply(4, 5)
multiply(10, 9)
multiply(2, 3, 4)
multiply(3, 5, 10, 6)'''
# lines 14-24 so now when I run the code the muliply method takes in multiple arguments
# lines 14-24 shows the multiply method again put with args and a for loop


# ********understanding **kwargs********


def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)
# lines 32-36 so now when I run the code the print_kwargs method takes in multiple arguments, kwargs we will need to assign keywords like a dictionary
# When this method run notice the ouput may be unordered depending on which version of python 3 im using
