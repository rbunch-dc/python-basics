width = int(raw_input("Enter width "))
height = int(raw_input("Enter height "))
for i in range(height):
	if i == 0:
		print "* "*(width)
	elif i in [(height-1)]:
		print ("* "*(width))
	else:
		print("*"+"  "*(width-2)+" *")
input()