# print "Hello, World!"
# Print two different things on the same line
# print ("Hello, World", "Again")

# This won't work!!
# print "This
# is a couple
# lines of a sentence. 
# Please print."

# This will...
# print """This
# will ignore the new lines
# until it sees another
# three double quotes"""

# print 'one'; print 'two';
# if x == 1: print 'one';
# ============
# print 'one'
# print 'two'
# if x == 1:
# 	print 'one'
# cond1 = (x % 2 / 6 + result_of_data == 5);
# cond2 = (x % 2 / 6 + result_of_data == 5)
# if ( cond1 || cond2 ):
# 	print "I hate the last line."


# Variables - string, number, letters, any other stuff that you can make 
# with a keyboard and you want stash soemthing that's not fast, 
# into something that is fast
# There is no declaration.
# In JS.... var name = "Shane";
# name = "Robert Bunch"
# Python is not heavily typed (for instance C#)
# name = "Robert " + "Bunch"
# first_name = "Robert";
# last_name = "Bunch";
# full_name = first_name + " " + last_name
# print full_name

# Arithmatic
# the_meaning_of_life = 40 + 2
# print the_meaning_of_life
# print the_meaning_of_life / 2
# print the_meaning_of_life % 5
# returns 8 because both are ints
# print the_meaning_of_life / 5
# print int(30.5 / 5.2)

# print 4 + "Joe"
# print 4 * "Joe"

# Data types (variables types)
# - Strings - English type stuff for people (in yellow)
# - Numbers - something with digits and stuff that goes with digits (. -)
# --- Floats, Integers
# - Booleans - True or False. 1 or 0. Yes or no. On or Off
# - lists - list of variables in one variable
# - dictionary - variables of variables
# - objects - Deal with it later

# # Strings
# first_name = "Rob"
# last_name = "Bunch"

# nickname = "Rob "the man" Bunch" BAD!
# nickname = 'Rob "the man" Bunch'
# nickname = "Rob \"the man\" Bunch"
# nickname = `Rob \"the man\" Bunch`


# formatted_string = "Hello, {} {}".format(first_name, last_name)
# print formatted_string
# print "Hello " + first_name + " " + last_name
# Placeholders
# print "Hello, %s %s" % (first_name, last_name)
# print "Hello, %s %s for the %drd time!" % (first_name, last_name, 3)

# Floats
# pi_the_magic_float = 3.14
# print pi_the_magic_float
# print type(pi_the_magic_float)
# make_me_an_integer = int(pi_the_magic_float)
# make_me_a_string = str(pi_the_magic_float) # "3.14"
# print make_me_an_integer
# print (.2 + .1)

# Booleans - true or false
# the_truth = True
# print type(the_truth)
# the_lie = False
# print type(the_lie)

# Raw Input
# first_name = raw_input("First Name: ")
# last_name = raw_input("Last Name: ")

# Conditionals
# 1 = means you want to assign the thing on the left to the thing on the right
# 2 = means you want to compare whats on the left with whats on the right

# if(first_name == last_name):
# 	print "Your first name is the same as yoru last name?"

# if you want to compare = or greater than, <=
# age = raw_input("How old are you?")
# age_as_int = int(age)
# # print type(age)
# if(age_as_int != 99):
# 	print "You are not 99 years old!"
# if(age_as_int >= 21):
# 	print "You can buy beer."
# elif(age_as_int >= 18):
# 	print "A few more years"
# else:
# 	print "You are underage."

# import random
# random_number = random.randint(1,10)

# Loop - keep doing something until I tell you to stop
# not_guessed = True
# while not_guessed:
# 	guess_a_number = raw_input("Guess a number between 1 and 10.")
# 	if (int(guess_a_number) == random_number):
# 		print "You guessed the number!";
# 		not_guessed = False;

student1 = "Marissa"
student2 = "Merilee"
student3 = "Daniel"
student4 = "Chris"

# print(student1,student2,student3,student4)

# list is a single variable with a bunch of numbered parts
# the number that an element is in, is called the "Index"
students = [
	"Marissa",
	"Merliee",
	"Daniel",
	"Chris",
	"Chad",
	"Shane",
	"Stephen",
	"Drew"
]
# The first element in a list is always 0. 
# The second element is always 1

# print (students)
# print(students[1])
# print(students[7])
# # print(students[8])
# print(students[-1])

atlantaTeams = [
	"Falcons",
	"Braves",
	"Hawks",
	"Thrashers"
]

# print (atlantaTeams[0])
print (atlantaTeams)
# To add an element to the END of a list, you can use the append method
atlantaTeams.append("Atl United")
print (atlantaTeams)

# Pop -- REMOVES the last item on the list
# students.pop()
# print students

# To delete an index, you can use the remove method
atlantaTeams.remove("Thrashers")
print (atlantaTeams)
# We can insert into any indicie with the insert method
atlantaTeams.insert(0,"Tom Brady's Team")
print (atlantaTeams)

teams_as_a_string = "Falcons,Braves, Hawks, Thrashers"
teams_as_a_list = teams_as_a_string.split(",")
print (teams_as_a_list)
# Sort will CHANGE the list
# atlantaTeams.sort();
# print (atlantaTeams)
# Sorted will sort, but NOT CHANGE the list
# copy_of_atlanta_teams = sorted(atlantaTeams);
# print (copy_of_atlanta_teams)

# copy_of_atlanta_teams.reverse();
# print (copy_of_atlanta_teams);

# length_of_atlanta_teams = len(copy_of_atlanta_teams)
# print (length_of_atlanta_teams)
# print (copy_of_atlanta_teams[-1])
# print (copy_of_atlanta_teams[length_of_atlanta_teams-1])

# print len(copy_of_atlanta_teams[0])

# The other type of loop... For
# for i in range(1,10):
# 	print i

# For Loop Format:
# [for] [what_you_want_to_call_the_thing_you_are_on] [in] [variable_looping_through]
# for student in students:
# 	# print student
# 	if(student == "Chris"):
# 		print "Welcome, Chris!"
# 	else:
# 		print "You are not Chris"

# Set up a for loop... but the range, will be 0 to len-1
# students_length = len(students)
# for i in range(0,students_length):
# 	print(students[i])

for i in range(0,10,2):
	print(i)

# If you want a portion of a list, you can use the [x:y] format
# This will create a COPY of the array, does not mutate or change the origianl
# it will start at the Xth element, and will stop at the Yth
print(students)
second_and_third = students[1:3]
print second_and_third
print(students)
all_but_the_first = students[1:]
# all_but_the_first = students[1:len(students)]
print all_but_the_first