answer = 5
guess = 0
while guess != answer:
    guess = input('Guess a number between 1 and 10: ')
    if guess == answer:
        print('You got it!')
        break
    else:
        print('Wrong! Try again!')
