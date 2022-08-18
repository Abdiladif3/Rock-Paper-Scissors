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
options = [rock, paper, scissors]

while True:
  my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
  if my_choice not in [0, 1, 2]:
    print("Please choose a digit from the given options.")
    continue
  print(options[my_choice])
  
  computer_choice = random.randint(0, 2)
  print(f"Computer chose: {options[computer_choice]}")
  
  # 0 > 2
  # 2 > 1
  # 1 > 0
  
  win = "You win! \n"
  loss = "You lose! \n"
  draw = "It's a draw! \n"
  ''
  if my_choice == 0 and computer_choice == 2:
    print(win)
  elif my_choice == 2 and computer_choice == 1:
    print(win)
  elif my_choice == 1 and computer_choice == 0:
    print(win)
    
  elif my_choice == 2 and computer_choice == 0:
    print(loss)
  elif my_choice == 1 and computer_choice == 2:
    print(loss)
  elif my_choice == 0 and computer_choice == 1:
    print(loss)
  
  else:
    print(draw)
  ''
  
  continuation = input("Do you want to keep playing? Type Yes or 'y' if you do, or type anything else if you want to quit: \n")
  continuation = continuation.lower()
  if continuation in ['yes', 'y']:
    continue
  else:
    print("Thank you for playing! ")
    break
