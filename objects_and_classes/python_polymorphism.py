# Polymorphism => Ability of a message to be displayed in more than one form. Has 2 types -
# Compile time => also called static or early binding polymorphism, it is resolved at compile time.
# Run time     => also dynamic or late binding polymorphism, function is resolved at runtime.
# Compile time => Method overloading and Operator overloading
# Run time     => Method Overriding
# Method overloading   => Multiple functions with the same name in a class, but different signatures.
# Operator overloading => Overload the operator to provide some extra functionality.
# Method Overriding    => allows a derived class to provide specific implementation for a method that is already
# provided by the parent class

# Python does not support Compile Time Polymorphism. Here, 2 classes can have functions with the same name but with
# different parameters, and that's now method overloading can be implemented.

# Method Overloading
class Information:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_info(self):
        print(f"Name          : {self.name}")
        print(f"Age           : {self.age}")
        print(f"Gender        : {self.gender}")

class Learner:
    def __init__(self, name, age, gender, experience, qualification):
        self.name = name
        self.age = age
        self.gender = gender
        self.experience = experience
        self.qualification = qualification

    def print_info(self):
        print(f"Name          : {self.name}")
        print(f"Age           : {self.age}")
        print(f"Gender        : {self.gender}")
        print(f"Experience    : {self.experience}")
        print(f"Qualification : {self.qualification}")

informationObj = Information("John Doe", 30, "M")
learnerObj = Learner("John Doe", 30, "M", 5, "Graduate")
informationObj.print_info()
learnerObj.print_info()

print("================================================================================")

# Operator Overloading
firstName = 'Dave'
lastName = 'Travolta'
concatenated_str = firstName + ' ' + lastName       # '+' operator is overloaded
print(f"concatenated_str = {concatenated_str}")

print("================================================================================")

# Method Overriding
class Learners(Information):
    def __init__(self, name, age, gender, experience, qualification):
        Information.__init__(self, name, age, gender)
        self.experience = experience
        self.qualification = qualification

    def print_info(self):
        """
        print_info function of child class is overriding the print_info function of parent class.
        To use the print_info function of parent class, the function needs to be invoked explicitly.
        """
        Information.print_info(self)
        print(f"Experience    : {self.experience}")
        print(f"Qualification : {self.qualification}")

learnersObj = Learners("John Doe", 30, "M", 5, "Graduate")
learnersObj.print_info()    # Calls the print_info of child class
