#4-3. Counting to Twenty:

numbers = list(range(1, 21))
print(numbers)

#4-4. One Million
numbers = list(range(1, 1000001))
#print(numbers)

#4-5. Summing a Million:


digits = range(1,1000001)
print(min(digits))
print(max(digits))
print(sum(digits))


#4-6. Odd Numbers:
odd_numbers = list(range(1,20,2))
print(odd_numbers)

#4-7. Threes:
multiples=list(range(3,31,3))
for multiple in multiples:
	print(multiple)

#4-8. Cubes
Cubes = [value**3 for value in range(1,11)]
for Cube in Cubes:
	print(Cubes)

#4-9. Cube Comprehension:

cubes=[value**3 for value in range(1,11)]
print(cubes)