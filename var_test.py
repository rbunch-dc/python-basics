x = 3
y = 0
def get_number():
	global y
	y = 5 #global y set to 5

def calc():
	# x is now local
	global x #tells teh function to use global x (not local)
	# x = x + y #because we used global x, we can add to it (it already exists)
	w = x + y #because we used global x, we can add to it (it already exists)
	# x = 5
	print w # will print the result of global x + global y
print y # will print global y, which is 0, not changed since line 2
get_number() #this will change global y from 0 to 5
calc()
print x # will print GLOBAL x, which is 8 (global x + global y)
print y  #will print GLOBAL y, whcih was changed by get_number
print w #will error, because there is no global w
