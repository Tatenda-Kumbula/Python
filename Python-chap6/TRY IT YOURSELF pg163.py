
python_glossary={
  'dictionary':'a collection of key-value pairs',
  'loop':'a set of code that repeats until/for as long as a condition is met',
  'list':'a collection of values assinged to a single key',
  'variable':'a single key-value pair',
  'print':'displays the sprcified text to the user'
  }
print(f"Dictionary=\n\t#{python_glossary['Dictionary']}\n")
print(f"Loop=\n\t#{python_glossary['Loop']}\n")
print(f"list=\n\t#{python_glossary['list']}\n")
print(f"Variable=\n\t#{python_glossary['Variable']}\n")
print(f" Print=\n\t#{python_glossary['Print']}\n")

 
#6-5

for River in Major_Rivers.items():
	print(f"The{River.title()}River runs through{Major_Rivers.title()}.")

for River in Major_Rivers.keys():
	print(River.title())

for River in Major_Rivers.values():
	print(River.title())


#6-6. Polling


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
'tatenda':'c',
'jerry':'ruby',
}

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")


for name in sorted(favorite_languages.values()):
	print(f"{name.title()}, thank you for taking the poll.")



