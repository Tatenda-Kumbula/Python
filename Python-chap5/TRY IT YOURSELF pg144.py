#5-8

usernames = ['tatenda', 'willie', 'admin', 'tom', 'jerry']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for loggin in again!")


#5-9

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for loggin in again!")
else:
    print("We need to find some users!")

 #5-10
current_users = ['tatenda', 'willie', 'admin', 'tom', 'jerry']
new_users = ['sarah', 'Willie', 'PHIL', 'tom', 'jerry']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")

#5-11
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")