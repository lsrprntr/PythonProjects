#classes are categorical objects
#classes are objects
#def are the the methods
class Fruit:
    #all local variables
    #__init__ is where we initialize attributes
    #self is reserved
    def __init__(self, name, clr): #parameters to assign attributes
        self.name = name
        self.colour = clr
    def details(self):
        print("my"+self.name+"is"+self.colour)


class PartyAnimal:
    x=0
    def __init__(self,parama):
        self.test=parama
        print("i am constructed")
    def party(self):
        print("test")
        self.x=self.x+1
        print("so far",self.x,self.test)
    def __del__(self):
        print("i am destructed,", self.x)

apple = Fruit("apple", "red")
banana = Fruit("banana","yellow")

print(apple)
apple.details()

an=PartyAnimal("blah")
an.party()
an.party()
print(an.x)
