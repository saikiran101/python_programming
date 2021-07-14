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

game=[rock,paper,scissors]

user_chocie=int(input("0 is for rock, 1 is for paper, 2 is for scissors"))
print("user")
print(game[user_chocie])

computer= random.randrange(0,3)
print("computer")
print(game[computer])

if game[user_chocie]== game[computer]:
  print(" its a draw match")
elif game[user_chocie]==0 and game[computer]:
  print("computer won")
elif game[user_chocie] < game[computer[0]]:
  print("user won")