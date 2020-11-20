#9-10
from admin import Admin
from user import Admin
from restaurant import Restaurant

class Restaurant():

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
    
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        
        self.number_served = number_served

    def increment_number_served(self, additional_served):
    
        self.number_served += additional_served
my_restaurant.py:



channel_club = Restaurant('the channel club', 'steak and seafood')
channel_club.describe_restaurant()
channel_club.open_restaurant()

#9-11

class User():

    def __init__(self, first_name, last_name, username, email, location):
        
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
    
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
       
        self.login_attempts += 1

    def reset_login_attempts(self):
   
        self.login_attempts = 0


class Admin(User):
    

    def __init__(self, first_name, last_name, username, email, location):
       
        super().__init__(first_name, last_name, username, email, location)
 
        self.privileges = Privileges()


class Privileges():
 

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")



tatenda = Admin('tatenda', 'kumbula', 't_kumbula', 't_kumbula@example.com', 'alaska')
tatenda.describe_user()

tatenda_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
tatenda.privileges.privileges = eric_privileges

print(f"\nThe admin {eric.username} has these privileges: ")
tatenda.privileges.show_privileges()

#9-12
class User():
 

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
     
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):

        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):

        self.login_attempts += 1

    def reset_login_attempts(self):

        self.login_attempts = 0


class Admin(User):


    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)
        
        # Initialize an empty set of privileges.
        self.privileges = Privileges()


class Privileges():
 

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")


  

tatenda = Admin('tatenda', 'kumbula', 't_kumbula', 't_kumbula@example.com', 'alaska')
tatenda.describe_user()

tatenda_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
tatenda.privileges.privileges = eric_privileges

print(f"\nThe admin {tatenda.username} has these privileges: ")
tatenda.privileges.show_privileges()