ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
# Write a python expression that gets the email address of Ramit.
ramits_email = ramit['email']

# Write a python expression that gets the first of Ramit's interests.
ramits_first_interest = ramit['interests'][0]

# Write a python expression that gets the email address of Jasmine.
jasmine_email = ramit['friends'][0]['email']

# Write a python expression that gets the second of Jan's two interests.
jans_second_interest = ramit['friends'][1]['interests'][1]

# In this exercise, are you using dynamic keys or fixed keys?
# Fixed