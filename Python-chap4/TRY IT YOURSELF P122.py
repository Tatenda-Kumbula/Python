my_foods = ['pizza', 'falafel', 'carrot cake','ice cream','burger']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print(f'The first three items in the list are: {my_foods[:3]}')
#print(my_foods[-3:])
print(f'Three items from the middle of the list are: {my_foods[:3]}')
print(f'The last three items in the list are: {my_foods[:3]}')

#4-11. My Pizzas, Your Pizzas

pizzas=['BBQ chicken','pepperoni','hawaiian']
friend_pizzas=pizzas[:]

pizzas.append('rib')
friend_pizzas.append('vegetarian')

print("My favorite pizzas are:")
for p in pizzas:
	print (p)

print("\nMy friends favorite pizzas are:")	
for fp in friend_pizzas:
	print(fp)