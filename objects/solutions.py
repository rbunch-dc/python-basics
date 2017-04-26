class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def __repr__(self):
        return 'This is Person object with name: %s %s %s' % (self.name, self.email, self.phone)

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1

    def print_contact_info(self):
        print self.email, self.phone

    def add_friend(self, other_person):
    	self.friends.append(other_person)

    def num_friends(self):
    	print len(self.friends)

# Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
jordan = Person("Jordan", "jordan@aol.com",'495-586-3456')
# Have sonny greet jordan using the greet method.
sonny.greet(jordan)
# Have jordan greet sonny using the greet method.
jordan.greet(sonny)

# pass sonny object to friends instance attr
# jordan.friends.append(sonny)
# Print off jordan's frist friends name
# print jordan.friends[0].name

jordan.num_friends()
jordan.add_friend(sonny)
# print jordan.friends.append(sonny)
jordan.num_friends()

# Write a print statement to print the contact info (email and phone) of Sonny.
# print sonny.email, sonny.phone
# Write another print statement to print the contact info of Jordan.
# print jordan.email, jordan.phone
sonny.print_contact_info()
jordan.print_contact_info()

print "$$$$$$$$$$$$$$$$$$$$$$"
print sonny
print "$$$$$$$$$$$$$$$$$$$$$$"

# Create a class Vehicle. A Vehicle object will have 3 attributes:
class Vehicle(object):
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
	def print_info(self):
		print self.make, self.model, self.year		
# A vehicle is created thus:
car = Vehicle('Nissan', 'Leaf', 2015)
# And you can access it's attributes individually like so:
car.print_info()

