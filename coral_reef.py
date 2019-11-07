# Following this Tutorial: https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3
# This is to show how to use multiple inheritance as well as single inferitance and overriding inheritance


class Coral:
    def community(self):
        print("Coral lives in a community.")


class Anemone:
    def protect_clownfish(self):
        print("The anemone is protecting the clownfish.")


# Notice this class uses pass with will inheritance all methods from BOTH of the class
# this line is also called a Tuple which what i've gathered so far means 2 things
class CoralReef(Coral, Anemone):
    pass


great_barrier = CoralReef()  # The object great_barrier is set as a CoralReef object
great_barrier.community()
great_barrier.protect_clownfish()
# then run code, the object great_barrier object of the coralreef class inherite both methods in both parent classes thus showing how to use multiple inheritances
