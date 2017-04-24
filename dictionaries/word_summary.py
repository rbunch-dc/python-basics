# Write a letter_histogram function that takes a word as its input, 
# and returns a dictionary containing the tally of how many times 
# each letter in the alphabet was used in the word. For example:

# >>> letter_histogram('banana')
# {'a': 3, 'b': 1, 'n': 2}

def letter_histogram(word):
	histo = {}
	for i in word:
		if not histo.has_key(i):
			histo[i] = 1
		else:
			histo[i] += 1
	print histo

user_word = raw_input("Please enter a word to histo: ")
letter_histogram(user_word)

def letter_histogram2(word):
	histo = {}
	for i in word:
		if histo.has_key(i):
			histo[i] += 1
		else:
			histo[i] = 1
