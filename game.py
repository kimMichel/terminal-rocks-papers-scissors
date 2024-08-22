import random

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor: '))

computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print('The computer choose Rock!')
elif computer_choice == 1:
    print('The computer choose Paper!')
else:
    print('The computer choose Scissor!')

if choice == computer_choice:
    print('Its draw!')
elif choice > computer_choice & computer_choice != 0:
    print('You win!')
elif choice > computer_choice & computer_choice == 0:
    print('You loose!')
elif choice < computer_choice & computer_choice != 2:
    print('You loose!')
elif choice < computer_choice & computer_choice == 2:
    print('You win!')