#9-4
class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
    
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
       
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
      
        self.number_served = number_served

    def increment_number_served(self, additional_served):
      
        self.number_served += additional_served


restaurant = Restaurant('the top', 'pizza')
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 430
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(1257)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(239)
print(f"Number served: {restaurant.number_served}")

#9-5

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

tatenda = User('tatenda', 'kumbula', 't_kumbula', 't_kumbula@example.com', 'alaska')
tatenda.describe_user()
tatenda.greet_user()

print("\nMaking 3 login attempts...")
tatenda.increment_login_attempts()
tatenda.increment_login_attempts()
tatenda.increment_login_attempts()
print(f"  Login attempts: {tatenda.login_attempts}")

print("Resetting login attempts...")
tatenda.reset_login_attempts()
print(f"  Login attempts: {tatenda.login_attempts}")
