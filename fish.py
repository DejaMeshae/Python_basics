class Fish:
    # def is at the start of a method, it defines a method
    def __init__(self, first_name, last_name="Fish"):
        self.first_name = first_name
        self.last_name = last_name

    def swim(self):
        print('This fish is swimming.')

    def swim_backwards(self):
        print("The fish can swim backwards.")
