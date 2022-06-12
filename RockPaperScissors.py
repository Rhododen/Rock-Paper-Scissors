from ast import While
import random

options = ["R", "P", "S"]

print('''
Kindly make a move by picking one of the following
R for Rock
P for Paper
S for Scissors''')



x = random.choice(options)



def moves():

  while True:
    player = input("Your move: ")
    player = player.upper()

    if player in options:
      break
    else:
      print("Not valid")

  if player == "R":
    player = "Rocks"
    print("Player: Rock")
  elif player == "P":
    player = "Paper"
    print("Player: Paper")
  else:
    player = "Scissors"
    print("Player: Scissors")


  cpu = x
  if cpu == "R":
    cpu = "Rock"
    print("CPU: Rock")
  elif cpu == "P":
    cpu = "Paper"
    print("CPU: Paper")
  else:
    cpu = "Scissors"
    print("CPU: Scissors")

  if cpu == player:
    print("TIE!!!")
  elif player == "Rock" and cpu == "Scissors":
    print("You win!")
  elif player == "Paper" and cpu == "Rock":
    print("You win!")
  elif player == "Scissors" and "Paper":
    print("You win!")
  else:
    print("You lose!")

moves()




while True:
  print('''Do you want to play again?
  Y for Yes
  N for No
  ''')
  replay = input("> ").upper()
  if replay == "Y":
    moves()
  elif replay == "N":
    print("See you next time")
    break
  else:
    print("Kindly select one of the stated options")




    
    





  