# Inheritance is the process of forming a new class from an existing or base class. 4 types of inheritance:
# Single level inheritance => a class can inherit from only one class
# Multiple inheritance     => a class can inherit from more than one class
# Multilevel inheritance   => a derived class is created from another derived class
# Hierarchical inheritance => a base class can have multiple subclasses inherited from it (create multiple derived
# classes from same base class)

# Single level inheritance
class ParentClass:
    def parent(self):
        print("Parent Class")

class ChildClass(ParentClass):
    def child(self):
        print("Child Class")

child1 = ChildClass()
child1.parent()
child1.child()

print("================================================================================")

# Multilevel inheritance
class ChildClass1(ParentClass):
    def child_1(self):
        print("Child Class")

class ChildClass2(ChildClass1):
    def child_2(self):
        print("Child Class")

child2 = ChildClass2()
child2.parent()
child2.child_1()
child2.child_2()

print("================================================================================")

# Multiple inheritance
class Parent1Class:
    def parent_1(self):
        print("Parent1 Class")

class Parent2Class:
    def parent_2(self):
        print("Parent2 Class")

class ChildMulti(Parent1Class, Parent2Class):
    def child_multi_fn(self):
        print("ChildMulti Class")

child_multi = ChildMulti()
child_multi.parent_1()
child_multi.parent_2()
child_multi.child_multi_fn()

# Hierarchical inheritance
class ParentHClass:
    def parent(self):
        print("Parent Class")

class ChildHClass1(ParentHClass):
    def child_h1(self):
        print("Child Class")


class ChildHClass2(ParentHClass):
    def child_h2(self):
        print("Child Class")

child_h1 = ChildHClass1()
child_h2 = ChildHClass2()
child_h1.parent()
child_h1.child_h1()
child_h2.parent()
child_h2.child_h2()
