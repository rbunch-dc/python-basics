class Person(object):
    def __init__(self,name,gender,buggsBunny):
        self.name = name
        self.gender = gender
        self.species = "Human"
        # self.number_of_arms = number_of_arms
        self.phone = {
            "cell": buggsBunny,
            "home": "Who has a home phone anymore?"
        }
        # pointless_variable = "Congress"
        # print pointless_variable

    def greet(self, other_person):
        print "Hello %s, I am %s!" % (other_person, self.name)

    def print_contact_info(self):
        if(self.phone['cell'] != ""):
            print "%s's number is %s" % (self.name, self.phone['cell'])

marissa = Person("Marissa", "female", "770-777-7777")
print marissa.name + " " + marissa.gender
print marissa.species
merilee = Person("Merilee","female", "404-777-7777")
print merilee.species
merilee.species = "Robot"
print merilee.species
# print merilee.number_of_arms
print marissa.phone['cell']
print marissa.phone['home']
# print marissa.pointless_variable
marissa.greet("Rob")
marissa.print_contact_info()
merilee.print_contact_info()



class Vehicle(object):
    def __init__(self, make2, model2, year2):
        self.make = make2
        self.model = model2
        self.year = year2

    def print_info(self):
        print self.year, self.model, self.make

    def change_year(self, new_year):
        self.year = new_year

    def get_year(self):
        return self.year

david_cummings_car = Vehicle("Mcclaren",'Mp4-12c', 2013)
david_cummings_car.print_info()
david_cummings_car.change_year(2015)
david_cummings_car.year = 2015
print (david_cummings_car.year)
print (david_cummings_car.get_year())