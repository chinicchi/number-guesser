import random

range_num = int(input('Enter a number : '))
random_num = random.randint(1, range_num)

guess_num = int(input(f'Guess a number between 1 and {range_num} : '))

still_guess = True
while still_guess:
    if guess_num > random_num:
        guess_num = int(input(f'Number is too high. Guess another number between 1 and {range_num} : '))
    elif guess_num < random_num:
        guess_num = int(input(f'Number is too low. Guess another number between 1 and {range_num} : '))
    else:
        print(f'Your guess is correct. The correct number is {random_num}')
        still_guess = False