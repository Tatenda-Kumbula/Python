#9-1
class Restaurant():
   

    def __init__(self, name, cuisine_type):
       
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

restaurant = Restaurant('the top', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)


#9-2

class Restaurant():
    

    def __init__(self, name, cuisine_type):
        
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
     
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

the_top = Restaurant('the top', 'pizza')
the_top.describe_restaurant()

Bros = Restaurant("Bro's bistro", 'seafood')
Bros.describe_restaurant()

mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restaurant()

#9-3

class User():
    

    def __init__(self, first_name, last_name, username, email, location):
       
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
       
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        
        print(f"\nWelcome back, {self.username}!")

tatenda = User('tatenda', 'kumbula', 't_kumbula', 't_kumbula@example.com', 'alaska')
tatenda.describe_user()
tatenda.greet_user()

willie = User('willie', 'kross', 'williekross', 'wb@example.com', 'alaska')
willie.describe_user()
willie.greet_user()