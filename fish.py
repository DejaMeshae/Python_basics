# Following this Tutorial: https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3


class Fish:

     # def is at the start of a method, it defines a method, I think __init__ means initilized
    def __init__(self, first_name, last_name="Fish",
                 skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print('This fish is swimming.')

    def swim_backwards(self):
        print("The fish can swim backwards.")
        # added 2 methods that prints a statement, all sub classes will also have these methods


'''class Trout(Fish):  # this is the child class, notice I pass in the parent class
    pass



# the pass keyword defaults the parent methods meaning I dont have to declare it again
# This is me passing in the name of the fish so everytime I call Terry it will inherite the Trout methods
terry = Trout("Terry") 

print(terry.first_name + " " + terry.last_name)  
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.swim_backwards()
# We created a Trout object that uses the methods from the fish class even though we did not define the methods in this class
# We only needed to pass the value of Terry to the first_name variable
# Then run the code CTL + ALT + N'''
# I commented out lines 27-38 because below I am using that same class to show how to use the super() function


# these lines of code below uses the super() function, we are calling a parent method into a child method to change it, we added freshwater but this also still included all of the other parent methods
class Trout(Fish):
    def __init__(self, water="freshwater"):
        self.water = water
        super().__init__(self)
# Because im using the Super method above to alter the __init__ methos from the parent class


terry = Trout()
terry.first_name = "Terry"
# Because I have overridden the method, I no longer need to pass first_name in as a parameter to Trout like in the above Trout class, if I did pass in a parameter, we would reset freshwater instead I will therefore initialize the first_name by calling the variable in our object instance.
terry.first_name = "Terry"  # this line initilize first name
print(terry.first_name + " " + terry.last_name)
print(terry.eyelids)  # lines 54 and 55 use parent __intit__() through super()

print(terry.water)  # Use child __init__() override
terry.swim()  # Use parent swim() method
# then run code to excute lines 43-58


class Clownfish(Fish):
    def live_with_anemone(self):
        print("The clownfish is co existing with sea anemone.")


    # creating a method
casey = Clownfish("Casey")
print(casey.first_name + " " + casey.last_name)
casey.swim()
casey.live_with_anemone()
# Notice live_with_anemone() only applies to the class as that method is only apart of this class
# Also take note that live_with_anemone() won't with another class


class Shark(Fish):
    def __init__(self, first_name, last_name='Shark',
                 skeleton='cartilage', eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")
# In the Shark class we have over written the initialized parameters by changing the last_name and cartilage string and eyelids to equal true
# Also overrode the swim_backwards method


sammy = Shark("Sammy")
print(sammy.first_name + " " + sammy.last_name)
sammy.swim()
sammy.swim_backwards()
print(sammy.eyelids)
print(sammy.skeleton)
# overrode the __init__() and swim_backwards() (lines 50-58) also inheriting the swim() method from the parent class
