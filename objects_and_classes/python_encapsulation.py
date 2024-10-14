# Encapsulation is the process of binding data members and member functions into a single unit.
# It hides the state of a structured data object inside the class, preventing unauthorised access
# It acts as a protective barrier that restricts direct access to variables and methods i.e. (data hiding)

class Encapsulation:
    def __init__(self, a, b, c):
        self.public = a
        self._protected = b
        self.__private = c

