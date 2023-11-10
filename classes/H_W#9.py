"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
"""


class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize a restaurant_name and a cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describing a restaurant."""
        print(f"Restaurant name is {self.restaurant_name.title()}.")
        print(f"Restaurant cuisine is {self.cuisine_type.title()}.")

    def open_restaurant(self):
        """Indication of the restaurant."""
        print(f"The {self.restaurant_name.title()} restaurant is open!")


rest = Restaurant('asia', 'japanise')
print(f"Rest name is {rest.restaurant_name.title()}, it is {rest.cuisine_type.title()} cuisine!")
rest.describe_restaurant()
rest.open_restaurant()

"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""

my_rest = Restaurant('avar', 'dagestani')
my_rest.describe_restaurant()
bro_rest = Restaurant('samarcand', 'uzbek')
bro_rest.describe_restaurant()
sis_rest = Restaurant('iran', 'persian')
sis_rest.describe_restaurant()

"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user
"""


class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def describe_user(self):
        print(f"The summary of info: {self.first_name.title()}, {self.last_name.title()}, {self.email}, {self.password}")

    def called_greet_user(self):
        print(f"Welcome, {self.first_name.title()} {self.last_name.title()}!")


jose = User('jose', 'rodriges', 'jorod@gmail.com', 'jor')
jose.describe_user()
jose.called_greet_user()
mike = User('michael', 'chush', 'mich@gmail.com', 'mich')
mike.describe_user()
mike.called_greet_user()


"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a
day of business.
"""

class Restaurant:
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize a restaurant_name and a cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describing a restaurant."""
        print(f"Restaurant name is {self.restaurant_name.title()}.")
        print(f"Restaurant cuisine is {self.cuisine_type.title()}.")

    def open_restaurant(self):
        """Indication of the restaurant."""
        print(f"The {self.restaurant_name.title()} restaurant is open!")

    def set_number_served(self):
        print(f"The number of customers that have been served: {self.number_served}")

    def increment_number_served(self, guests):
        self.number_served += guests


rest = Restaurant('asia', 'japanise')
print(f"Rest name is {rest.restaurant_name.title()}")
print(f"Number of people served: {rest.number_served}")
rest.number_served = 5
print(f"Number of people served after chenching: {rest.number_served}")
rest.set_number_served()
rest.increment_number_served(3)
print(f"The number of customers who’ve been served a day: {rest.number_served}")

"""
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""

class User:
    def __init__(self, first_name, last_name, email, password, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.login_attempts = int(login_attempts)

    def increment_login_attempts(self, attempts=1):
        self.att = self.login_attempts + attempts
        print(self.att)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)

    def describe_user(self):
        print(f"The summary of info: {self.first_name.title()}, {self.last_name.title()}, {self.email}, {self.password}, {self.login_attempts}")

    def called_greet_user(self):
        print(f"Welcome, {self.first_name.title()} {self.last_name.title()}!")


user1 = User('jose', 'rodriges', 'jorod@gmail.com', 'jor', '5')
user1.increment_login_attempts()
user1.reset_login_attempts()

"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
"""

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['punch', 'orange', 'cherry']

    def display_flavors(self):
        print('The flavors we have today:', self.flavors)

ice = IceCreamStand('gold', 'turkish')
print(ice.flavors)
ice.describe_restaurant()
ice.display_flavors()

"""
9-7. Admin: An administrator is a special kind of user. Write a class called 
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) 
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list 
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of 
privileges. Create an instance of Admin, and call your method
"""

class Admin(User):
    def __init__(self, first_name, last_name, email, password, login_attempts ):
        super().__init__(first_name, last_name, email, password, login_attempts)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(self.privileges)

adm = Admin('zaMir', 'zaKiev', 'zaza@gmail.com', 'mirkiev', '7')
adm.describe_user()
adm.show_privileges()

