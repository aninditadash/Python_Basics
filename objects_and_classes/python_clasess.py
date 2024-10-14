# Access modifiers set the accessibility of classes, methods and other members in object-oriented languages.
# They facilitate encapsulation of the components
# 3 types of access modifiers in Python
# Public access modifiers, Protected access modifiers, Private access modifiers
# Public access modifiers    => public data members of a class can be accessed from any part of the program, all
# data members and member functions are public by default.
# Protected access modifiers => protected members are only accessible to a class derived from it, data members are
# declared protected by adding _ symbol before the data member.
# Private access modifiers   => private members are only accessible within the class and are declared by adding __
# before the data member.

class Student:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.counter += 1
        self._roll_number = "A2024/{}/{:003d}".format(self.name[:3].upper(), Student.counter)
        self.__file_number = "A2024/{}/{:003d}".format(self.name.upper(), Student.counter)

    def print_student_details(self):
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Roll Number : {self._roll_number}")
        print(f"File Number : {self.__file_number}")

john = Student("John Doe", 10)
john.print_student_details()

class Science(Student):
    def display(self):
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Roll Number : {self._roll_number}")
        print(f"File Number : {self.__file_number}")

john_science = Science("John Davis", 15)
john_science.print_student_details()
# We get AttributeError in below code
john_science.display()  # Error for self.__file_number as it is a derived class and cant access private variables
