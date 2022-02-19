import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Let's play Rock, Paper, Scissors!")
player=input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n")

computer_random=random.randint(0,2)
#ROCK
if player=="0":
  print("Player chose Rock")
  print(rock)
  if computer_random==0:
    print("Computer chose Rock")
    print(rock)
    print("It's a tie")
  elif computer_random==1:
    print("Computer chose Paper")
    print(paper)
    print("You Lose!")
  elif computer_random==2:
      print("Computer chose Scissors")
      print(scissors)
      print("You Win!")
#PAPER
elif player=="1":
  print("Player chose Paper")
  print(paper)
  if computer_random==0:
    print("Computer chose Rock")
    print(rock)
    print("You Win!")
  elif computer_random==1:
    print("Computer chose Paper")
    print(paper)
    print("It's a Tie!")
  elif computer_random==2:
    print("Computer chose Scissors")
    print(scissors)
    print("You Lose!")
#SCISSORS
elif player=="2":
  print("Player chose Scissors")
  print(scissors)
  if computer_random==0:
    print("Computer chose Rock")
    print(f"{rock}")
    print("You Lose!")
  elif computer_random==1:
    print("Computer chose Paper")
    print(paper)
    print("You Win!")
  elif computer_random==2:
    print("Computer chose Scissors")
    print(scissors)
    print("It's a Tie!")
else:
  print("Incorrect Input")

