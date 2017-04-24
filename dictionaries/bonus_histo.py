# Bonus Challenge

# Given a histogram tally (one returned from either letter_histogram or word_summary),
# print the top 3 words or letters.

def para_histogram(paragraph):
	para_list = paragraph.split()
	histo = {}
	for i in para_list:
		if not histo.has_key(i):
			histo[i] = 1
		else:
			histo[i] += 1
	return histo

def letter_histogram(word):
	histo = {}
	for i in word:
		if not histo.has_key(i):
			histo[i] = 1
		else:
			histo[i] += 1
	return histo

user_word = raw_input("Please enter a word to histo : ")
histo = letter_histogram(user_word)
chads_list = []
for key in histo:
	chads_list.append([key,histo[key]])
chads_list.sort(key = lambda x: x[1])
print chads_list[-1]
print chads_list[-2]
print chads_list[-3]


user_word = raw_input("Please enter a word to histo : ")
histo = letter_histogram(user_word)
max_key = ""
new_dict = {}
while len(new_dict.keys() <= 2):
	max_number = 0
	for i in histo:
		if histo[i] > max_number:
			max_number = histo[i]
			max_key = i
	del histo[max_key]
	new_dict[max_key] = max_number
print new_dict

