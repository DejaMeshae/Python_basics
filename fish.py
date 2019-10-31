class Fish:

     # def is at the start of a method, it defines a method
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


class Trout(Fish):  # this is the child class, notice I pass in the parent class
    pass

    # the pass keyword defaults the parent methods meaning I dont have to declare it again
terry = Trout("Terry")
print(terry.first_name + " " + terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.swim_backwards()
# We created a Trout object that uses the methods from the fish class even though we did not define the methods in this class
# We only needed to pass the value of Terry to the first_name variable
# Then run the code CTL + ALT + N
