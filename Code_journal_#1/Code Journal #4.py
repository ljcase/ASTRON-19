
class Dog: # sets the classs to a dog
    def __init__(self,length_of_arms, length_of_legs, number_of_eyes, has_a_tail, Is_furry):
        self.length_of_arms = length_of_arms
        self.length_of_legs = length_of_legs
        self.number_of_eyes = number_of_eyes
        self.has_a_tail = has_a_tail
        self.Is_furry = Is_furry
    
    def describe(self):
        print(f"This is a dog with")
        print(f"arms that are {self.length_of_arms}in")
        print(f"legs that are {self.length_of_legs}in")
        print(f"it has {self.number_of_eyes} eyes")
        print(f"and a huge tail {self.has_a_tail}" if self.has_a_tail else "and a huge tail")
        print(f"Is_furry: {self.Is_furry}" if self.Is_furry else "But is not furry")

my_dog = Dog(5.0,5.0,10,False,False)

my_dog.describe()