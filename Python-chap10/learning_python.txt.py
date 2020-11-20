#10.1

filename = 'Learning_python.txt'

with open (filename) as file_object:
	lines = file_object.read()
print(lines)

with open (filename) as file_object:
	for line in file_object
		print files


filename = 'Learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())


#10.2


filename = 'Learning_python.txt'

with open (filename) as file_object:	
	for line in file_object:
	line =line.replace('python','C')
	print(line)	