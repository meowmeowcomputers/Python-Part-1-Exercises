import random
answer = random.randint(1, 10)
guess = 0
guessnum = 5

while guess != answer:
    if guessnum > 0:
        guess = int(input('Guess a number between 1 and 10: '))
        if guess == answer:
            print('You got it!')
            again = str.input('Play again? (y/n)')
            if str.lower(again) == 'y':
                guess = 0
                guessnum = 5
                answer = random.randint(1, 10)
            elif str.lower(again) == 'n':
                print('See you later!')
                break
            else:
                print('You had 2 options, and you went to a third!?! \n I\'ll assume you want to play again')
                guess = 0
                guessnum = 5
                answer = random.randint(1, 10)
        elif guess > 5:
            print('Your guess is too high!')
            guessnum -= 1
            print('You have {g} guesses left' .format(g=guessnum))
        elif guess < 5:
            print('Your guess is too low!')
            guessnum -= 1
            print('You have {g} guesses left' .format(g=guessnum))
    else:
        print('You ran out of guesses!')
        break
