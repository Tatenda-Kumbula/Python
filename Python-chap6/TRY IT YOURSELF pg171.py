
#6-7. People
aeinstein= {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		}
mcurie= {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		}
tkumbula={
		'first':'tatenda',
		'last':'kumbula',
		'location':'jhb',
		}
skhosi={
		'first':'siya',
		'last':'khosi',
		'location':'cpt',
		}
people=[aeinstein,mcurie,tkumbula,skhosi]

for person in people:
	print(f"first name:{person['first'].title()}")
	print(f"last name:{person['last'].title()}")
	print(f"location:{person['location'].title()}")
	print('\n')

#6-8. Pets:

pet_1= {
		'owners_name': 'albert',
		'pet': 'parrot',
		
		}
pet_2= {
		'owners_name': 'marie',
		'pet': 'snake',
		
		}
pet_3={
		'owners_name':'tatenda',
		'pet':'dog',
		
		}
pet_4={
		'owners_name':'siya',
		'pet':'cat',
		
		}

pet=[pet_1,pet_2,pet_3,pet_4]

for pet in pet:
	print(f"owners_name:{pet['owners_name'].title()}")
	print(f"pet:{pet['pet'].title()}")
	print('\n')


#6-9. Favorite Places


favorite_places={'Tatenda':'London,Paris',
	'Jerry':'Dubai,Paris',
	'Tom':'NYC,California'
	}
for name,places in favorite_places.items():
		print(f"Name:{name.title()}")
		print(f"Places:{places}")
		print('\n')


#6-10. Favorite Numbers

favorite_numbers = {
'jen': 78,
'sarah': 9,
'edward': 8,
'phil': 23,
'tom': 1
}

for favorite_numbers in favorite_numbers.items():
		print(f"Name:{name.title()}")
		print(f"Places:{places}")
		print('\n')



#6-11. Cities:
cities={
	'Durban':{
			'country':'South Africa',
			'population':21_500_000,
			'fact':'it was found a long time ago.',
			},
	'Pretoria':{
			'country':'South Africa',
			'population':21_500_000,
			'fact':'it was found a long time ago.',
			},
	'Lusaka':{
			'country':'Zambia',
			'population':1_500_000,
			'fact':'it was found a long time ago.',
			},
		}	

for city, info in cities.items():
	print(f"\nCity:	{city}")
	print(f"\tPopulation:	{info['population']}")
	print(f"\tFun fact: {info['population']}")


#6-12. Extensions:

favorite_languages = {
'jen': ['python','ruby'],
'sarah': ['c',]
'edward': ['ruby','c'],
'phil': ['python'],
}

for name,languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite_languages are:)