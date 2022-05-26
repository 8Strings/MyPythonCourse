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

#Write your code below this line 👇
import random
userchoice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

userchoice = int(userchoice)
if userchoice == 0:
  print("User chose:\n" + rock)
elif userchoice == 1:
  print("User chose:\n" + paper)
else:
  print("User chose:\n" + scissors)
  
CPUchoice = random.randint(0, 2)
if CPUchoice == 0:
  print("Computer chose:\n" + rock)
elif CPUchoice == 1:
  print("Computer chose:\n" + paper)
else:
  print("Computer chose:\n" + scissors)

# Print outcomes
if userchoice == CPUchoice:
  print("It's a draw!")
elif userchoice == CPUchoice + 1:
  print("You win!")
elif userchoice == CPUchoice - 1:
  print("You lose.")
elif userchoice == CPUchoice + 2:
  print("You win!")
elif userchoice == CPUchoice - 2:
  print("You lose.")
  


