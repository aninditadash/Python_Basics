# Four concepts of Object-Oriented Programming => Encapsulation, Inheritance, Polymorphism, Abstraction
# Object represents an entity in real world that can be distinctly identified. It consists of the following components:
# 1) Identity  => gives unique name to the object
# 2) State     => reflects the properties of an object (attributes)
# 3) Behaviour => reflects the response of an object to other objects  (instance methods)
# A class is a blueprint for an object, defines objects that share the same properties and methods
# A class can be like an object constructor for creating objects.
# Instantiating objects => creation of objects or instances of a given class.

# In Python, __init__ is a method automatically called when memory is allocated to a new object. In the init method,
# the self refers to the newly created object. Default arguments can be used in constructor.
# In other methods, self refers to the instance whose method was called.

# In python, it's not necessary to explicitly delete an object after use. It has automatic Garbage Collection.
# The classes do not have any destructor methods.

# Types of Attributes in Python => Data attributes (instance attributes) and Class attributes.
# Data attributes  => owned by a particular instance of class, each instance has its value, the init method creates
# and initialises the variables, they are referred inside the class using the self keyword.
# Class attributes => class is the owner, it's a variable shared by all instances of a class, also known as static in
# other languages, used to build class wise constants and object counters.

class Demo:
    pass

obj = Demo()
print(obj)
help(obj)

print("================================================================================")

class ShoppingCart:
    """
    This is class Shopping Cart having information and methods related to the shopping cart added by the user
    """
    # class attribute
    counter = 0

    def __init__(self, user_id: str, user_name: str, products_list: list) -> None:
        """
        Initialisation of the Shopping Cart
        :param user_id:
        :param user_name:
        :param products_list:
        """
        self.user_id = user_id
        self.user_name = user_name
        self.products_list = products_list
        ShoppingCart.counter += 1

    def display_cart(self):
        print(f"Hi {self.user_name}, your shopping cart contains below items: ")
        for key, value in self.products_list:
            print(f"{key}: {value}")
        print(f"No. of Shopping carts: {ShoppingCart.counter}")


shopping_cart_1 = ShoppingCart("1", "John Doe", [
    ("Electronics", "Phillips Hair Dryer"),
    ("Electronics", "Havells Wet Iron"),
    ("Groceries", "Apple")
])
shopping_cart_1.display_cart()
print(f"shopping_cart_1.user_id = {shopping_cart_1.user_id}\nshopping_cart_1.user_name = {shopping_cart_1.user_name}\n")

shopping_cart_2 = ShoppingCart("2", "Jane Doe", [
    ("Beauty", "Essence Mascara Lash Princess"),
    ("Beauty", "Eyeshadow Palette with Mirror"),
    ("Beauty", "Lakhme Moisturizer"),
    ("Groceries", "Apple")
])
shopping_cart_2.display_cart()
print(f"shopping_cart_2.user_id = {shopping_cart_2.user_id}\nshopping_cart_2.user_name = {shopping_cart_2.user_name}\n")

print(shopping_cart_1.counter, shopping_cart_2.counter)

print(f"shopping_cart_1.user_name is shopping_cart_2.user_name = "
      f"{shopping_cart_1.user_name is shopping_cart_2.user_name}")

print(f"shopping_cart_1.counter is shopping_cart_2.counter = {shopping_cart_1.counter is shopping_cart_2.counter}")
