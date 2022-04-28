import random

range_num = int(input('Enter range number from 1 to : '))

list_num = list(range(1,range_num+1))
guess_num = random.choice(list_num)

high_low_correct = input(f'Your number is {guess_num}. Enter h (too high) or l (too low) or c (correct) : ')

still_guess = True
while still_guess:
    if high_low_correct.lower() == 'h':
        for element in list(list_num):
            if element >= guess_num:
                list_num.remove(element)
        guess_num = random.choice(list_num)
        high_low_correct = input(f'Your number is {guess_num}. Enter h (too high) or l (too low) or c (correct) : ')
    elif high_low_correct.lower() == 'l':
        for element in list(list_num):
            if element <= guess_num:
                list_num.remove(element)
        guess_num = random.choice(list_num)
        high_low_correct = input(f'Your number is {guess_num}. Enter h (too high) or l (too low) or c (correct) : ')
    elif high_low_correct.lower() == 'c':
        print(f'Your number is {guess_num}. The computer guessed correctly!')
        still_guess = False
    else:
        high_low_correct = input(f"I don't understand. Enter h (too high) or l (too low) or c (correct) : ")