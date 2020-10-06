import random as rn

rando = rn.randint(1,100)
numbers = 0

print('guess a number between 1-100')

while numbers < 7:
    guess = int(input('enter guess: '))
    numbers +=1
    if guess > rando:
        print('your guess is too high')
        numbers +=1
    elif guess < rando:
        print('your guess is too low')
        numbers += 1
    else:
        print('great job guessing the number. You got it in ' + '%s' %(numbers) + ' tries')
