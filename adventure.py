user_input = raw_input("Enter Input")
try:
	convert_user = int(user_input)
except ValueError:
	print "You must enter a number!"
else:
	print "Thanks for the number!"