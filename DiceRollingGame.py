#Ask to roll dice
# if yes give two random numbers
# if no then close the program
import random

while True:
  Choice = input('Roll the dice? (y/n):').lower()
  if Choice == 'y':
      die1 = random.randint(1,6)
      die2 = random.randint(1,6)
      print (f'({die1},{die2})')
  elif Choice == 'n':
      print("thankyou")
      break
  else:
      print ('Error ....')