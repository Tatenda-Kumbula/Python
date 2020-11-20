Guests=['Tatenda','Ruben','Caylem','Juan']

print(f'Evening {Guests[0].title()},you are being invited for dinner .')

print(f'Evening {Guests[1].title()},you are being invited for dinner .')

print(f'Evening  {Guests[2].title()},you are being invited for dinner ')

print(f'Evening {Guests[3].title()},you are being invited for dinner ')


#3.5

print(f'{Guests[3].title()},sorry to dissapoint you but i can nto make it to dinner ')

del Guests[3]

print(f'Evening {Guests[0].title()},you are still being invited for dinner .')

print(f'Evening {Guests[1].title()},you are still being invited for dinner .')

print(f'Evening  {Guests[2].title()},you are still being invited for dinner ')



#3.6

Guests.insert(0,'Courtney')

Guests.insert(2,'Tom')

Guests.append('Huey')


print(f'{Guests[0].title()}, i have found a bigger dinner table .')

print(f'{Guests[1].title()},i have found a bigger dinner table .')

print(f'{Guests[2].title()},i have found a bigger dinner table ')

print(f'{Guests[3].title()},i have found a bigger dinner table ')

print(f'{Guests[4].title()},i have found a bigger dinner table ')

print(f'{Guests[5].title()},i have found a bigger dinner table ')


print(f'Good morning {Guests[0].title()},you are hereby invited to dine with on Sunday .')

#3.7

message='Im truely sorry to inform you that i can only invite two people only'
print(message)

pop1=Guests.pop()
print(f"Sorry {pop1} you are not invited anymore")

pop2=Guests.pop()
print(f"Sorry {pop2} you are not invited anymore")

pop3=Guests.pop()
print(f"Sorry {pop3} you are not invited anymore")

pop4=Guests.pop()
print(f"Sorry {pop4} you are not invited anymore")

print(f"{Guests[0]} Still invited")
print(f"{Guests[1]} Still invited")

del Guests[1]
del Guests[0]

print(Guests)