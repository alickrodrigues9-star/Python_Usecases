# generate a valid number
# ask the user to guess in loop till correct number is guessed.

import random

number_to_guess = random.randint(1,100)

#userinput = input("Guess a number?")
#guess = int(userinput)
#print (number_to_guess)

while True:
  try:
     guess = int(input("Guess a number?"))

     if guess < number_to_guess:
         print ("Too low")
     elif guess > number_to_guess:
         print ("too high")
     else:
         print("correct guess")
         break 

  except ValueError:
    print("Enter a valid number...")
    

