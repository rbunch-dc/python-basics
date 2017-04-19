import random
secret_number = random.randint(1,10);
# print secret_number

# Hard code for now
secret_number = 5
keep_asking = True
number_of_guess = 5
while (keep_asking):
	if(number_of_guess == 0):
		play_again = raw_input("You ran out of guesses. Would you like to play again. Y or N?")
		if(play_again == "Y"):
			number_of_guess = 5
		elif(play_again == "N"):
			keep_asking = False;
			print "Goodbye, coward"
	else:
		print ("You have %d guesses left")  % (number_of_guess)
		guess_a_number = raw_input("Guess a number between 1 and 10.")
		if (int(guess_a_number) == secret_number):
			print "You guessed the number!";
			keep_asking = False;
			# number_of_guess = 0;
			
		elif (int(guess_a_number) < secret_number):
			print "%d is too low" % (int(guess_a_number))
			# number_of_guess = number_of_guess - 1
			# number_of_guess += 1
		elif(int(guess_a_number) > secret_number):
			print "%d is too high" % (int(guess_a_number))
			# number_of_guess = number_of_guess - 1
		number_of_guess -= 1

	# else:
	# 	print "%d is too high" % (int(guess_a_number))

