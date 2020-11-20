#9-6

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


class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type='ice_cream'):
       
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
      
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'blue cherry']

big_one.describe_restaurant()
big_one.show_flavors()


#9-7
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
        self.privileges = []

    def show_privileges(self):
        
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


tatenda = Admin('tatenda', 'kumbula', 't_kumbula', 't_kumbula@example.com', 'alaska')
tatenda.describe_user()

tatenda.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

tatenda.show_privileges()

#9-8

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

tatenda.privileges.show_privileges()

print("\nAdding privileges...")
tatenda_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
tatenda.privileges.privileges = eric_privileges
tatenda.privileges.show_privileges()

#9-9

class Car():
    
    def __init__(self, manufacturer, model, year):
       
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
       
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
      
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
   
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
   
        self.battery_size = battery_size

    def describe_battery(self):
        
        print(f"This car has a {self.battery_size}-kWh battery.")

        
    def get_range(self):
      
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        message = f"This car can go approximately {range}"
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        
        if self.battery_size == 75:
            self.battery_size = 100
            print("Upgraded the battery to 100 kWh.")
        else:
            print("The battery is already upgraded.")
    
        
class ElectricCar(Car):
    
    def __init__(self, manufacturer, model, year):
       
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'roadster', 2019)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()




#9-13

from random import randint
x = randint(1, 6)

from random import randint

class Die():
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
      
        self.sides = sides

    def roll_die(self):
        
        return randint(1, self.sides)


d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)


d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)


d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)


#9-14

from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []
print("Let's see what the winning ticket is...")

#
while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)

    
    if pulled_item not in winning_ticket:
        print(f"  We pulled a {pulled_item}!")
        winning_ticket.append(pulled_item)



#9-15

from random import choice

def get_winning_ticket(possibilities):
    
    winning_ticket = []

    
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

       
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    
    for element in played_ticket:
        if element not in winning_ticket:
            return False

  
    return True

def make_random_ticket(possibilities):
    
    ticket = []
    
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

       
        
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False


max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")

