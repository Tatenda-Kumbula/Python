#4.10
players=['Tatenda','Morty','Rick','Micheal','Ali']
print(F"The first three items in the are:{players[:3]}")
print(F"three items from the middle of the list are:{players[1:4]}")
print(F"The last three items in the list are :{players[-3]}")

#4.11
pizzas=['BBQ Chicken','pepperoni','hawaiian']
friend_pizzas=pizzas[:]

pizzas.append('ribs')
friend_pizzas.append('vegetarian')

print("My favorite pizzas are:")
for p in pizzas:
	print(p)

print("\nMy friend's favorite pizzas are:")
for fp in friend_pizzas:
	print(fp)

#4.12

my_foods=['pizza','burger','beef']
friend_foods=my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for mf in my_foods:
	print(mf)

print("\nMy friend's favorite foods are:")
for fp in friend_foods:
	print(friend_foods)
