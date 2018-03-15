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


### MAIN ###

string_length = get_length()

pluck_position = get_pluck_position(string_length)
