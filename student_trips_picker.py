students = [
	"Marissa",
	"Merliee",
	"Daniel",
	"Chris",
	"Chad",
	"Shane",
	"Stephen",
	"Drew",
	# "Guido",
	"Porscha",
	"Carla",
	"YingRong",
	# "Ian",
	"Nick",
	# "Michael",
	"Hayes"
]

# Take the list "students", randomly pair 2 until all students have been paired
import random
# 1. Grab a random index from students
# 2. then remove that student from the list
# 3. Repeat until len(list) = 0

def get_student():
	# Get a random number from the indicies left in students
	rand_num = random.randint(0,len(students)-1)
	current_student = students[rand_num]
	students.remove(current_student)
	return current_student


while students:
	student1 = get_student()
	student2 = get_student()
	student3 = get_student()	
	print ("%s %s %s") % (student1,student2,student3)


# for i in range(0,len(students))
# for student in students
# while students:
# 	get_student()
# 	# Get a random number from the indicies left in students
# 	rand_num = random.randint(0,len(students)-1)
# 	# print (rand_num)
# 	current_student = students[rand_num]
# 	students.remove(current_student)
# 	print current_student
# 	rand_num = random.randint(0,len(students)-1)
# 	current_student = students[rand_num]
# 	students.remove(current_student)
# 	print (" is paired with " + current_student)

print [0]
