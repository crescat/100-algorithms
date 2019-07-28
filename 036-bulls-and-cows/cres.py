# Day 36: Bulls & Cows
import random
import re

def check(a, b):
    bulls = sum(a[i] == b[i] for i in range(len(a)))
    cows = len(set(a) & set(b)) - bulls
    return bulls, cows


def get_input():
    while True:
        numbers = input('Please type in 4 numbers in range 0-9! Seperate number by space: \n')
        if re.match('\d \d \d \d', numbers) and len(numbers) == 7:
            return numbers
        else:
            print('Invalid input!')


def get_random_unique_numbers():
    lst = []
    while len(lst) < 4:
        num = random.randint(0, 9)
        if num not in lst:
            lst.append(num)
    return lst


def game(gamemode = 'manual'):
    ans = get_random_unique_numbers()
    mainloop = True
    trial = 1
    while mainloop:
        if gamemode == 'manual':
            num_input = get_input()
            numbers = [int(x) for x in num_input.split()]
        elif gamemode == 'auto':
            numbers = get_random_unique_numbers()
            print(tuple(numbers))

        bulls, cows = check(ans, numbers)
        print('{} bulls, {} cows'.format(bulls, cows))

        if ans == numbers:
            mainloop = False
            print('You won! Your number of trial is {}'.format(trial))

        trial += 1

game(gamemode = 'auto')
# gamemode 'auto' will automatically form random numbers
# to match the correct numbers.
# gamemode 'manual'(by default) will take in manually-given
# numbers to continue the game.
