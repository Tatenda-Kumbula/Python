#10-3
name = input("What's your name? ")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)

#10-4
filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
        print(f"Hi {name}, you've been added to the guest book.")

 #10-5
 filename = 'programming_poll.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")