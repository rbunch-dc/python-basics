# Word Summary

# Write a word_histogram function that takes a paragraph of text as its input, and returns a dictionary containing the tally of how many times each letter in the alphabet was used in the text. For example:

# >>> word_histogram('To be or not to be')
# {'to': 2, 'be': 2, 'or': 1, 'not': 1}
# In this exercise, are you using dynamic keys or fixed keys?

def letter_histogram(paragraph):
	para_list = paragraph.split()
	histo = {}
	for i in para_list:
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
