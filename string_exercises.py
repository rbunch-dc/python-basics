# a_string = "My name is Rob"
# new_string = ""
# for letter in a_string:
# 	# print(letter)
# 	new_string += letter.upper()
# print new_string

# Given a string, print the string uppercased. #string #easy
# a_string = "Capitalize me"
# print a_string.upper()

# reverse_me = "I'm a string"
# print reverse_me
# new_string = reverse_me[::-1]
# print new_string
# characters_from_string = []
# for character in reverse_me:
# 	characters_from_string.append(character)
# characters_from_string.reverse()
# print characters_from_string
# print("".join(characters_from_string))
# reverse_as_list = list(reverse_me)
# print (reverse_as_list)
# characters_from_string = list(reverse_me)
# characters_from_string.reverse()
# print("".join(characters_from_string))

# a_string = "My name is Rob"
# new_string = ""
# for i in range(0,len(a_string)):
# 	# print(letter)
# 	last_index = len(a_string)-1
# 	letter_stepping_backwards = last_index - i
# 	new_string += a_string[letter_stepping_backwards]
# print new_string

# Given a paragraph of text as a string, print the paragraph in leetspeak. 
# To translate a string to leetspeak, you need to replace make the following 
# character replacements (treat all input characters as uppercase):

# A => 4
# E => 3
# G => 6
# I => 1
# O => 0
# S => 5
# T => 7
# Example: Leet => l337

# leet_string = "Leet"
# leet_string_as_list = list(leet_string)
# leet_speak = ""
# for character in leet_string_as_list:
# 	if(character.upper() == "A"):
# 		# leet_string_as_list.remove(character)
# 		# leet_string_as_list.insert(character, "4")
# 		leet_speak += "4"
# 	elif(character.upper() == "E"):
# 		leet_speak += "3"
# 	elif(character.upper() == "G"):
# 		leet_speak += "6"
# 	elif(character.upper() == "I"):
# 		leet_speak += "1"
# 	elif(character.upper() == "O"):
# 		leet_speak += "0"
# 	elif(character.upper() == "S"):
# 		leet_speak += "5"
# 	elif(character.upper() == "T"):
# 		leet_speak += "7"
# 	else:
# 		leet_speak += character
# print leet_speak

# leet_list = [
# 	["A","4"],
# 	["E","3"],
# 	["G","6"],
# 	["I","1"],
# 	["O","0"],
# 	["S","5"],
# 	["T","7"]
# ]
# leet_string = "Leet Loot Noob"
# leet_paragraph = leet_string.upper()
# for old,new in leet_list:
# 	print "This is old: " + old
# 	print "This is new: " + new
# 	leet_paragraph = leet_paragraph.replace(old,new)
# print leet_paragraph


# Long-long Vowels

# Given a word as a string, print the result of extending any long vowels 
# to the length of 5. Examples:

# Good => Goooood
# Cheese => Cheeeeese
# Man => Man
# Spoon => Spooooon

string_to_test = "Spoonn"
result = ""
current = ""
previous = ""

for i in range(0,len(string_to_test)):
	current = string_to_test[i]
	if (current == previous) and (current != "n") :
		result = result + 4 * current
	else:
		result = result + current
	previous = current
print result


# Caesar Cipher

# Given a string, print the Caesar Cipher (or ROT13) of that string. 
# What is Caesar Cipher? http://practicalcryptography.com/ciphers/caesar-cipher/

# Use your solution to decipher the following text: 
# "lbh zhfg hayrnea jung lbh unir yrnearq"

def decrypt_function(encrypted_letter):
	try:
		number = encrypted_list.index(encrypted_letter)
	except ValueError:
		# Do this!
		decrpyted_message.append(encrypted_letter)
	else:
		decrpyted_message.append(decrpyted_list[number])

message = "lbh zhfg hayrnea jung lbh unir yrnearq!"
decrpyted = "abcdefghijklmnopqrstuvwxyz"
encrypted = "nopqrstuvwxyzabcdefghijklm"
message_list =  list(message)
decrpyted_list = list(decrpyted)
encrypted_list = list(encrypted)
decrpyted_message = []

for i in range(0,len(message_list)):
	decrypt_function(message_list[i])

final_decrypted_message = "".join(decrpyted_message)
print (final_decrypted_message)

