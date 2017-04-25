# import stuff
import os

phonebook_data = [
	{
		"name": "Melissa",
		"number": "404-235-5428"
	},
	{
		"name": "Joe",
		"number": "404-235-2125"
	},
	{
		"name": "Mike",
		"number": "770-134-2229"
	},
	{
		"name": "Igor",
		"number": "770-233-3461"
	}
]

def get_number(name):
	for entry in phonebook_data:
		# BAD
		# if phonebook_data[i].name == name:
		# GOOD
		if entry['name'] == name:
			print entry['number']

# Main loop
while 1:
	print """Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Search for an entry
6. Quit
	"""
	user_input = raw_input("What do you want to do (1-6)? ")
	# raw_input comes in as what data type? -- string! What are we expected? int
	# option 1
	# if(user_input == "1")
	# option 2
	try:
		convert_user = int(user_input)
	except ValueError:
		os.system("say 'What is your problem?'")
		print "You must enter a number!\n"
	else:
		# I tried to convert it and succeeded!
		if(convert_user == 1):
			name = raw_input("Enter a name to search for: ")
			get_number(name)
		elif(convert_user == 6):
			# user chose to quit, so leave the loop
			break



import os

while 1:
	print """Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
	"""
	user_input = raw_input("What do you want to do (1-5)?")
	try:
		convert_user = int(user_input)
	except ValueError:
		os.system('clear')
		print "You must enter a number!\n"
	else:
		if((convert_user < 1) or (convert_user > 5)):
			os.system('clear')
			print "Invalid option"
		elif(convert_user == 5):
			break

