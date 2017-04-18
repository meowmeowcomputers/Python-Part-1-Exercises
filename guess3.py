import random
answer = random.randint(1, 10)
guess = 0
while guess != answer:
    guess = input('Guess a number between 1 and 10: ')
    if guess == answer:
        print('You got it!')
    elif guess > 5:
        print('Your guess is too high!')
    elif guess < 5:
        print('Your guess is too low!')
