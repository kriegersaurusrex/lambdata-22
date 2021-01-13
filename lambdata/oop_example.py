"""OOP Examples - 312"""

import pandas as import pd

class MyDataFrame(pd.DataFrame):
    def num_cells(self):
        return self.shape[0] * self.shape[1] #Return number of cells in dataframe
        



class BareMinimumClass:
    pass 

class Complex:
    def __init__(self, real_part, imag_part):
        """
        Constructor for Complex Numbers.
        Complex Numbers have a real part and an imaginary part.
        """
        self.r = real_part
        self.i = imag_part

    def add(self, other_complex):
        #Adding num2: num1.r+num2.r and num1.i+num2.i
        self.r += other_complex.r
        self.i += other_complex.i
        
    def __repr__(self):
        return "({}, {})".format(num1.r, num1.i)

class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)
    
    def receive_upvotes(self, num_upvotes=1):
        #default 1 if no upvotes passed
        self.upvotes += num_upvotes
    
    def is_popular(self):
        #if upvotes > 100, then it'll be true with boolean return
        return self.upvotes > 100

class Animal:
    """General representation of animals"""
    def __init__(self, name, weight, diet_type):
        #Constructors
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type
    #Methods
    def run(self):
        return "Vroom, Vroom, I go quick"

    def eat(self, food):
        return "Huge fan of that " + food

class Sloth(Animal):
    def __init__(self, name, weight, diet_type, num_naps=104):
        super().__init__(name, weight, diet_type)
        self.num_naps = float(num_naps)

        #Constructors
        #self.name = str(name)
        #self.weight = float(weight)
        #self.diet_type = diet_type
    def run(self):
        return "I am a slow guy"
    def eat(self):
        return "I like leaves2"
    def say_something(self):
        return "Sloth of typing"

if __name__ == "__main__":
    num1 = Complex(3, -5)
    num1.r # returns real part, 3
    num1.i # return imag part, -5
    num2 = Complex(2,6)
    num1.add(num2)
    print("num1.r: {}, num2.r: {}".format(num1.r, num1.i))

    user1 = SocialMediaUser("John", "LA", 500)
    user2 = SocialMediaUser("Carl", "Mississippi")
    user3 = SocialMediaUser("George Washington", "", 4000)
    user4 = SocialMediaUser("Carlos", "Argentina", 5)

    print(user1.is_popular())
    print(user2.is_popular())
    user2.receive_upvotes(101)
    print("received X number of upvotes".format(user2.upvotes))
    print(user2.is_popular())

