# 1) Declare two variables, a string and an integer 
# named "fullName" and "age". Set them equal to your name and age.
# Python is dynamic. We dont ahve to "Declare" with var
fullname = "Daniel Oliva"
age = 23

# 2) Declare an empty array called "myArray". 
# Add the variables from #1 (fullName and age) to the empty array using the push method.
# Print to the console.

# So there are no arrays... btu there are lists
my_array = []
# there is no push... but there append
my_array.append(fullname)
my_array.append(age)
print (my_array)

# 3) Write a simple function that takes no parameters called "sayHello". 
# Make it print "Hello!" to the console when called.
# Call the function.

def say_hello():
	print ("Hello!")
say_hello()

# 4) Declare a variable named splitName and set it equal to
# fullName split into two seperate objects in an array.
# (In other words, if the variable fullName is equal to "John Smith", then splitName should 
# equal ["John", "Smith"].)
# Print splitName to the console.
# HINT: Remember to research the methods and concepts listed in the instructions PDF.

# This is easy...
split_name = fullname.split()
print (split_name)

# 5) Write another simple function that takes no parameters called "sayName".
# When called, this function should print "Hello, ____!" to the console, where the blank is 
# equal to the first value in the splitName array from #4.
# Call the function.  (In our example, "Hello, John!" would be printed to the console.)

def say_name():
	print ("Hello, " + split_name[0])

say_name()

# 6) Write another function named myAge.  This function should take one parameter: the year you 
# were born, and it should print the implied age to the console.
# Call the function, passing the year you were born as the argument/parameter.
# HINT: http://www.w3schools.com/js/js_functions.asp

def my_age(year_born):
	print (2017-year_born)
my_age(1991)

# 7) Using the basic function given below, add code so that sum_odd_numbers will print to the console the sum of all the odd numbers from 1 to 5000.  Don't forget to call the function!
# HINT: Consider using a 'for loop'.

def sum_odd_numbers():
	sum = 0
	# for i in range(1,5001):
		# if (i % 2 == 1):
			# any number divided 2 with a remainder of 1 MUST be odd
			# sum += i
	for i in range(1,5001,2):
		sum += i
	return sum
print (sum_odd_numbers())

# break example
i = 0
while 1: #this will run forever...
	i += 1
	print i
	if (i == 10):
		break

print ("We broke out of the loop!")