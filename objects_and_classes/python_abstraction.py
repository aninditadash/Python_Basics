# Abstraction is the process by which only the essential details are displayed to the user.
# In Python, abstraction works by incorporating abstract classes and methods.
# Abstract class is a class which contains only abstract methods, these methods do not have implementation and all
# implementation is done in the subclasses.
# An abstract class can only be inherited, only an object of derived class can be used to access the features of the
# abstract class.

from abc import abstractmethod, ABC

class Beverage(ABC):
    @abstractmethod
    def ingredients(self):
        print('base')

    @abstractmethod
    def taste(self):
        pass


# Below line gives error
# TypeError: Can't instantiate abstract class Beverage without an implementation for abstract method 'ingredients'
# beverageObj = Beverage()

class MangoShake(Beverage):
    def ingredients(self):
        print("Mango, milk and sugar")

    def taste(self):
        print("Sweet, Sour and yummy!!")


class OrangeJuice(Beverage):
    def ingredients(self):
        print("Orange, Water and sugar")

    def taste(self):
        print("Sweet and yummy!!")

mangoShakeObj = MangoShake()
mangoShakeObj.ingredients()
mangoShakeObj.taste()

orangeJuiceObj = OrangeJuice()
orangeJuiceObj.ingredients()
orangeJuiceObj.taste()
