# Following this Tutorial: https://www.digitalocean.com/community/tutorials/understanding-class-inheritance-in-python-3
# This is to show how to use multiple inheritance


class Coral:
    def community(self):
        print("Coral lives in a community.")


class Anemone:
    def protect_clownfish(self):
        print("The anemone is protecting the clownfish.")


# Notice this class uses pass with will inheritance all methods from BOTH of the class
class CoralReef(Coral, Anemone):
    pass
