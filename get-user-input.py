#! /usr/bin/python


### FUNCTIONS ###

def get_length(): 

   print('Length of string:')
   string_length = raw_input('> ')

   try: 
      string_length = float(string_length)
   except ValueError:
      print('Please enter a number...')
      get_length()

   return string_length

def get_pluck_position(string_length):

   print('Position of pluck:')
   pluck_position = raw_input('> ')

   try:
      pluck_position = float(pluck_position)
   except ValueError:
      print('Please enter a number...')
      get_pluck_position(string_length)

   if (pluck_position <= 0) or (pluck_position >= string_length):
      print('Choose a position between 0 and '+str(string_length))
      get_pluck_position(string_length)

   return pluck_position

def get_pluck_displacement():

   print('Displacement of pluck')
   pluck_displacement = raw_input('> ')

   try:
      pluck_displacement = float(pluck_displacement)
   except ValueError:
      print('Please enter a number...')
      get_pluck_displacement()

   return pluck_displacement()

def get_time():

   print('Time elapsed during calculation:')
   time = raw_input('> ')

   try:
      time = float(time)
   except ValueError:
      print('Please enter a number...')
      get_time()

### MAIN ###
string_length = get_length()
pluck_position = get_pluck_position(string_length)
pluck_displacement = get_pluck_displacement()
time = get_time()
